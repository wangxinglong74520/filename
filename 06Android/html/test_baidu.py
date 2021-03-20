#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : test_baidu.py.py
# @Time    : 2021/2/27 17:33
# @Author  : Merle
# @Site    : 
"""

"""

from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(15)

    def test_serchChina(self):
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
        unittest.main()
