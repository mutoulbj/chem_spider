#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import copy
import requests
from pyquery import PyQuery as pq
from mongodb import db



def get_product():
    detail_urls = db.aladdin_detail_page.find()
    for item in detail_urls:
        for url in item['urls']:
            res = requests.get(url)
            if res.status_code == 200:
                p = pq(res.content)

                d = {}
                d['number'] = p('div.pl10.fl.w120.pt14 h1.itmdet-topbar-itmnum').text()
                d['name'] = p('div.pt14 h1.f18').text()
                d['en_name'] = p('div.itmdet-baseCnt-title span.fb').text().replace('Product Name:', '').strip()

                tbody = pq(p('div.itmdet-baseCnt.fl table.productOverViewInfo tbody tr'))
                for t in tbody:
                    tr = pq(t)
                    if u'别名' in tr('td:first').text():
                        d['alias_name'] = tr('td').eq(1).text()

                    if 'CAS' in tr('td:first').text():
                        d['cas'] = tr('td').eq(1).text()

                    if u'分子式' in tr('td:first').text():
                        d['formula'] = tr('td').eq(1).text()  # 分子式

                    if u'分子量' in tr('td:first').text():
                        d['weight'] = tr('td').eq(1).text()  # 分子量

                    if 'EINECS' in tr('td:first').text():
                        d['einecs'] = tr('td').eq(1).text()

                    if 'MDL' in tr('td:first').text():
                        d['mdl'] = tr('td').eq(1).text()

                tbody_2 = pq(p('table#pro_tbl tbody tr'))

                if not tbody_2:
                    d['item_num'] = p('#addToCardsForm div.p10').text()
                    save_product(keyword=item['keyword'], d=d)
                else:
                    for i in tbody_2:
                        tr = pq(i)
                        d_copy = copy.deepcopy(d)
                        d_copy['item_num'] = tr('td').eq(0).text()
                        d_copy['spec'] = pq(tr('td').eq(1))('a').text()  # 产品规格
                        d_copy['sale_price'] = pq(tr('td').eq(2))('span').text()  # 销售价格
                        d_copy['discounted_price'] = pq(tr('td').eq(3))('b').text()  # 折扣价格
                        d_copy['stock'] = tr('td').eq(4).text()  # 库存
                        d_copy['unit'] = tr('td').eq(6).text()  # 计量单位
                        save_product(keyword=item['keyword'], d=d_copy)

            time.sleep(random.randint(0,4))


def save_product(keyword, d):
    if keyword == 'fxkx':
        db.aladdin_product_fxkx.update({'number': d['number']}, {'$set': d}, upsert=True)
    elif keyword == 'smkx':
        db.aladdin_product_smkx.update({'number': d['number']}, {'$set': d}, upsert=True)
    elif keyword == 'gdhx':
        db.aladdin_product_gdhx.update({'number': d['number']}, {'$set': d}, upsert=True)
    elif keyword == 'clkx':
        db.aladdin_product_clkx.update({'number': d['number']}, {'$set': d}, upsert=True)

if __name__ == '__main__':
    get_product()