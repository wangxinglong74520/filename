import scrapy
from qiubai.items import QiubaiItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []
        for div in divs:
            # extract()
            author = div.xpath('.//div[@class="author clearfix"]/a[2]/h2/text()').get()
            content = div.xpath('.//div[@class="content"]/span//text()').extract()
            content = ''.join(content)
            print(author, content)

            item = QiubaiItem()
            item['author'] = author
            item['content'] = content

            yield item