#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : HtmlReport.py.py
# @Time    : 2021/2/27 17:42
# @Author  : Merle
# @Site    : 
"""

"""
import HTMLTestRunner
from time import strftime, localtime, time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(15)

    def test_searchChina(self):
        """百度搜索中国的测试用例"""
        self.driver.find_element_by_xpath(".//*[@id='kw']").send_keys("中国")
        self.driver.find_element_by_xpath(".//*[@id='su']").click()

        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(".//*[@id='1']/h3/a"))
        result = self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").text

        self.assertEqual(result, "中国_百度百科")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 获取TestSuite的实例对象
    suite.addTest(SearchTestCase("test_searchChina"))
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
