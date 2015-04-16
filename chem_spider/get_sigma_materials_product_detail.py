#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongodb import db, conn

from sigma_product_detail import ProductDetail

# p = ProductDetail(db_price=db.materials_product_price, db_detail=db.materials_product_detail)
p = ProductDetail(db_price=db.materials_product_price, db_detail=db.materials_product_detail_1)

count = db.materials_product_detail_1.count()
pros = db.sigma_materials_product_urls.find(timeout=False).skip(count)
for pro in pros:
    p.get_base_info(url=pro["url"])
conn.close()