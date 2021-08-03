# -*- coding: utf-8 -*-
"""
@FileName: test_await
@Time: 2021/7/31 15:15
@Author: zhaojm

Module Description

"""
async def test():
    return 1



t = test()
print(type(t))

# t.send(1)


await t