#! /usr/bin/env python
# coding=utf-8

import getpass
username = raw_input('username: ')
password = getpass.getpass('password: ')
print('%s %s' % (username, password))

