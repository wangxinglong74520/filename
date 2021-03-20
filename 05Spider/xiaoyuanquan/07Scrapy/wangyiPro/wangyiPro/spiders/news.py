import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['news.163.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储五个板块详情的url

    def __init__(self):
        self.bro = webdriver.Chrome()

    # 解析url
    def parse(self, response):
        lis = response.xpath('//div[@class="ns_area list"]/ul/li')
        alist = [4, 5, 7, 8, 9]
        for index in alist:
            model_url = lis[index].xpath('./a/@href').get()
            print(model_url)
            self.models_urls.append(model_url)


        # 依次对每个板块的页面进行请求
        for url in self.models_urls:  # 对每一个url进行请求发送
            yield scrapy.Request(url, callback=self.parse_model)

    # 每一个板块对应的新闻标题相关的内容都是动态加载出来的
    def parse_model(self, response):  # 解析每一个板块页面中对应新闻的标题和详情内容
        divs = response.xpath('//div[@class="ndi_main"]/div')
        for div in divs:
            title = div.xpath('.//div[@class="news_title"]/h3/a/text()').get()
            new_detail_url = div.xpath('.//div[@class="news_title"]/h3/a/@href').get()
            print('title',title)
            print('new',new_detail_url)
            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        content = response.xpath('div[@class="post_body"]//text()').get()
        # print(content)
        content = ''.join(content)
        item = response.mate['item']
        item['content'] = content

    def closed(self, spider):
        self.bro.quit()
