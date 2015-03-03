#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import random
from pyquery import PyQuery as pq
from mongodb import db
from settings import ALADDIN_BASE_URLS

def get_aladdin_pages():
    """
    获取每个分类的分页url,存进mongodb
    :return:
    """
    breadcrumb_search_url = 'http://www.aladdin-e.com/breadcrumbSearch/1/{amount}/20/{page}/CS/{catalog}'
    for key, url in ALADDIN_BASE_URLS.items():
        res = requests.get(url)
        if res.status_code == 200:
            content = res.content
            p = pq(content)
            amount = int(p('#itemListNavigationTopUtil .ml5.fl').text()[2: -10])
            catalog = url.split('/')[-1]
            pages = amount // 20

            if amount % 20:
                pages += 1

            for i in range(pages):
                url = breadcrumb_search_url.format(**{
                    'amount': amount,
                    'page': i+1,
                    'catalog': catalog
                })
                db.aladdin_base_url.update({'keyword': key}, {'$addToSet': {'urls': url}}, upsert=True)
        time.sleep(random.randint(0,5))


if __name__ == '__main__':
    get_aladdin_pages()

