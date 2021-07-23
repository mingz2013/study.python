# -*- coding: utf-8 -*-
"""
@FileName: __init__
@Time: 2020/5/29 11:11
@Author: zhaojm

Module Description

"""

import asyncio
import datetime
import time

from app import demo
from app import log


def run():
    t1 = datetime.datetime.now()
    log.info("run <<....", time.time(), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    # asyncio.get_event_loop().run_until_complete(check_redis_key.main())
    asyncio.get_event_loop().run_until_complete(demo.main())

    t2 = datetime.datetime.now()
    log.info("run >>....", "begin time:", t1.strftime('%Y-%m-%d %H:%M:%S.%f'), "| end time:",
             t2.strftime('%Y-%m-%d %H:%M:%S.%f'))
    log.info("run >>....", "begin time:", t1, "| end time:", t2)
    log.info("run >>....", "days, seconds, total_seconds, microseconds:", (t2 - t1).days, (t2 - t1).seconds,
             (t2 - t1).total_seconds(), (t2 - t1).microseconds)
    log.info("run >>....", time.time(), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
