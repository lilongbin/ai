#! /usr/bin/env python
# coding=utf-8
# redis-server redis.conf

import redis

def test():
    host = 'localhost'
    port = 6379
    # cnnpool = redis.ConnectionPool(host, port)
    # rdb = redis.Redis(connection_pool=cnnpool)
    rdb = redis.Redis(host, port)
    rdb.append('test', 'hello world')
    print(rdb.get('test'))

if __name__ == '__main__':
    test()
