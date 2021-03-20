#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 05wutou.py
# @Time    : 2021/1/31 17:53
# @Author  : Merle
# @Site    : 
"""
无头浏览器
"""
from selenium import webdriver
# 无可视化
from selenium.webdriver.chrome.options import Options
# 规避检查
from selenium.webdriver import ChromeOptions

# 无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 规避检查
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

chrome = webdriver.Chrome(chrome_options=chrome_options,options=option)

chrome.get('https://www.baidu.com')
a = chrome.page_source
print(a)
chrome.quit()
