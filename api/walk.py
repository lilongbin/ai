#! /usr/bin/env python
# coding=utf-8
import os

def getfiles(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for dirname in dirnames[:]:
            if len(dirname)>1 and dirname[0] == ".":
                dirnames.remove(dirname)
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def getdirs(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for dirname in dirnames[:]:
            if len(dirname)>1 and dirname[0] == ".":
                dirnames.remove(dirname)
        for dirname in dirnames:
            yield os.path.join(dirpath, dirname)

def test():
    for file in getfiles('.'):
        print('%s' % file)

if __name__ == '__main__':
    test()

