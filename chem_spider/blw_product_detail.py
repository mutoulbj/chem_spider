#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import requests
import copy
import json
from mongodb import db, conn


def get_product_detail():
    base_url = 'http://www.jkchemical.com/Controls/Handler/GetPackAgeJsonp.ashx?value={pro_name}&type=product'
    pros = db.blw_product.find(timeout=False)

    for pro in pros:
        pro.pop('_id')
        pro_name = pro.get('pro_name', None)
        if pro_name:
            url = base_url.format(pro_name=pro_name)
            res = requests.get(url)
            if res.status_code == 200:
                res = json.loads(res.content[1:-1])
                print res
                for item in res:
                    d = copy.deepcopy(pro)
                    save_product_detail(d, item)
            time.sleep(random.randint(0, 5))
    conn.close()


def save_product_detail(pro, item):
    deliverTime = item.get('_deliverTime', None)

    if deliverTime:
        pro['deliver_time'] = deliverTime + item.get('_timeUnit') + u'发货'
    else:
        pro['deliver_time'] = u'现货'

    pro['spec'] = item.get('_package', '')
    pro['price'] = item.get('_listPrice', '')
    db.blw_product_detail.insert(pro)


if __name__ == '__main__':
    get_product_detail()