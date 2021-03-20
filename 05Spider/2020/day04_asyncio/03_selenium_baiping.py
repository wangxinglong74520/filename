#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 03_selenium_baiping.py
# @Time    : 2020/12/17 21:40
# @Author  : Merle
# @Site    : 
"""

"""
import json
import time

from selenium.webdriver import Chrome
from urllib.parse import quote
import requests
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.common.by import By

chrome = Chrome()


def start(cityName):
    url = f'http://zhaopin.baidu.com/?city={quote(cityName)}'
    chrome.get(url)
    #  搜索
    query = chrome.find_element_by_css_selector('input[name="query"]')
    query.send_keys('Python')
    time.sleep(1)
    # 最大化浏览器
    chrome.maximize_window()
    # chrome.execute_script('var q=document.documentElement.scrollLeft=500')
    # 点击搜索
    chrome.find_element_by_css_selector('.search-btn>i').click()
    time.sleep(1)
    chrome.execute_script('var q=document.documentElement.scrollTop=500')
    # 等待出现class_name为listitem的div元素出现
    ui.WebDriverWait(chrome, 60).until(
        expected_conditions.visibility_of_all_elements_located((
            By.CLASS_NAME, 'listitem'
        )),
        'listitem的div元素没有出现'
    )
    # 连续向下滚动10次
    for i in range(11):
        chrome.execute_script('var q=document.documentElement.scrollTop=500')

    # 获取所有岗位信息
    items = chrome.find_elements(By.CSS_SELECTOR, '.listitem>a')
    items = items[1:]  # 第一个a标签是广告
    print(items)
    for item in items:
        # 过滤广告
        try:
            item.find_element(By.CLASS_NAME, 'adbar-item')
            continue
        except:
            pass
        data = item.find_element(By.TAG_NAME, 'div').get_attribute('data-click')
        info_url = json.loads(data)['url']  # 岗位的详情链接
        title = item.find_element(By.CLASS_NAME, 'title').text  # 岗位名称
        salary = item.find_element(By.CSS_SELECTOR, '.salaryarea span').text
        print(info_url,title,salary)


if __name__ == '__main__':
    start('西安')
