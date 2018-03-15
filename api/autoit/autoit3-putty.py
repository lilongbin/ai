#! /usr/bin/env python2
# coding=utf-8

import autoit
import time

putty = r'C:\Program Files (x86)\PuTTY\putty.exe'
host_ip = '10.171.59.99'
host_port = '22'
username = 'longbin'
password = '***'

autoit.run(putty)
time.sleep(2)
autoit.win_activate("PuTTY Configuration")
autoit.send("{DEL}"*15)
autoit.send(host_ip,1)
autoit.send('{TAB}')
autoit.send('{DEL}'*5)
autoit.send(host_port)

time.sleep(2)
autoit.control_click("PuTTY Configuration","&Open")
time.sleep(2)
title = autoit.win_get_title(host_ip)
print('title: %s' % title)

autoit.win_activate(title)
autoit.send(username + '{ENTER}')
time.sleep(5)
autoit.send(password + '{ENTER}')
autoit.send('{ENTER}'*2)
