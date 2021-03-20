import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        divs = response.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div')
        for div in divs:
            name = div.xpath('.//p[@class="t"]/span[1]/@title')
            job_url = div.xpath('./a/@href')
            print(name,job_url)