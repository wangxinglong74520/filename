# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from utils.header import get_ua
import random


class MiddleproSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MiddleproDownloaderMiddleware:

    # 拦截请求
    def process_request(self, request, spider):
        headers = {'User-Agent': get_ua()}
        # UA 伪装
        request.headers['User-Agent'] = headers
        return None

    # 拦截所有的响应
    def process_response(self, request, response, spider):
        return response

    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        # 代理IP
        proxy_http = {
            '218.14.12.22:9999',
            '61.145.8.134:9999',
            '27.43.188.171:9999'
        }
        proxy_https = {
            '36.249.52.35:9999',
            '27.43.187.117:9999',
            '58.253.153.116:9999'

        }
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://' + random.choice(proxy_http)
        else:
            request.meta['proxy'] = 'http://' + random.choice(proxy_https)
        return request  # 将修正后的请求对象进行重新发送
