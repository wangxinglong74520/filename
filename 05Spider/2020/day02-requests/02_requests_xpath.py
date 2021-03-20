#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02_requests_xpath.py
# @Time    : 2020/11/23 22:49
# @Author  : Merle
# @Site    : 
# ******************  基于request库作用实现网络请求 xpath     *************
from lxml import etree
import requests


class RequestError(Exception):
    """
    请求异常
    """
    pass


class ParseError(Exception):
    """解析异常"""
    pass


def get(url):
    resp = requests.get(url,
                        headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'},
                        proxies={'http': 'http://211.21.120.163:8080'},
                        )
    if resp.status_code == 200:
        parse(resp.text)
        print(resp.text)
        # print(resp.cookies)
    else:
        raise RequestError('请求失败!')


def parse(html):
    # 使用xpath解析
    root = etree.HTML(html)  # Element 元素对象
    divs = root.xpath('//dic[@class="li-itemmod"]')  # List[<>,<>] 可迭代对象
    print(divs)
    for div in divs:
        # 提取src的属性值
        cover_url = div.xpth('.//img/@src').extract()[0]  # list[]
        print(cover_url)
        # 获取名称
        title = div.xpath('.//h3/a/text()').extract()[0]
        print(title)


if __name__ == '__main__':
    get('https://shanghai.anjuke.com/community/?from=esf_list_navigation')
