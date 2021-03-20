#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02_requests_gushiwen.py
# @Time    : 2020/11/23 23:38
# @Author  : Merle
# @Site    : 
# ******************       *************
import os
import time

import requests
import uuid as uuid
from lxml import etree
from utils import header
from dao import Connection
from csv import DictWriter
import ssl

requests.packages.urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='admin123',
    db='stu',
    port=3306,
    charset='utf8'
)
cur = conn.cursor()
cur.execute('use stu')
base_url = 'https://www.gushiwen.org'
def itempipline(item):
    """保存数据"""
    print(item)
    # 字符串:id,name,author,content,tags
    # values 占位符字符串:%(id)s,%(name)s,%(author)s,%(content)s,%(tags)s,
    sql = 'insert into dushuwang(%s) values(%s)'
    fields = ','.join(item.keys())
    value_placeholds = ','.join(['%%(%s)s' % key for key in item])
    with cur as c:
        c.execute(sql % (fields,value_placeholds),item)
        cur.close()
#
# csv_file = open('dushuwang.csv', 'a')
has_header = os.path.exists('dushuwang.csv')  # 是否是第一次写入csv的头
header_fields = ('id', 'name', 'author', 'content', 'tags')


def itempipeline4csv(item):
    with open('dushuwang.csv', 'a') as f:
        global has_header
        write = DictWriter(f, header_fields)
        if not has_header:
            write.writeheader()  # 写入第一行标题行
            has_header = True
        write.writerow(item)

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
        itempipeline4csv(item)
        itempipline(item)
        # 获取下一页的链接
        # next_url = base_url+root.xpath('//a[@id="amore"]/@href')[0]
        # # url_l =root.xpath('//a[@id="amore"]/@href')[0]
        # print(next_url)
        # # 间隔0.5秒
        # time.sleep(0.5)
        # # 发起下一页的请求
        # get(next_url)


def get(url):
    resp = requests.get(url,
                        verify=False,
                        headers={'User-Agent': header.get_ua()})
    if resp.status_code == 200:
        # print(resp.text)  # 240099
        parse(resp.text)
    else:
        raise Exception('请求失败')


if __name__ == '__main__':
    get('https://www.gushiwen.cn/default_2.aspx')
