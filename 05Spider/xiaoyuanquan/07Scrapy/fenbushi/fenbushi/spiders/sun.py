import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy_redis

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://pic.netbian.com/4kmeinv/index.html']
    redis_key = 'fbs'
    rules = (
        Rule(LinkExtractor(allow=r'<a href="/4kmeinv/index_\d+\.html">'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)

