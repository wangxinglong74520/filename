#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 03xiecheng.py
# @Time    : 2021/1/31 14:59
# @Author  : Merle
# @Site    : 
"""
协程
"""
import asyncio


async def request(url):
    print('正在请求的url', url)
    print('请求成功', url)
    return url

# async 修饰的函数,调用之后返回的一个协程对象
c = request('www.baidu.com')

# # 创建一个事假循环对象
# loop = asyncio.get_event_loop()
# # 将协程对象注册到loop中
# loop.run_until_complete(c)

# # task的使用
# loop = asyncio.get_event_loop()
# # 基于loop创建了一个task对象
# task = loop.create_task(c)
# # 运行任务
# loop.run_until_complete(task)
# print(task)

# # future的使用
# loop = asyncio.get_event_loop()
# # 基于loop创建了一个task对象
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)
def callbake_fun(task):
    # result 返回的就是对象中封装的协程对象对应函数的返回值
    print(task.result())

#  绑定回调
loop = asyncio.get_event_loop()

task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中  将任务对象传递给回调函数
task.add_done_callback(callbake_fun)
# 运行
loop.run_until_complete(task)







