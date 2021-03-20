#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : meinv.py
# @Time    : 2020/12/6 21:02
# @Author  : Merle
# @Site    : 
"""
爬取美女网
-requests
-bs4
-csv储存
- 扩展 携程 asyncio
"""
import json

from bs4 import BeautifulSoup, Tag
from utils.header import get_ua
import requests
import time

headers = {
    'User-Agent': get_ua()
}


def get(url):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        parse(resp.text)


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
    itempipeline(item)
    # 加载下一页
    post('http://www.meinv.hk/wp-admin/admin-ajax.php')


page = 2


def post(url):
    print('下一页url:', url)
    time.sleep(1)
    global page
    resp = requests.post(url, data={
        "total": 27,
        "action": "fa_load_postlist",
        "paged": page,
        "category": 28,
        "wowDelay": "0.3s"
    }, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        if not resp.text == "":
            ret = json.loads(resp.text)
            page += 1
            parse(ret['postlist'])


def itempipeline(item):
    print(item)


if __name__ == '__main__':
    start_url = 'http://www.meinv.hk/?cat=28'
    get(start_url)
