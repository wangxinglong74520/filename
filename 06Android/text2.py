#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : text2.py
# @Time    : 2021/2/27 14:52
# @Author  : Merle
# @Site    : 
"""

"""

from multiprocessing import Pool
from threading import Thread

from multiprocessing import Process


def loop():
    while True:
        pass


if __name__ == '__main__':

    for i in range(3):
        t = Process(target=loop)
        t.start()

    while True:
        pass
