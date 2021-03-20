#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : my_unit.py
# @Time    : 2021/2/28 16:35
# @Author  : Merle
# @Site    : 
"""

"""
import unittest


class MyUnit(unittest.TestCase):
    def setUp(self) -> None:
        print('方法开始')

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('类开始')
    #     pass

    def tearDown(self) -> None:
        print('方法结束')


    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('类结束')
    #     pass
