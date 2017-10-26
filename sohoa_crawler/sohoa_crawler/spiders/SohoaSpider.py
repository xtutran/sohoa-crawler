import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request
import json
from sohoa_crawler.items import Sohoa
from sohoa_crawler.items import Comment
import re
import requests

class SohoaSpider(scrapy.Spider):
    name = "sohoa"
    allowed_domains = ["sohoa.vnexpress.net", "interactions.vnexpress.net"]
    start_urls = [
        "http://interactions.vnexpress.net/index/get?offset=24&limit=24&frommobile=0&sort=like&objectid=3206913&objecttype=1&siteid=1002592"
        ]

    def parse(self, response):

        item = Sohoa()

        item['title'] = response.xpath('//title/text()').extract()[0].encode('utf8')
        item['url'] = response.url
        item['description'] = response.xpath('//*[@id="box_details_news"]/div/div[1]/div[1]/div[4]/text()').extract()[0].encode('utf8')
        
        ## parse main content
        pages = []
        for sel in response.xpath('//div[@class="fck_detail width_common"]/p[@class="Normal"]'):
            page = sel.xpath('text()').extract()
            if len(page) == 0:
                continue
            pages.append(page[0].strip().encode('utf8'))

        item['content'] = '\n'.join(pages)
        
        ## parse user comments
        detail = response.xpath('//div[@class="item_social"]')
        objectid = detail.xpath('@data-component-objectid').extract()[0].strip()     
        siteid = detail.xpath('@data-component-siteid').extract()[0].strip()
        objecttype = detail.xpath('@data-objecttype').extract()[0].strip()

        comment_url = "http://interactions.vnexpress.net/index/get?offset=0&limit=1000&frommobile=0&sort=like&objectid=" + str(objectid)\
                    + "&objecttype=" + str(objecttype) + "&siteid=" + str(siteid) 
        print comment_url

        r = requests.get(comment_url)
        jsonStr = re.match('defaultCallback\((.*?)\);', r.text).group(1)
        with open('comments.json', 'w') as f:
            f.write(jsonStr)
        
        return item
