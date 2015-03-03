#! /usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy import Request
from chem_spider.mongodb import db

class AladdinSpider(CrawlSpider):
    name = 'aladdin_spider'
    allowed_domins = ['aladdin-e.com']
    
    def __init__(self):
        super(AladdinSpider, self).__init__()
        start_urls = []
        detail_urls = db.aladdin_detail_page.find()

        for item in detail_urls:
            for url in item['urls']:
                start_urls.append(url)


