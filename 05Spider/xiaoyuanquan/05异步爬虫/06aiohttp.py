#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 06aiohttp.py
# @Time    : 2021/1/31 16:31
# @Author  : Merle
# @Site    : 
"""

"""
import requests
import asyncio
import time
import aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # text() 返回字符串形式的响应数据
            # read() 返回的二进制形式的响应数据
            #  json() 返回的就是json对象
            # 注意:获取响应数据操作前一定要使用await进行手动挂起
            page_text = await resp.text()
            print(page_text)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('消耗时间', end - start)
