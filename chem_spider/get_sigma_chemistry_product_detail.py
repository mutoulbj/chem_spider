#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongodb import db, conn

from sigma_product_detail import ProductDetail

p = ProductDetail(db_price=db.chemistry_product_price, db_detail=db.chemistry_product_detail)

count = db.chemistry_product_detail.count()
pros = db.sigma_chemistry_product_urls.find(timeout=False).skip(count)
for pro in pros:
    p.get_base_info(url=pro["url"])
conn.close()