# -*- coding: utf-8 -*-
"""
@FileName: test_async_await_2
@Time: 2020/5/12 11:11
@Author: zhaojm

Module Description

"""

import asyncio

print('file ........', 1)


async def task(n):
    print("task begin...", n)
    if n == 1:
        await asyncio.sleep(n)
        n -= 1
        print(n)
        return await task(n)
    elif n == 0:
        return n
    elif n > 1:
        print(n-1)
        return await task(n-1)


print('file ........', 2)

tasks = [
    task(100),
    # task(5),
    # task(4),
    # task(12),
    # task(2)
]

print('file ........', 3)

loop = asyncio.get_event_loop()
print('file ........', 4)

loop.run_until_complete(asyncio.wait(tasks))
print('file ........', 5)

loop.close()
print('file ........', 6)
