#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : shanxi2.py
# @Time    : 2021/1/6 22:15
# @Author  : Merle
# @Site    : 
"""

"""
import scrapy

from scrapy.http import FormRequest, Request


class ShanxiSpider(scrapy.Spider):
    name = 'shanxi2'
    allowed_domains = ['ccgp-shaanxi.gov.cn']

    def start_requests(self):
        self.url = 'http://www.ccgp-shaanxi.gov.cn/notice/list.do?noticetype=3&province=province'
        self.data = {
            'page.pageNum': '1'
        }
        self.MAX_PAGE = 1399
        yield FormRequest(self.url, formdata=self.data)

    def parse(self, response):
        trs = response.css('.list-box tbody tr')
        for tr in trs:
            item = {}
            item['id'] = tr.xpath('./td[1]/text()').get()
            item['area'] = tr.xpath('./td[2]/text()').get()
            item['title'] = tr.xpath('./td[3]/a/text()').get()
            item['url'] = tr.xpath('./td[3]/a/@href').get()
            item['date'] = tr.xpath('./td[4]/text()').get()

            yield item
        # 获取下一页
        if len(trs) >= 10:
            yield Request(response.request.url,
                          meta={'next_page': True}, dont_filter=True)
