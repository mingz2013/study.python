# -*- coding: utf-8 -*-
"""
@FileName: test_object
@Time: 2020/11/12 20:30
@Author: zhaojm

Module Description

"""

import time


def test_get_value():
    class A(object):
        def __init__(self):
            self.a = 1

    b = dict()
    b['a'] = 1

    count = 100000000

    a = A()

    t1 = time.time()

    for i in range(count):
        a.a

    t2 = time.time()

    for i in range(count):
        b['a']

    t3 = time.time()

    print(t2 - t1)
    print(t3 - t2)

    # 0.08032417297363281
    # 1.103281021118164


def test_create():
    class A(object):
        def __init__(self):
            self.a = 1

    count = 100000000

    t1 = time.time()

    for i in range(count):
        A()

    t2 = time.time()

    for i in range(count):
        dict()

    t3 = time.time()

    print(t2 - t1)
    print(t3 - t2)


test_create()
# test_get_value()
