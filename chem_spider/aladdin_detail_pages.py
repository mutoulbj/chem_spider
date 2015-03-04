#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import random
from pyquery import PyQuery as pq
from mongodb import db


def get_aladdin_detail_url():
    base_urls = db.aladdin_base_url.find({'keyword': 'gdhx'})
    for item in base_urls:
        for url in item['urls']:
            res = requests.get(url)
            if res.status_code == 200:
                p = pq(res.content)
                tbody = pq(p('table#itmlist-tbl tbody tr'))

                for i in tbody:
                    tr = pq(i)
                    href = 'http://www.aladdin-e.com' + tr('td:first a').attr('href')
                    db.aladdin_detail_page.update({'keyword': item['keyword']}, {'$addToSet': {'urls':  href}}, upsert=True)
            print '*'
            time.sleep(random.randint(0, 5))


if __name__ == '__main__':
    get_aladdin_detail_url()