#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import random
import time
from pyquery import PyQuery as pq
from mongodb import db, conn
from requests.exceptions import ConnectionError
from chem_log import log

# urls = [
#     'http://www.sigmaaldrich.com/china-mainland/zh/analytical-chromatography/analytical-chromatography-catalog.html',
#     'http://www.sigmaaldrich.com/china-mainland/chemistry-product.html',
#     'http://www.sigmaaldrich.com/china-mainland/zh/materials-science/material-science-products.html?TablePage=9540636'
# ]

base_url = 'http://www.sigmaaldrich.com'
chromatography_db_collection = {
    0: db.sigma_chromatography_urls_0,
    1: db.sigma_chromatography_urls_1,
    2: db.sigma_chromatography_urls_2,
    3: db.sigma_chromatography_urls_3,
    4: db.sigma_chromatography_urls_4,
    5: db.sigma_chromatography_urls_5,
    6: db.sigma_chromatography_urls_6,
    7: db.sigma_chromatography_urls_7,
    8: db.sigma_chromatography_urls_8,
    9: db.sigma_chromatography_urls_9
}

def get_chromatography_base_urls():
    """
    分析/色谱, 基本url
    :return:
    """
    url = 'http://www.sigmaaldrich.com/china-mainland/zh/analytical-chromatography/analytical-chromatography-catalog.html'
    res = get_res(url)
    if res:
        p = pq(res.content)
        section = p('div.text.parbase.section').eq(0)
        tables = pq(section).find('table.normal')
        for t in tables:
            trs = pq(t)('tbody').find('tr')
            for tr in trs:
                href = pq(tr)('td a').attr('href')
                db.sigma_chromatography_urls.insert({'url': base_url+href})


def get_chromatography_urls():
    """
    根据基本的url,一步步进入,若不是最终的产品页面,则保存进对应级别的url,否则保存具体产品的url
    :return:
    """

    for i in range(10):
        if i == 0:
            base_urls = db.sigma_chromatography_urls.find(timeout=False)
        else:
            base_urls = chromatography_db_collection[i-1].find(timeout=False)

        print base_urls.count(), '\n'
        if base_urls:
            for url in base_urls:
                res = get_res(url['url'])
                if res:
                    if 'Product #' not in res.content:
                        p = pq(res.content)
                        url_list = chromatography_extract_li(p)

                        for item in url_list:
                            # 保存进mongodb
                            chromatography_db_collection[i].insert({'url': item})
                    else:
                        # 是具体产品页面，保存url进具体产品url表
                        chromatography_extract_product_url(pq(res.content))
            conn.close()
        else:
            conn.close()
            break


def chromatography_extract_li(p):
    """
    提取出非具体产品列表页的产品分类url
    :param p: pyquery 对象
    :return:
    """
    url_list = []
    uls = p('div.opcContainer table#opcmaintable table ul.opcsectionlist')
    for ul in uls:
        lis = pq(ul).find('li')
        for li in lis:
            url_list.append(base_url + pq(li)('a').attr('href'))
    return url_list


def chromatography_extract_product_url(p):
    """
    获取产品列表页的产品url
    :param p: pyquery对象
    :return:
    """
    tables = p('table.opcTable')
    for t in tables:
        trs = pq(t)('tbody').find('tr')
        for tr in trs:
            href = pq(tr)('td:first a').attr('href')
            if href:
                db.sigma_chromatography_product_urls.insert({'url': base_url+href})





def get_chemistry_urls():
    """
    化学
    一级一级获取url,直到最终的产品页面,获取到每个产品详情页的url
    :return:
    """
    url = 'http://www.sigmaaldrich.com/china-mainland/chemistry-product.html'
    pass


def get_materials_urls():
    """
    材料科学
    一级一级获取url,直到最终的产品页面,获取到每个产品详情页的url
    :return:
    """
    url = 'http://www.sigmaaldrich.com/china-mainland/zh/materials-science/material-science-products.html?TablePage=9540636'
    pass


def get_res(url):
    """
    使用requests获取结果
    :param url:
    :return:
    """
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        res = requests.get(url)
        time.sleep(random.randint(0, 3))
        if res.status_code == 200:
            return res
        return None
    except ConnectionError, e:
        time.sleep(20)
        log.debug(str(e) + ' error')
        return None


