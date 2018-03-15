#! /usr/bin/env python
# coding=utf-8

from selenium import webdriver
import time

try: input = raw_input
except: pass

def test(url=''):
    url = 'http://xxx'
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    
    browser.find_element_by_id('uid').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_name('Submit').click()
    time.sleep(2)

if __name__ == '__main__':
    test()

