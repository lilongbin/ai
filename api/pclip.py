#! /usr/bin/env python
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2018-01-13 14:31:03
####################################################

import pyperclip

def pclip_copy(info):
    if not info:
        return
    # copy info to clip board
    pyperclip.copy(info)

def pclip_paste():
    # paste from clip board
    info = pyperclip.paste()
    return info

def test():
    info = "pyperclip test hello world"
    pclip_copy(info)
    print(pclip_paste())

if __name__ == "__main__":
    test()

