#! /usr/bin/env python
# coding=utf-8

import os
import sys
import hashlib

def md5sum(filename):
    if not os.path.isfile(filename):
        return
    fd = open(filename, "rb")
    md5 = hashlib.md5()
    md5.update(fd.read())
    md5sum = md5.hexdigest()
    fd.close()
    return md5sum

def proc(filename):
    if os.path.isfile(filename):
        print("%s  %s" % (md5sum(filename), filename))

def help():
    help_info = """
Usage:
    python %s filename
    """ % os.path.basename(sys.argv[0])
    print("%s" % help_info)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        help()
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("ERROR: %s: No such file." % filename)
        sys.exit(1)
    proc(filename)

