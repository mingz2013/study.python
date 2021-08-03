# -*- coding: utf-8 -*-
"""
@FileName: test_async_await_3
@Time: 2020/5/12 11:20
@Author: zhaojm

Module Description

"""

import asyncio

async def double(x):
    r = x * 2
    print(r)
    return r

coroutine = double(6)

print(type(coroutine))  # <class 'coroutine'>

# coroutine.send(1)


loop = asyncio.get_event_loop()

loop.run_until_complete(coroutine)

# loop.close()

print("-" * 100)


async def sum_inter(n):
    print('sum', n, "+",  1)
    await asyncio.sleep(1)
    return n + 1


async def sum(n):
    r = await sum_inter(n)
    print(r)
    return r

coroutine = sum(1)

loop.run_until_complete(coroutine)

tasks = asyncio.wait([
    sum(10),
    sum(133)
])

print(type(tasks)) # <class 'coroutine'>

loop.run_until_complete(tasks)
# loop.close()




task = loop.create_task(sum(1000))
print(type(task)) # <class '_asyncio.Task'>


loop.run_until_complete(task)