import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.baid.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=8']

    rules = (
        # 规则解释器
        # 获取多个网页
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
        # 获取子网页的内容
        Rule(LinkExtractor(allow=r''),callback='parse_detail')
    )

    def parse_item(self, response):
        # 解析标题和id
        print(response)

    def parse_detail(self,response):
        pass