# -*- coding: utf-8 -*-
"""
@FileName: test_new
@Time: 2020/11/2 18:48
@Author: zhaojm

Module Description

"""

import functools
import time


def traceMethod(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('traceMethod', func.__name__, float('%.5f' % (end - before)))
        return result

    return wrapper


class TraceMethodCalls(type):

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        class_name, supers, attrs = args
        for name, attr in attrs.items():
            if callable(attr):
                attrs[name] = traceMethod(attr)

        return type.__new__(cls, *args, **kwargs)


class A(object, metaclass=TraceMethodCalls):
    pass


def mark(func):
    setattr(func, 'hahahaha', 'hahahaha')
    return func


class AA(A):
    # def __new__(cls, *args, **kwargs):
    #     print(args, kwargs)
    #     pass

    @mark
    def f(self):
        time.sleep(0.1)
        pass


aa = AA()
aa.f()
print(aa.f.__dict__, aa.f.hahahaha, aa.f.__name__)
