#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : ecshop_login.py
# @Time    : 2021/2/28 12:33
# @Author  : Merle
# @Site    : 
"""

"""
import os
import unittest


class EeshopLogin(unittest.TestCase):

    # 测试用例
    def test01_baili(self):
        print('测试打印')

    # 测试用例
    def test02_weiwei(self):
        print('weiwei')


if __name__ == '__main__':
    # print('-------')
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest('test01_baili')
    # testcase = [EeshopLogin('test01_baili'),EeshopLogin('test02_weiwei')]
    testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern='*.py')
    suite.addTests(testcase)
    unittest.main(defaultTest='suite')  #  运行
    # unittest.TextTestRunner().run(suite)  # 运行
