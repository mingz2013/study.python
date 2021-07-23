# -*- coding: utf-8 -*-
"""
@FileName: demo_say_after
@Time: 2020/5/29 14:28
@Author: zhaojm

Module Description

"""

import asyncio
import time


async def say_after(delay, what):
    print("say_after <<", delay, what)
    await asyncio.sleep(delay)
    print("say_after >>", what)


async def main():
    """

    started at 14:31:06
    hello 1
    hello 3
    hello 2
    finished at 14:31:12

    """
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello 1')  # 阻塞
    await say_after(3, 'hello 3')  # 阻塞
    await say_after(2, 'hello 2')  # 阻塞

    print(f"finished at {time.strftime('%X')}")


async def main2():
    """

    started at 14:34:58
    hello 1
    hello 2
    hello 3
    finished at 14:35:01

    """
    # 创建了任务就会并发的执行，而不需要await，
    # 如果没有await，task没有执行程序完就会over, 无法保证task一定会执行完成

    task1 = asyncio.create_task(say_after(1, 'hello 1'))
    task2 = asyncio.create_task(say_after(2, 'hello 2'))
    task3 = asyncio.create_task(say_after(3, 'hello 3'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 3 seconds.)
    # await task1
    # await task3
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    # asyncio.run(main())
    # asyncio.run(main2())
    asyncio.get_event_loop().run_until_complete(main2())
    asyncio.get_event_loop().run_forever()
