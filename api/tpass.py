#! /usr/bin/env python
# coding=utf-8

import sys
import tty
import termios

def getch():
    fd = sys.stdin.fileno() 
    old_settings = termios.tcgetattr(fd) 
    try:
        tty.setraw(fd) 
        ch = sys.stdin.read(1) 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
    return ch

def getpass(maskchar="*"):
    password = ""
    masklen = len(maskchar)
    while True:
        ch = getch()
        if ch == "\r" or ch == "\n":
            print('')
            break
        elif ch == "\b" or ord(ch) == 127: 
            if len(password) > 0: 
                sys.stdout.write("\b \b" * masklen) 
                password = password[:-1] 
        else: 
            if maskchar: 
                sys.stdout.write(maskchar) 
            password += ch
    return password

if __name__ == "__main__": 
    print("Enter password:"), 
    password = getpass("**") 
    print('you input: %s' % password)