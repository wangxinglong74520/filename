# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from redis import Redis


class MoviePipeline(object):
    conn = None

    def open_spider(self, spider):
        self.conn = spider.conn

    def process_item(self,item,spider):
        dic = {
            'name':item['name'],
            'desc':item['desc']
        }
        print(dic)
        self.conn.lpush('dovieData',dic)
        return item