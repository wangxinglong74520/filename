#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 03_tasks.py
# @Time    : 2020/12/6 19:29
# @Author  : Merle
# @Site    : 
# ****************** 基于进程+线程实现多任务爬虫程序      *************
import uuid
from multiprocessing import Queue, Process
from threading import Thread
from queue import Queue as TQueue

from utils.header import get_ua

import requests
from lxml import etree

headers = {
    'User-Agent': get_ua()
}


class DownloadThread(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.content = None

    def run(self):
        # 下载
        print('开始下载', self.url)
        resp = requests.get(self.url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            self.content = resp.text
        print('下载完成', self.url)

    def get_content(self):
        return self.content


class DownloadProcess(Process):
    """下载进程"""

    def __init__(self, url_q, html_q):
        self.url_q: Queue = url_q
        self.html_q = html_q
        super().__init__()

    def run(self):
        while True:
            try:
                url = self.url_q.get(timeout=30)
                # 启动子线程下载任务
                t = DownloadThread(url)
                t.start()
                t.join()
                #  获取下载数据
                html = t.get_content()
                # 将数据压入到解析队列中
                self.html_q.put((url, html))

            except:
                break
        print('下载进程 over')


class ParseThead(Thread):
    def __init__(self, html, url_q, parent_url):
        self.html = html
        self.parent_url = parent_url
        self.url_q = url_q
        super(ParseThead, self).__init__()

    def run(self):
        root = etree.HTML(self.html)
        imgs = root.xpath('//div[contains(@class,"picblock")]//img')

        for img in imgs:
            item = {}
            item['id'] = uuid.uuid4().hex
            item['name'] = img.xpath('./@alt')[0]
            try:
                item['cover'] = img.xpath('./@src2')[0]
            except:
                item['cover'] = img.xpath('./@src')[0]
            # 将item数据写入ES的索引库
            print(item)

        # 获取下一页的连接
        next_page = root.xpath('//a[@class="nextpage"]/@href')
        if next_page:
            next_url = self.parent_url + next_page[0]
            self.url_q.put(next_url)  # 将新的下载任务添加到下载队列中


class ParseProcess(Process):
    """解析进程"""

    def __init__(self, url_q, html_q):
        super(ParseProcess, self).__init__()
        self.url_q = url_q
        self.html_q: Queue = html_q

    def run(self):
        while True:
            try:
                # 读取解析任务
                url, html = self.html_q.get(timeout=60)
                print('开始解析:', url)
                parent_url = url[:url.rindex('/') + 1]
                # 启动解析线程
                ParseThead(html, self.url_q, parent_url).start()

            except:
                break
        print('解析进程结束')


if __name__ == '__main__':
    task1 = Queue()  # 下载任务队列
    task2 = Queue()  # 解析任务队列
    # 起始爬虫任务
    task1.put('http://sc.chinaz.com/tupian/shuaigetupian.html')

    p1 = DownloadProcess(task1, task2)
    p2 = ParseProcess(task1, task2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('----over----')
