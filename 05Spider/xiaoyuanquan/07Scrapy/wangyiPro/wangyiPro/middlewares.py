# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep


class WangyiproSpiderMiddleware:
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


class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):

        return None

    # 该方法拦截对应的响应对象
    def process_response(self, request, response, spider):  # spider 爬虫对象
        bro = spider.bro  # 获取在爬虫类中定义的浏览器对象
        # 挑选指定的响应对象进行篡改
        # 通过url 指定的request
        # 通过request指定response
        if request.url in spider.models_urls:
            bro.get(request.url)  # 对每个模块的url进行请求
            # response  # 板块对应的响应对象
            # 实例化一个新的响应对象
            sleep(2)
            page_text = bro.page_source  # 包含了动态加载的新闻数据
            new_request = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)

            return new_request
        else:
            # response  # 其他请求对应的响应对象
            return response

    def process_exception(self, request, exception, spider):
        pass
