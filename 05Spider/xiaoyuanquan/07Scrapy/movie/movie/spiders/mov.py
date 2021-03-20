import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from movie.items import MovieItem

class MovSpider(CrawlSpider):
    name = 'mov'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.4567kan.com/index.php/vod/show/id/1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/id/1/page/\d+\.html'), callback='parse_item', follow=False),
    )
    # 创建redis对象
    conn = Redis(host='192.168.17.130',port=6379)
    def parse_item(self, response):
        lis = response.xpath('//ul[@class="stui-vodlist clearfix"]/li')
        for li in lis:
            movie_url = 'http://www.4567kan.com' + li.xpath('./div/a/@href').get()
            movie_name = li.xpath('./div/a/@title').get()
            # 将获取的url存入redis中
            ex = self.conn.sadd('urls',movie_url)
            if ex == 1:  # redis 数据库和set相似  不存在为1,存在为0
                print(f'{movie_name}电影没有被爬取过')
                yield scrapy.Request(url=movie_url,callback=self.parse_detail)

    def parse_detail(self,response):
        # 解析详情页中的电影类型,进行持久化存储
        item = MovieItem()
        item['name'] = response.xpath('//div[@class="stui-content__detail"]/h1/text()').get()
        desc = response.xpath('//span[@class="detail-content"]/text()').get()
        desc = ''.join(desc)
        item['desc'] = desc
