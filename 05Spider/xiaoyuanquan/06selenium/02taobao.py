#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02taobao.py
# @Time    : 2021/1/31 17:04
# @Author  : Merle
# @Site    : 
"""

"""
from selenium import webdriver
from time import sleep
chrome = webdriver.Chrome()
chrome.get('https://www.taobao.com/')
# 标签定位
search_input = chrome.find_element_by_id('q')
# 标签交互
search_input.send_keys('iphone')
# 执行一组js程序
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# 点击搜索按钮
chrome.find_element_by_css_selector('.btn-search').click()

chrome.get('https://www.baidu.com')
sleep(2)
# 返回
chrome.back()
sleep(2)
# 前进
chrome.forward()


sleep(4)
#
chrome.quit()



