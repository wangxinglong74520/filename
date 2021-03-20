#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01_chrome_headless.py
# @Time    : 2020/12/20 16:03
# @Author  : Merle
# @Site    : 
"""
配置chrome的无头选项
爬取百度贴吧-python
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def parse_data(flag=False):
    # 向下滚动1000
    chrome.execute_script('var q = document.documentElement.scrollTop=5000')
    # 查找搜索结果
    posts = chrome.find_elements(By.CLASS_NAME, 's_post')
    if flag:
        # 第一页去掉第一个
        posts = posts[1:]
    for post in posts:
        # a = post.find_element(By.XPATH, '//span[1]/a')
        a = post.find_element(By.CSS_SELECTOR, '.p_title a')
        url = a.get_attribute('href')  # 获取url
        title = a.text
        print(url, title)
    time.sleep(3)
    # 查找下一页
    # 网页中的大于号 > 使用&gt;
    chrome.find_element(By.LINK_TEXT, '下一页>').click()
    parse_data()


if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # options.binary_location = ''  # 配置浏览器驱动

    chrome = Chrome(options=options)
    # chrome = Chrome()
    # 启动1
    chrome.get('https://tieba.baidu.com/index.html')
    # 最大化浏览器
    chrome.maximize_window()
    # 查找搜索框的元素
    chrome.find_element(By.ID, 'wd1').send_keys('Python')
    # 点击搜索按钮
    chrome.find_element(By.XPATH, '//form[@id="tb_header_search_form"]/span[2]').click()

    time.sleep(1)
    # 解析数据
    parse_data(True)  # true 第一次对搜索的数据去掉第一项(用户信息)

    # 截屏保存图片
    chrome.save_screenshot('tieba.png')
    # chrome.quit()  # 退出
