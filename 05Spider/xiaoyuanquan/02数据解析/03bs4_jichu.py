#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 03bs4_jichu.py
# @Time    : 2021/1/24 21:53
# @Author  : Merle
# @Site    : 
"""
bs4解析基础
爬取三国演义所有内容
"""
import requests
from utils.header import get_ua
from bs4 import BeautifulSoup
import json

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url, headers=headers)
    page_text.encoding = 'utf-8'
    page_text = page_text.text
    # 数据解析
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节标题
    lo_list = soup.select('.book-mulu > ul > li')
    fp = open('case/sanguo.txt', 'w', encoding='utf-8')
    for li in lo_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        # 解析详情页的内容
        next_url = requests.get(url=detail_url, headers=headers)
        next_url.encoding = 'utf-8'
        next_url = next_url.text
        # 解析出详情页中的内容
        detail_soup = BeautifulSoup(next_url, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到章节的内容
        content = div_tag.text
        fp.write(title + ":" + content + '\n')
        print(title, "爬取成功!!")
