#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 04_session.py
# @Time    : 2020/11/25 22:42
# @Author  : Merle
# @Site    : 
# ******************       *************
"""
610039018@qq.com
disen888
超级鹰
disen666
disen888
1.下载验证码的图片
2.图片验证码的打码
3.登录
4.获取个人的收藏信息
"""
import uuid

import requests
from lxml import etree
from utils.header import get_ua
from utils.chaojiying import rec_code

# 创建session
session = requests.session()  # 获取验证码接口和登录的接口必须在同一个session中


def download_code():
    resp = session.get('https://so.gushiwen.org/RandCode.ashx',
                       headers={'User-Agent': get_ua()})
    # 写入文件
    with open('code.png', 'wb') as f:
        f.write(resp.content)


def get_code_str():
    download_code()
    return rec_code('code.png')


def login():
    resp = session.post('https://so.gushiwen.org/user/login.aspx',
                        data={
                            'email': '1544798456@qq.com',
                            'pwd': 'admin123',
                            'code': get_code_str()
                        })
    if resp.status_code == 200:
        collect()
    else:
        print('-' * 30)
        print(resp.text)


def collect():
    resp = session.get('https://so.gushiwen.org/user/collect.aspx')
    parse(resp.text)

def parse(html):
    root = etree.HTML(html)  # 获取html的根元素
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')
    # print(divs)
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('.//p[1]//text()')  # 诗名
        item['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
        item['content'] = '<br>'.join(div.xpath('.//div[@class="contson"]/text()'))
        item['tags'] = ','.join(div.xpath('./div[last()]/a/text()'))
        print(item)

if __name__ == '__main__':
    login()
