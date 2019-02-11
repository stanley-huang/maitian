# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaitianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    totalprice = scrapy.Field()
    uniprice = scrapy.Field()
    size = scrapy.Field()
    district = scrapy.Field()