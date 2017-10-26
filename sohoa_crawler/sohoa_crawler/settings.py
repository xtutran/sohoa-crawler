# -*- coding: utf-8 -*-

# Scrapy settings for sohoa_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sohoa_crawler'

SPIDER_MODULES = ['sohoa_crawler.spiders']
NEWSPIDER_MODULE = 'sohoa_crawler.spiders'

ITEM_PIPELINES = [
 'sohoa_crawler.pipelines.SohoaPipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sohoa_crawler (+http://www.yourdomain.com)'
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'sohoa_crawler'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''
