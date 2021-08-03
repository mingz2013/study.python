# -*- coding: utf-8 -*-
"""
@FileName: test
@Time: 2020/5/11 14:32
@Author: zhaojm

Module Description

"""

import asyncio

import random

print('begin...file...')


async def guess_num():
    print('begin...hello...')
    num = random.randint(0, 10)
    while True:
        n = input("guess num ?")
        print('you guess num is ', n)
        n = int(n)
        if n < num:
            print('less than...')
            continue
        elif n > num:
            print('more than...')
            continue
        else:
            print('ok...success')
            break

    print('end...hello....')

print('file .....11111')

loop = asyncio.get_event_loop()
print('file .....22222')
loop.run_until_complete(guess_num())
print('file .....33333')
# loop.run_forever()
loop.close()
print("end...file....")
