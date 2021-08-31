#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2017 * Ltd. All rights reserved.
#   
#   File name   : install_test.py
#   Author      : longbin
#   Created date: 2017-10-22 01:11:33
#   Description : 
#
#================================================================

import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b = tf.constant(22)
print("")
print("Tensorflow result: %s" % sess.run(a+b))
print("Tensorflow install test OK")

