#! /usr/bin/env python
# -*- coding: utf-8 -*-

BOT_NAME = 'chem_spider'

SPIDER_MODULES = ['chem_spider.spiders']
NEWSPIDER_MODULE = 'chem_spider.spiders'

DEFAULT_ITEM_CLASS = 'chem_spider.items.AladdinItem'
ITEM_PIPELINES = {
    'chem_spider.piplines.ItemStoreProcess': 1
}

LOG_FILE = 'logs/debug.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = True

# cookies
COOKIES_ENABLED = True
COOKIES_DEBUG = False

# aladdin
ALADDIN_BASE_URLS = {
    'fxkx': 'http://www.aladdin-e.com/catalog/1485',
    'smkx': 'http://www.aladdin-e.com/catalog/1424',
    'gdhx': 'http://www.aladdin-e.com/catalog/635',
    'clkx': 'http://www.aladdin-e.com/catalog/1357'
}

# mongodb
# mongodb_uri = 'mongodb://localhost:27017'
mongodb_uri = 'mongodb://121.40.85.47:27017'
mongodb_db_name = 'chem_spider'
mongodb_user = 'mutoulbj'
mongodb_passwd = 'fan'