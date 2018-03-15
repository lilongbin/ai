#! /usr/bin/env python
# coding: utf-8
# __metaclass__ = type
import os
import logging

class MyLogger(logging.Logger):
    def __init__(self, filename='log/test.log', cLevel=logging.INFO, fLevel=logging.WARNING):
        # super(MyLogger, self).__init__(filename)
        logging.Logger.__init__(self, filename)

        # 日志格式设置
        fmtHandler = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)s][%(levelname)s] %(message)s')

        # log终端输出流设置
        try:
            consoleHd = logging.StreamHandler()
            consoleHd.setLevel(cLevel)
            consoleHd.setFormatter(fmtHandler)
            self.addHandler(consoleHd)
        except Exception as reason:
            self.error("%s" % reason)

        # log文件设置
        try:
            os.makedirs(os.path.dirname(filename))
        except Exception as reason:
            pass
        try:
            fileHd = logging.FileHandler(filename)
            fileHd.setLevel(fLevel)
            fileHd.setFormatter(fmtHandler)
            self.addHandler(fileHd)
        except Exception as reason:
            self.error("%s" % reason)            

        return
        # 设置回滚日志,每个日志最大10M,最多备份5个日志
        try:
            rtfHandler = logging.BaseRotatingHandler(
                            filename, maxBytes=10*1024*1024, backupCount=5)
        except Exception as reason:
            self.error("%s" % reason)
        else:
            self.addHandler(rtfHandler)

def main():
    logfile1 = 'log/test1.log'
    log = MyLogger(logfile1)
    log.debug("debug msg")
    log.info("info msg")
    log.warning("warning msg")
    log.error("error msg")
    log.critical("critical msg")

    logfile2 = 'log/test2.log'
    log = MyLogger(logfile2)
    log.debug("debug msg")
    log.info("info msg")
    log.warning("warning msg")
    log.error("error msg")
    log.critical("critical msg")

if __name__ == '__main__':
    main()


