# -*- coding: utf-8 -*-
"""
@FileName: echo_example_client
@Time: 2020/5/11 11:18
@Author: zhaojm

Module Description

"""


#!/usr/bin/env python

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        data = await websocket.recv()
        print(data)

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))