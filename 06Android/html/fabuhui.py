#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : fabuhui.py
# @Time    : 2021/2/27 17:57
# @Author  : Merle
# @Site    : 
"""

"""
import HTMLTestRunner
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://127.0.0.1:8000/'

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('inputUsername').send_keys('admin')
        driver.find_element_by_id('inputPassword').send_keys('admin123456')
        driver.find_element_by_xpath('/html/body/div/form/button').click()
        time.sleep(1)

    def closeDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 获取TestSuite的实例对象
    suite.addTest(LoginTestCase("test_login"))
    # 把测试用例添加到测试容器中
    # now = strftime("%Y-%m-%M-%H_%M_%S", localtime(time()))
    # 获取当前时间
    filename = "test.html"
    # 文件名
    fp = open(filename, "wb")
    # 以二进制的方式打开文件并写入结果
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="测试报告的标题",
        description="测试报告的详情")
    runner.run(suite)
    fp.close()
