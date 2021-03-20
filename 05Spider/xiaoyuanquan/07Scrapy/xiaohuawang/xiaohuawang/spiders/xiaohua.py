import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/tuku/']

    def parse(self, response):
        li_lists = response.xpath('//ul[@class="pbl "]/li')
        for li in li_lists:
            img_url = 'http://www.521609.com' + li.xpath('./a/img/@src').get()
            img_name = li.xpath('./a/p/text()').get()
            print(img_url, img_name)
