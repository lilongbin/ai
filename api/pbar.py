#! /usr/bin/env python
# coding=utf-8

import progressbar

class Pbar(object):
    def __init__(self, maxval=1):
        self.maxval = maxval
        self.pbar = progressbar.ProgressBar(maxval=self.maxval)
        self.pbar.start()
    def update(self, curval):
        if curval>=self.maxval:
            curval = self.maxval
        self.pbar.update(curval)
    def finish(self):
        self.pbar.finish()

def test():
    maxval = 10
    pbar = Pbar(maxval)
    import time
    for i in range(maxval):
        pbar.update(i+1)
        time.sleep(1)
    pbar.finish()

if __name__ == '__main__':
    test()
