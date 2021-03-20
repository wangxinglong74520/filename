#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01_asyncio_meinv.py
# @Time    : 2020/12/14 22:30
# @Author  : Merle
# @Site    : 
"""

"""
import asyncio
import csv
import os
import sys

import requests
from bs4 import BeautifulSoup, Tag
from utils.header import get_ua
import json

headers = {
    'User-Agent': get_ua()
}


@asyncio.coroutine
def get(url):
    # 协程
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        yield from parse(resp.text)


@asyncio.coroutine
def post(url, page=2):
    print('---下一页---', url, page)
    yield from asyncio.sleep(0.5)
    resp = requests.post(url, data={
        'total': 14,
        'action': 'fa_load_postlist',
        'paged': page,
        'category': 28,
        'wowDelay': '0.3s'
    }, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        ret = json.loads(resp.text)
        print(ret)
        if ret['code'] == 200:
            yield from parse(ret['postlist'])
            yield from post(url, page + 1)


@asyncio.coroutine
def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    content_boxs = soup.select('.content-box')
    item = {}
    for content_box in content_boxs:
        img: Tag = content_box.find('img')
        item['name'] = img.attrs.get('alt')
        item['cover'] = img.attrs.get('src')
        info = content_box.select('.posts-text')[0].get_text()
        try:
            _, birthday, city = [txt.strip() for txt in info.split('/')]
            item['birthday'], item['city'] = birthday[2:].strip(), city[2:].strip()
        except:
            item['birthday'], item['city'] = ('', '')

    yield from itempipeline(item)
    # 加载下一页
    # post('http://www.meinv.hk/wp-admin/admin-ajax.php')


@asyncio.coroutine
def itempipeline(item):
    yield from save_csv(item)
    yield from save_img(item['cover'], item['name'])


@asyncio.coroutine
def save_csv(item):
    has_header = os.path.exists(csv_filepath)
    with open(csv_filepath, 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=item.keys())
        if not has_header:
            writer.writeheader()
        writer.writerow(item)


@asyncio.coroutine
def save_img(url, name):
    resp = requests.get(url,headers=headers)
    if resp.status_code == 200:
        type_ = resp.headers['content-type']
        ext_name = 'png' if type_.startswith('image/png') else '.jpg'
        with open(f'images/{name} {ext_name}', 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    csv_filepath = 'meinv.csv'
    # sys.argv是命令行参数列表, 0位置是脚本名, 1是脚本名后的第一个参数
    # csv_filepath = sys.argv[1]  #
    loop = asyncio.get_event_loop()
    # 起始协程任务是单个的
    # loop.run_until_complete(get())
    # 起始多个协程
    loop.run_until_complete(asyncio.wait(
        (get('http://www.meinv.hk/?cat=28'),
         post('http://www.meinv.hk/wp-admin/admin-ajax.php'))
    ))
