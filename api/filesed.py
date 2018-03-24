#! /usr/bin/env python
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2018-03-22 22:33:39
####################################################

import os
import sys
import re

class FileSed(object):
    def __init__(self, filename):
        self.filename = filename
        self.fileloc = []
        self.loc = {}
        linenumber = 0
        with open(self.filename) as fd:
            for line in fd:
                linenumber += 1
        self.linenumber = linenumber
        print("filename: %s:%d" % (self.filename, self.linenumber))
    def search(self, src):
        src = re.compile(src) 
        loc = []
        linenumber = 0
        with open(self.filename) as fd:
            for line in fd:
                linenumber += 1 
                if src.search(line):
                    loc.append(linenumber)
        return loc
    def reloc(self, loc):
        self.fileloc = []
        if not loc:
            self.fileloc = range(self.linenumber+1)
            return self.fileloc
        self.loc = {}
        """
        x
        x,y
        x~y
        x,+y
        '$'
        /xx/
        """
        print("loc: %s %s" % (loc, type(loc)))
        address1,step,address2=0,1,0
        if isinstance(loc, int):
            # integer
            loc = int(loc)
            self.loc["start"] = loc
            self.loc["end"] = self.loc["start"]
        elif isinstance(loc, str):
            if loc == "$":
                self.loc["start"] = self.linenumber
                self.loc["end"] = self.linenumber
            elif re.match("[0-9]+~[0-9]+", loc):
                "x~y"
                loc = re.findall("([0-9]+)~([0-9]+)", loc)
                self.loc["start"] = int(loc[0][0])
                self.loc["step"] = int(loc[0][1])
                self.loc["end"] = self.linenumber
            elif loc.startswith('/') and loc.endswith('/'):
                '/xxx/'
                loc = loc.strip('/')
                start = self.search(loc)
                self.fileloc = start
                #if not start:
                #    start = self.linenumber
                #elif len(start) >= 2:
                #    start = start[0]
                #else:
                #    start = start[0]
                #self.loc["start"] = start
                #self.loc["end"] = start + 1
        else:
            if len(loc) != 2:
                print("ERROR: addr param invalid.")
                return
            start = loc[0]
            end = loc[1]
            if isinstance(start, int):
                self.loc["start"] = int(start)
            elif start == "$":
                self.loc["start"] = self.linenumber
            elif start.startswith('/') and start.endswith('/'):
                start = start.strip("/")
                start = self.search(start)
                if not start:
                    start = self.linenumber
                elif len(start) >= 2:
                    start = start[0]
                else:
                    start = start[0]
                self.loc["start"] = start
            # x,y
            # x,+y
            # '$', '/xx/'
            if isinstance(end, int):
                self.loc["end"] = int(end)
            elif end == "$":
                self.loc["end"] = self.linenumber
            elif end.startswith('/') and end.endswith('/'):
                end = end.strip("/")
                end = self.search(end)
                if not end:
                    end = self.linenumber
                elif len(end) >= 2:
                    end = end[-1]
                else:
                    end = end[0]
                self.loc["end"] = end
            elif end.startswith('+') and isinstance(end.strip('+'), int):
                self.loc["end"] = self.loc["start"] + int(end.strip("+"))
            # tuple or list addr param
        # print(self.loc)
        address1 = self.loc.get("start") or 1
        step     = self.loc.get("step") or 1
        address2 = self.loc.get("end") or 0
        # print(address1, step, address2)
        # x
        # x,y
        # x~y
        # x,+y
        # '$'
        # /xx/
        self.fileloc = self.fileloc or range(address1, address2 + 1, step)
        print("fileloc: %s" % self.fileloc)
        return self.fileloc
    def printf(self, loc=None):
        "[address1[ ,address2 ]] p"
        self.reloc(loc)
        curline = 0
        with open(self.filename) as fd:
            for line in fd:
                curline += 1
                if curline in self.fileloc:
                    print("{:03d} {:s}".format(curline, line.rstrip('\n')))
                    # print(line.rstrip('\n'))
    def replace(self, src, dst, loc=None, inplace=False, flag=None):
        "[address1[ ,address2 ]] s/pattern/replace/[flag]"
        """
            g            全局匹配,会替换文本行中所有符合规则的字符串;
            None         默认替换第1个符合规则的字符串; 
            n            十进制数字,表示替换第n个符合规则的字符串;
            p            替换第1个符合规则的字符串,并输出到标准输出;
            w            替换第1个符合规则的字符串,并写入到磁盘文件;
        """
        self.reloc(loc)
        re_src = re.compile(src)
        if not flag:
            count = 1
        elif flag == "g":
            count = 0
        elif flag in "pw":
            count = 1
        else:
            count = int(flag)
        curline = 0
        with open(self.filename) as fd:
            for line in fd:
                curline += 1
                if curline in self.fileloc:
                    leftspace = len(line.rstrip())
                    line = re_src.sub(dst, line, count=count)
                    leftspace -= len(line.rstrip())
                    # print("{:03d} {:s}".format(curline, line.rstrip('\n')))
                    print("%s%s" % (" "*leftspace, line.rstrip('\n')))
                else:
                    print(line.rstrip('\n'))
        # loc = self.reloc(loc)
    def delete(self, loc=None):
        "[address1[ ,address2 ]] d"
        self.reloc(loc)
        curline = 0
        with open(self.filename) as fd:
            for line in fd:
                curline += 1
                if curline in self.fileloc:
                    pass
                    # print(line.rstrip('\n'))
                else:
                    print(line.rstrip('\n'))
    def append(self, src, loc='$'):
        "[address1] a string"
        if not isinstance(loc, str) and not isinstance(loc, int):
            print("ERROR: must one addr parameter.")
            return
        self.reloc(loc)
        curline = 0
        with open(self.filename) as fd:
            for line in fd:
                curline += 1
                if curline in self.fileloc:
                    print("%s" % src)
                    print(line.rstrip('\n'))
                else:
                    print(line.rstrip('\n'))
    def insert(self, src, loc='$'):
        "[address1] i string"
        if not isinstance(loc, str):
            print("ERROR: must one addr parameter.")
            return
        self.reloc(loc)
        curline = 0
        with open(self.filename) as fd:
            for line in fd:
                curline += 1
                if curline+1 in self.fileloc:
                    print("%s" % src)
                    print(line.rstrip('\n'))
                else:
                    print(line.rstrip('\n'))

def filesed_test():
    filename = "test.txt"
    sed = FileSed(filename)
    #sed.printf()
    #sed.printf(("/@property/", "/@age/"))
    #sed.printf("/@property/")
    ## replace @ -> #
    #sed.replace("^[\s ]*@", "#", (8,18))
    #sed.replace("^[\s ]*@", "#", '8~2')
    # append print("hello world")
    sed.append('\tprint("hellor world")', '$')
    # insert if __name__ == "__main__":
    sed.insert('if __name__ == "__main__":', '$')
    sed.insert('####################', '/if __name__ ==/')


if __name__ == "__main__":
    filesed_test()

