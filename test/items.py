# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rlabel = scrapy.Field()
    plabel = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    head = scrapy.Field()
