# -*- coding: utf-8 -*-

# Scrapy settings for test project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'test'

SPIDER_MODULES = ['test.spiders']
NEWSPIDER_MODULE = 'test.spiders'
DEPTH_LIMIT = 3
DEPTH_PRIORITY = 2
DEPTH_STATS_VERBOSE = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'test (+http://www.yourdomain.com)'
