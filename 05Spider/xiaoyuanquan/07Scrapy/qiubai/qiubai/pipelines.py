# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class QiubaiPipeline:
    fp = None

    # 重写父类方法
    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('qiushi.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content + '\n')
        #
        return item  # 就会传递给下一个即将被执行的管道类

    def close_spider(self, spider):
        print('结束爬虫')
        self.fp.close()


class mysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root',
                                    password='admin123', db='qiubai')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values("%s","%s")' % (item["author"], item["cotent"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()
