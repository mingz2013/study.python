# -*- coding: utf-8 -*-
"""
@FileName: basic_example_client
@Time: 2020/5/11 11:01
@Author: zhaojm

Module Description

"""


#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    print("hello....")
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")
    print("end hello....")

asyncio.get_event_loop().run_until_complete(hello())

print("end...")