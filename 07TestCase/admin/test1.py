#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : test1.py
# @Time    : 2021/2/28 16:35
# @Author  : Merle
# @Site    : 
"""

"""
import time

from selenium import webdriver

from admin.my_unit import MyUnit


class Test1(MyUnit):
    def test_member(self):
        """用来登录的"""
        # deiver = webdriver.Chrome()
        # deiver.implicitly_wait(5)
        # deiver.get('http://127.0.0.1:8000')
        # deiver.find_element_by_id('inputUsername').send_keys('admin')
        # deiver.find_element_by_id('inputPassword').send_keys('admin123456')
        # time.sleep(1)
        # deiver.find_element_by_xpath('/html/body/div/form/button').click()
        # time.sleep(3)
        print('这是登录')
