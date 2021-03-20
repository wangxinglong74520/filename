#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01.py
# @Time    : 2021/1/31 13:34
# @Author  : Merle
# @Site    : 
"""

"""
import time
from multiprocessing.dummy import Pool

# 使用线程池方式执行
start_time = time.time()


def get_page(str):
    print('正常下载:', str)
    time.sleep(2)
    print('下载成功:', str)


name_list = ['xiaozi', 'aa', 'bb', 'cc']
# 实例化一个线程池对象
pool = Pool(4)
# 将列表中买一个列表元素传递给get_page进行处理
pool.map(get_page, name_list)
end_time = time.time()
print(end_time-start_time)