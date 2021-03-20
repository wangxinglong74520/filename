import scrapy
from bossPro.items import BossproItem


class BassSpider(scrapy.Spider):
    name = 'bass'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101020100&industry=&position=']

    def parse(self, response):
        lis = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in lis:
            item = BossproItem()
            job_name = li.xpath('.//div[@class="job-title"]/span/text()').get()
            price = li.xpath('//span[@class="red"]/text()').get()
            adders = li.xpath('.//span[@class="job-area"]/text()').get()
            detail_url = 'https://www.zhipin.com' + li.xpath('.//span[@class="job-name"]/@href').get()
            print(job_name,price,adders)
            print('123456')
            item['job_name'] = job_name
            # 对详情页发起请求
            yield scrapy.Request(detail_url, callback=self.parse_deatil, meta={'item': item})

    def parse_deatil(self, response):
        # 回调函数接受item
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div/text()')
        job_desc = ''.join(job_desc)
        print(job_desc)
        item['job_desc'] = job_desc
        print('12124124')

        yield item