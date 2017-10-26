# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class Sohoa(Item):
    title = Field()
    description = Field()
    url = Field()
    content = Field()
    comments = Field()

class Comment(Item):
    url = Field()
    comment = Field()

class SohoaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
