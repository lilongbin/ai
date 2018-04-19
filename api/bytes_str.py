#! /usr/bin/env python
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2018-03-24 18:09:56
####################################################

#在Python3中，我们需要编写接受str或bytes，并总是返回str的方法：
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    # Instance of str
    return value

#另外，还需要编写接受str或bytes，并总是返回bytes的方法：
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    # Instance of bytes
    return value

#在Python2中，需要编写接受str或unicode，并总是返回unicode的方法：
#python2
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    # Instance of unicode
    return value

#另外，还需要编写接受str或unicode，并总是返回str的方法：
#Python2
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    # Instance of str
    return vlaue

