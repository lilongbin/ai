#! /usr/bin/env python2
# coding=utf-8

import autoit
import time

autoit.run("notepad.exe")
time.sleep(2)
autoit.win_activate(u"无标题 - 记事本")
autoit.send("{LSHIFT}")
time.sleep(2)
autoit.send("#Process finished with exit code 0.",1)
time.sleep(2)
autoit.win_close(u"无标题 - 记事本")
autoit.win_activate(u"记事本")
time.sleep(2)
autoit.control_click(u"记事本",u"保存(&S)")
time.sleep(2)
autoit.win_activate(u"另存为")
autoit.control_set_text(u"另存为","[CLASS:Edit; INSTANCE:1]","myTest.py")
time.sleep(2)
autoit.control_click(u"另存为",u"保存(&S)")
