# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:08:31 2015

@author: Wizard
"""

import scrapy
from test.items import TestItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["berkeley.edu"]
    start_urls = [
        "http://vcresearch.berkeley.edu/faculty-expertise?name=&expertise_area=&term_node_tid_depth="
    ]
    rules = (Rule(SgmlLinkExtractor(allow=()), callback='parse_items', follow=True),)

    def parse_items(self, response):
        if not response.url.startswith('http://vcresearch'):
            torrent = TestItem()
            torrent['rlabel'] = -1
            torrent['plabel'] = -1
            torrent['url'] = response.url
            torrent['head'] = response.xpath('//head').extract()[0]
            torrent['body'] = response.xpath('//body').extract()[0]
            return torrent


# class TestSpider(BaseSpider):
#   name = "test"
#   allowed_domains = ["doc.scrapy.org"]
#   start_urls = ["http://doc.scrapy.org/en/0.24/index.html"]

#   def parse(self, response):
#       hxs = HtmlXPathSelector(response)
#       titles = hxs.select("//span[@class='pl']")
#       item = TestItem()
#       item ["url"] = response.url
#       item ["name"] = response.xpath("//h1/text()").extract()
#       item['description'] = response.body
#       return item