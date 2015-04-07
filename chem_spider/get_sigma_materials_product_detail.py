#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongodb import db, conn

from sigma_product_detail import ProductDetail

p = ProductDetail(db_price=db.materials_product_price, db_detail=db.materials_product_detail)

pros = db.sigma_materials_product_urls.find(timeout=False).skip(26519)
for pro in pros:
    p.get_base_info(url=pro["url"])
conn.close()