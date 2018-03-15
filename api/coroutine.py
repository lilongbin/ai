#! /usr/bin/env python
# coding=utf-8

import sys
import time

'''
consumer函数是一个generator，把一个consumer传入produce后：
1.首先调用con.send(None)启动生成器；
2.然后，一旦生产了东西，通过con.send(n)切换到consumer执行；
3.consumer通过yield拿到消息，处理，又通过yield把结果传回；
4.produce拿到consumer处理的结果，继续生产下一条消息；
5.produce决定不生产了，通过con.close()关闭consumer，整个过程结束。
'''

def consumer():
    '''
    这个函数因为yield而变得画风特别不同
    1 yield相当于return
    2 相当于保存了当时运行的上下文
    3 相当于协程中让出调度权
    4 相当于具有上下文迭代器中的next()功能
    5 当next被调用时，相当于从当初保存的上下文位置开始继续执行，相当于协程中的得到调度权
    6 带yield的函数返回的是一个生成器对象，而这个生成器具有上述所有功能
    '''
    '''
    yield属于协程被调度出去1开辟内存保存当前上下文2函数return等待下次被唤醒继续执行并且可带信息(send就可)
    x.next()属于协程被调度进来，可以从上次yield暂停处继续执行
    x.send(param)类似next，不同的是可以带参数使得yield表达式能返回send传递的这个参数
    '''
    client = ''
    while True:
        s_generator = yield client
        if not s_generator:
            return
        print('[C] Consuming %s...' % s_generator)
        time.sleep(1)
        client = '200 OK'

def producer(con):
    if sys.version_info[0] == 2:
        con.next()
    else:
        con.__next__()
    s_generator = 0
    while s_generator < 5:
        s_generator += 1
        print('[P] Producing %s...' % s_generator)
        client = con.send(s_generator)
        print('[P] Consumer return: %s\n' % client)
    con.close()

if __name__ == '__main__':
    c = consumer()
    producer(c)
