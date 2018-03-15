#! /usr/bin/env python
# coding=utf-8
# /usr/lib/totem/plugins/pythonconsole/totem_ff.py

# put following sentenses to pythonconsole.py of 
# class PythonConsolePlugin(totem.Plugin):
'''
	def fastforward_init(self, Console):
		pydir = "/usr/lib/totem/plugins/pythonconsole"
		fffile = "totem_ff.py"
		import os
		Console.eval("import os", False)
		if not os.path.isfile(os.path.join(pydir, fffile)): return
		Console.eval("OLD_DIR=os.getcwd()", False)
		Console.eval("os.chdir('%s')" % pydir, False)
		Console.eval("from totem_ff import *", False)
		Console.eval("os.chdir(OLD_DIR)", False)
		Console.eval("ff = FF(totem_object)", False)
		Console.eval("ff = ff.ff", False)
		Console.eval("print('ff(sec=5)')", False)
'''
# and add below sentenses to show_console func
'''
			self.fastforward_init(console)
'''

class FF():
	def __init__(self, obj):
		self.obj = obj
	def ff(self, sec=5):
		totem_object = self.obj
		get_current_time = totem_object.get_current_time
		seek_time        = totem_object.action_seek_time
		seek_relative    = totem_object.action_seek_relative
		def period():
			sec = get_current_time()//1000
			h=0;m=0;
			if sec // 3600: h = sec//3600; sec = sec%3600
			if sec // 60:   m = sec//60;   sec = sec%60
			print("%02d:%02d:%02d" % (h,m,sec))
		def FastForward(sec):
			#cur_time = get_current_time()
			#target_t = cur_time + int(sec)*1000
			#seek_time(target_t)
			seek_relative(int(sec)*1000)
			period()
		def FastBackward(sec):
			#cur_time = get_current_time()
			#if cur_time < int(sec): return
			#target_t = cur_time - int(sec)*1000
			#seek_time(target_t)
			seek_relative(-int(sec)*1000)
		sec = int(sec)
		if not -120<sec<120: sec=5
		totem_object.action_pause()
		if sec >= 0:
			FastForward(sec)
		else:
			FastBackward(-sec)
		totem_object.action_play()

