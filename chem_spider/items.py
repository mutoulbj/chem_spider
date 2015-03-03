#! /usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

class AladdinItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    en_name = scrapy.Field()
    alias_name = scrapy.Field()
    cas = scrapy.Field()
    formula = scrapy.Field()  # 分子式
    weight = scrapy.Field()   # 分子量
    einecs = scrapy.Field()
    mdl = scrapy.Field()
    item_num = scrapy.Field()
    spec = scrapy.Field()     # 产品规格
    sale_price = scrapy.Field()  # 销售价格
    discounted_price = scrapy.Field() # 折扣价格
    stock = scrapy.Field()    # 库存
    unit = scrapy.Field()     # 计量单位