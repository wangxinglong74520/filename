#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02_selenium_zhaopin.py
# @Time    : 2020/12/16 21:53
# @Author  : Merle
# @Site    : 
"""

"""
import re
import json
import time

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from utils.header import get_ua
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import json

headers = {
    'User-Agent': get_ua()
}

chrome = Chrome()


def get_allcity():
    url = 'https://www.zhaopin.com/citymap'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        html = resp.text
        s = re.search(r'<script>__INITIAL_STATE__=(.*?)</script>', html)
        json_data = s.groups()[0]
        data = json.loads(json_data)
        cityMapList = data['cityList']['cityMapList']
        for letter, citys in cityMapList.items():
            print(f'----{letter}----')
            for city in citys:
                # 生成器
                yield city


def get_city_jobs(url, name):
    chrome.get(url)  # 打开城市信息
    # 查找警告信息的button
    # chrome.find_element_by_css_selector('').click()
    # 根据class_name 查询WebElement
    input_search: WebElement = chrome.find_element_by_class_name('zp-search__input')
    input_search.send_keys('Python')
    # 点击查找
    chrome.find_element_by_class_name('zp-search__btn--blue').click()
    time.sleep(0.5)
    # 当前浏览器打开第二个窗口
    v2 = chrome.window_handles[2]
    chrome.switch_to.window(v2)
    # 滚动
    chrome.execute_script('var q = document.documentElement.scrollTop=5000')
    time.sleep(0.2)
    chrome.execute_script('var q = document.documentElement.scrollTop=10000')
    # 等待 class_name 为:'contentpile__content'div元素的出现
    ui.WebDriverWait(chrome, 60).until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'contentpile__content'))
        ,'插查的元素一直没有出现'
    )
    # 判断是否有数据   class_name 为:'contentpile__jobcontent'
    nocontent = chrome.find_element_by_class_name('contentpile__jobcontent')
    if not nocontent:
        print('当前城市不存在:', name)
    else:
        # 提取岗位结果
        divs = chrome.find_elements_by_class_name('contentpile__content__wrapper clearfix')
        for div in divs:
            job_info_url = div.find_element(By.XPATH,'.//a/@href')
            print(job_info_url)

if __name__ == '__main__':
    query_citys = ('北京','西安','深圳')
    for city in get_allcity():
        # 保存城市信息
        # 请求城市的python岗位
        if city['name'] in query_citys:
            get_city_jobs('https:' + city['url'], city['name'])
            time.sleep(5)
