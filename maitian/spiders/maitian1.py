# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
import redis
from ..items import MaitianItem


# 添加redis配置
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

class Maitian1Spider(RedisSpider):               # Redis分布式爬虫
    name = 'maitian1'
    allowed_domains = ['maitian1.com']
    # 添加redis配置，将爬取的数据入库
    redis_key = 'maitianspider:start_urls'

    def parse(self, response):
        # 爬取首页的二手房信息
        for item in response.xpath('//div[@class="list_title"]'):
            title = item.xpath('./h1/a/text()').extract_first().strip(),
            totalprice = item.xpath('.//span/text()').extract_first(),
            uniprice = item.xpath('.//ol/text()').re(r'\d+')[0],
            size = item.xpath('./p/span/text()').extract_first(),
            district = item.xpath('./p/text()').re(r'昌平|朝阳|东城|大兴|丰台|海淀|石景山|顺义|通州|西城')[0],
            yield MaitianItem(
                            title=title,
                            totalprice=totalprice,
                            uniprice=uniprice,
                            size=size,
                            district=district
            )
        # 爬取剩余页面的二手房信息
        next_page_obj = response.xpath('//div[@id="paging"]/a/@href').extract()
        print("-->next_page_obj:",next_page_obj)
        for page in next_page_obj:
            next_page_url = "http://bj.maitian.cn" + page
            print("-->next_page_url:",next_page_url)
            yield Request(url=next_page_url,dont_filter=True)
            # 在Redis数据库中添加 key,使用Redis分布式爬虫时启用此配置
            r.lpush('maitianspider:start_urls',next_page_url)
