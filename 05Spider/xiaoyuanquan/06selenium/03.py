#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 03.py
# @Time    : 2021/1/31 17:25
# @Author  : Merle
# @Site    : 
"""
iframe
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

chrome = webdriver.Chrome()
# 打开浏览器
chrome.get()
# 如果定位标签在iframe中,则必须先对iframe进行定位
chrome.switch_to.frame('标签名')  # 切换浏览器标签定位的作用域

# 动作链
action = ActionChains(chrome)
# 点击长按指定的标签
action.click_and_hold('标签')
# move_by_offset(x,y) x向水平方向拖动,y竖直    perform()立即执行动作链操作
action.move_by_offset(17,0).perform()
# 释放动作链
action.release()

# 打印浏览器文本信息
a = chrome.page_source


