# -*- coding: utf-8 -*-
"""
@FileName: echo_example_server
@Time: 2020/5/11 11:17
@Author: zhaojm

Module Description

"""


#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()