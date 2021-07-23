# -*- coding: utf-8 -*-
"""
@FileName: demo_await_object
@Time: 2020/5/29 14:42
@Author: zhaojm

Module Description

"""

# 可等待对象分为三种，协程，任务，Future


import asyncio
import datetime


# 定义一个协程函数
async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # So it *won't run at all*.

    # 协程对象
    # a = nested()

    # 协程
    # Let's do it differently now and await it:
    print(await nested())  # Will print "42".


async def main2():
    # 当一个协程通过asyncio.create_task()等函数被打包为一个任务，该协程将自动排入日程准备立即运行：
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete.
    await task
    print(task.result())


async def main3():
    # Future 是一种特殊的低层级可等待对象，表示一个异步操作的最终结果。
    # 当一个Future对象被等待，这意味着协程将保持等待直到该Future对象在其他地方操作完毕。
    # 在asyncio中需要Future对象以便允许通过async/await使用基于回调的代码。
    # 通常情况下 没有必要 在应用层级的代码中创建Future对象。

    # Future对象有时会由库和某些asyncio API暴露给用户，用作可等待对象：

    # await function_that_returns_a_future_object()

    # this is also valid:
    # await asyncio.gather(
    #     function_that_returns_a_future_obejct(),
    #     some_python_coroutine()
    #     )
    pass


def main4():
    # 运行asyncio程序
    async def main():
        await asyncio.sleep(1)

    asyncio.run(main())


def main5():
    async def task():
        await asyncio.sleep(1)

    t = asyncio.create_task(task())


def main6():
    async def display_date():
        loop = asyncio.get_event_loop()
        end_time = loop.time() + 5.0
        while True:
            print(datetime.datetime.now())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)

    asyncio.run(display_date())


async def main7():
    async def factorial(name, number):
        f = 1
        for i in range(2, number + 1):
            print(f"Task {name}: Compute factorial({i})...")
            await asyncio.sleep(1)
            f *= i
        print(f"Task {name}: factorial({number}) = {f}")

    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


async def main8():
    try:
        await asyncio.wait_for(asyncio.sleep(100), timeout=1.0)
    except asyncio.TimeoutError:
        print("timeout!")


import asyncio
import sys


def main9():
    loop = asyncio.get_event_loop()
    loop.add_reader(
        sys.stdin.fileno(), lambda: print(sys.stdin.readline()))
    # loop.add_writer()
    # loop.connect_read_pipe()
    loop.run_forever()


if __name__ == '__main__':
    # asyncio.run(main())
    # asyncio.run(main2())
    # main6()
    # asyncio.run(main7())
    # asyncio.run(main8())
    main9()
