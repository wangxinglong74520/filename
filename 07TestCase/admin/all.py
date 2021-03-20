#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : all.py
# @Time    : 2021/2/28 18:00
# @Author  : Merle
# @Site    : 
"""

"""
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tescase = unittest.defaultTestLoader.discover(os.getcwd(), pattern='*.py')
    suite.addTests(tescase)
    nowtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    fp = open(nowtime + '_report.html', 'wb')
    runner = HTMLTestRunner(stream=fp, verbosity=2,
                            title='自动化', description='登录')
    runner.run(suite)
