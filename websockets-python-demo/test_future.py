# -*- coding: utf-8 -*-
"""
@FileName: test_future
@Time: 2020/5/12 11:46
@Author: zhaojm

Module Description

"""


import asyncio

future = asyncio.Future()

print(type(future)) # <class '_asyncio.Future'>

async def one():
    await asyncio.sleep(2)
    future.set_result(1)

async def two():
    data = await future
    print(data)


loop = asyncio.get_event_loop()


tasks = asyncio.wait([
    one(),
    two()
])


print(type(tasks)) # <class 'coroutine'>

loop.run_until_complete(tasks)

loop.close()
