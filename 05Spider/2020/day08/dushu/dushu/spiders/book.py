import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['dushu.com']
    start_urls = ['https://www.dushu.com/book/']

    rules = (
        # 所有图书分类的连接 css匹配
        Rule(LinkExtractor(restrict_css='.sub-catalog'),
             follow=False),

        Rule(LinkExtractor('/book/\d+?_\d+?\.html'),  # 下一页的url
             follow=True),
        # 图书详情信息 正则匹配
        Rule(LinkExtractor('/book/\d+/'), 'parse_item', follow=False)
    )

    def parse_item(self, response):
        item = {}
        item['name'] = response.css('h1::text').get()
        # 使用ImagesPipeline下载图片时,需要使用Image_urls字段,
        # 是迭代的list/tuple类型
        # item['image_urls'] = response.css('.pic img::attr("src")').extract()
        item['cover'] = response.css('.pic img::attr("src")').get()
        # item['images'] = []  # 下载图片之后,保存本地的文件位置
        item['price'] = response.css('.num::text').get()

        table = response.css('#ctl00_c1_bookleft table')
        item['author'] = table.xpath('.//tr[1]/td[2]/text()').get()
        item['publisher'] = table.xpath('.//tr[2]/td[2]/a/text()').get()

        table = response.css('.book-details>table')
        item['isbn'] = table.xpath('.//tr[1]/td[2]/text()').get()
        item['publish_date'] = table.xpath('.//tr[1]/td[4]/text()').get()
        item['pages'] = table.xpath('.//tr[2]/td[4]/text()').get()
        yield item
'scrapy genspider shanxi http://www.ccgp-shaanxi.gov.cn/notice/list.do?noticetype=3&province=province'