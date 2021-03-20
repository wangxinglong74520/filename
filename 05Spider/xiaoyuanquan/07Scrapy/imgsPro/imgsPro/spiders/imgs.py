import scrapy
from imgsPro.items import ImgsproItem

class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    # allowed_domains = ['ww.xx.com']
    start_urls = ['https://sc.chinaz.com/tupian/index.html']

    def parse(self, response):
        divs = response.xpath('//div[@id="container"]/div')
        item = ImgsproItem()
        for div in divs:
            src = 'https:'+div.xpath('./div/a/img/@src2').get()
            item['src'] = src
            yield item