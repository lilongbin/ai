#! /usr/bin/env python
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2018-01-15 22:52:33
####################################################

from chardet import detect, universaldetector

def filechardet(filename):
    enc = None
    with open(filename, "rb") as fd:
        rawdata = fd.read(1024)
        # enc = chardet.detect(rawdata)["encoding"]
        enc = chardet.detect(rawdata).get("encoding")
    # print(enc)
    return enc

def test(filename=""):
    def usage():
        print("Usage:\r\n\tfilechardet filename")
    if not filename:
        usage()
        return
    if not filename:
        filename = "chardettest.txt"
        with open(filename, "w") as fd:
            fd.write("hello world\r\n")
    fileenc = filechardet(filename)
    print("%s encoding: %s" % (filename, fileenc))
    return
    import codecs
    with codecs.open(filename, encoding=fileenc) as fd:
        for line in fd:
            print("%s" % line.rstrip())

def bigfilechardet(filename, block=256):
    detector = universaldetector.UniversalDetector()
    with open(filename, 'rb') as fd:
        bytes = fd.read(block)
        while bytes and not detector.done:
            detector.feed(bytes)
            bytes = fd.read(block)
    detector.close()
    # print(detector.result)
    return detector.result.get("encoding")

if __name__ == "__main__":
    import sys
    filename = ""
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    test(filename)

