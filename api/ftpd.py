#! /usr/bin/env python
# coding=utf-8

import os
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

try: input = raw_input
except: pass

def select_one(selections, default=''):
    if not selections: return None
    if default:
        for indx, choice in enumerate(selections):
            if default in choice:
                return choice
    user_choice = []
    while True:
        for indx, choice in enumerate(selections):
            print('%2d> %s' % (indx+1, choice[0]))
        print('%2d> %s' % (0, 'quit'))
        none_value = [None for tmp in choice]
        sys.stdout.write('Please select your target id: ')
        sys.stdout.flush()
        user_select = input().strip()
        if not user_select:
            user_choice = none_value
            break
        if user_select == '0':
            sys.exit()
        try:
            user_select = int(user_select)
            user_choice = selections[user_select-1]
        except Exception as reason:
            print('ERROR: Invalid number, please try again.')
            continue
        break
    return user_choice


choice = ['127.0.0.1', '2121', '1', '1']
host, port, username, password = choice

def ftpd():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()
    
    # Define a new user having full r/w permissions and a read-only# anonymous user
    authorizer.add_user(username, password, '.', perm='elradfmwM')
    authorizer.add_anonymous(os.getcwd())
    
    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer
    
    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."
    # Specify a masquerade address and the range of ports to use for
    # passive connections. Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)
    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = (host, port)
    server = FTPServer(address, handler)
    
    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5
    
    # start ftp server 
    server.serve_forever()

if __name__ == '__main__':
    # systemctl stop firewalld
    ftpd()
