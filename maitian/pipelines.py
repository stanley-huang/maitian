# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import json
import csv
from pymongo import MongoClient
from scrapy import Item

# 将爬取结果进行持久化存储
class MaitianPipeline(object):
    def __init__(self):
        self.file = None


    def process_item(self, item, spider):
        '''

        :param item:
        :param spider:
        :return:
        '''
        # 创建一个写csv文件对象,并把把要写入的文件传进去
        self.writer = csv.writer(self.file)
        # 写csv文件
        if item['title']:
            self.writer.writerow((item['district'],item['title'],item['totalprice'],item['uniprice'],item['size']))
        return item

    @classmethod
    def from_crawler(cls,crawler):
        return cls()

    def open_spider(self,spider):
        now = time.strftime('%Y-%m-%d',time.localtime())
        filename = 'maitian' + now + '.csv'
        self.file = open(filename,'a',encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()


# 将爬取结果永久存放至MongoDB
class MongoDBPipeline(object):
    def __init__(self):
        pass

    def process_item(self,item,spider):
        '''

        :param item:
        :param spider:
        :return:
        '''
        self.insert_db(item)
        return item

    def insert_db(self,item):
        if isinstance(item,Item):
            item = dict(item)
        self.db.maitian.insert_one(item)

    @classmethod
    def from_crawler(cls,crawler):
        return cls()

    def open_spider(self,spider):
        '''
        创建连接mongodb数据库的实例对象
        :param spider:
        :return:
        '''
        db_uri = spider.settings.get('MONGODB_URI','mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME','scrapy_db')

        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]

    def close_spider(self,spider):
        '''
        关闭数据库实例
        :param spider:
        :return:
        '''
        self.db_client.close()