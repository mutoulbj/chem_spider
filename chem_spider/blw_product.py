#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import requests
from pyquery import PyQuery as pq
from mongodb import db, conn
from requests.exceptions import ConnectionError


def get_product():
    detail_urls = db.blw_urls.find(timeout=False)
    for item in detail_urls:
        try:
            res = requests.get(item['url'])
        except ConnectionError:
            res = False

        if res and res.status_code == 200:
            p = pq(res.text)

            trs = get_trs(p)

            for tr in trs:
                d = get_product_base(tr)  # 获取基本信息

                #  获取不同价格、规格
                pro_name = get_pro_name(tr)
                d['pro_name'] = pro_name

                save_product(d)
        time.sleep(random.randint(0, 5))
    conn.close()


def get_trs(p):
    return pq(p('table#ctl00_ContentPlaceHolder1_up_Product_GridView1').find('tr'))


def get_product_base(tr):
    spans = pq(tr)('td:first div.PRODUCT_box div.product_name a').find('span')
    if len(spans) > 1:
        # 存在中文名称
        name = pq(tr)('td:first div.PRODUCT_box div.product_name a span').eq(0).text()
        en_name = pq(tr)('td:first div.PRODUCT_box div.product_name a').text().replace(name, '').replace(u'（订货以英文名称为准）','').strip()
    else:
        name = ''
        en_name = pq(tr)('td:first div.PRODUCT_box div.product_name a').text().strip()

    d = {
        'name': name,
        'en_name': en_name
    }

    lis = pq(tr)('td:first div.PRODUCT_box div.mulu_text div.left ul').find('li')
    for li in lis:
        c = pq(li).text()
        if u'纯度' in c:
            d['pure'] = c.split(u'：')[1].strip()
        elif 'CAS' in c:
            d['cas'] = c.split(u'：')[1].strip()
        elif 'MDL' in c:
            d['mdl'] = c.split(u'：')[1].strip()
        elif u'产品编号' in c:
            d['item_num'] = c.split(u'：')[1].strip()
        elif u'分子式' in c:
            d['formula'] = c.split(u'：')[1].strip().replace(' ', '')
    return d


def get_pro_name(tr):
    # 获取pro_name,用于后续请求获取产品详情
    pro_name = pq(pq(tr)('td').eq(0))('div.PRODUCT_box div.mulu_r').attr('data-jkid')
    return pro_name


def get_product_result(d, pro):
    d['spec'] = pq(pro)('td').eq(0).text()
    d['price'] = pq(pro)('td').eq(1).text()
    d['send'] = pq(pro)('td').eq(4).text()
    return d


def save_product(d):
    db.blw_product.insert(d)


if __name__ == '__main__':
    get_product()