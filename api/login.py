#! /usr/bin/env python
# coding=utf-8

import string
import random
import crypt
import getpass

try: input = raw_input
except: pass

def getsalt():
    '''generate a random 2_character salt'''
    chars = string.letters + string.digits
    return random.choice(chars) + random.choice(chars)

def cryptword():
    print('crypt password')
    raw_word = input('raw password: ')
    crypt_word = crypt.crypt(raw_word, getsalt())
    print('Please save crypt password: %s' % crypt_word)
    return crypt_word

#crypt_word = cryptword()
crypt_word = 'DH9zpYzRFRtLM'

def login(username, password):
    word = crypt.crypt(password, crypt_word[:2])
    return crypt_word == word

def test():
    username = input('username: ')
    password = getpass.getpass('password: ')
    if login(username, password):
        print('welcome to login!')
    else:
        print('username or password not correct!')

if __name__ == '__main__':
    test()

