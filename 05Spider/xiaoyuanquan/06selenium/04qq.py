#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 04qq.py
# @Time    : 2021/1/31 17:44
# @Author  : Merle
# @Site    : 
"""
登录qq空间
"""
from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get('https://qzone.qq.com/')
# 切换
chrome.switch_to.frame('login_frame')
chrome.find_element_by_id('switcher_plogin').click()
chrome.find_element_by_id('u').send_keys('1544798456')
sleep(1)
chrome.find_element_by_id('p').send_keys('admin123')
sleep(2)
chrome.find_element_by_id('login_button').click()
sleep(2)
chrome.quit()