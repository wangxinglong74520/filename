#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01base.py
# @Time    : 2021/1/31 16:55
# @Author  : Merle
# @Site    : 
"""
selenium的使用
"""
import time
from selenium import webdriver
from lxml import etree

chrome = webdriver.Chrome()
chrome.get('http://scxk.nmpa.gov.cn:81/xk/')

# 获取浏览器当前页面的源码数据
page_text = chrome.page_source

# 解析数据
tree = etree.HTML(page_text)
lis = tree.xpath('//ul[@id="gzlist"]/li')
for li in lis:
    name = li.xpath('./dl/@title')[0]
    print(name)
time.sleep(5)
chrome.quit()























