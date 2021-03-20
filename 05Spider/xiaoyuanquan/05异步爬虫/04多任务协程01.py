#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 04多任务协程01.py
# @Time    : 2021/1/31 15:18
# @Author  : Merle
# @Site    : 
"""多任务协程
"""
import asyncio
import time


async def request(url):
    print('正在下载', url)
    # 在异步协程中如果出现了同步模块相关代码,那么就无法实现异步
    # time.sleep(2)
    # 当早asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完成', url)


start = time.time()
urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.douban.com'
]

stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    # 注册到事件循环对象中
    stasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))

print(time.time() - start)
