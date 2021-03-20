import scrapy


class ShiwenSpider(scrapy.Spider):
    name = 'shiwen'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://gushiwen.org/user/collect.aspx']

    def parse(self, response):
        print(response.text)
