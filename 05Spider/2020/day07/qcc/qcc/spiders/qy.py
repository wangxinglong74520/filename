import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QySpider(CrawlSpider):
    name = 'qy'
    allowed_domains = ['qcc.com']
    start_urls = ['https://www.qcc.com/g_AH']

    rules = (
        Rule(LinkExtractor(allow=r'g_[A-Z]{2,}\.html',  # 允许提取的
                           deny=r'g_[A-Z]{2.}_\d+\.html',  # 不允许提取得
                           ),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css='.pagination'),
             'parse_item', follow=True)
    )

    def parse_item(self, response):

        trs = response.css('.m_srchList tr')
        for tr in trs:
            item = {}
            item['cover'] = tr.xpath('./td[1]/img/@src').get()
            item['name'] = tr.xpath('./td[2]/a/text()').get()
            yield item
