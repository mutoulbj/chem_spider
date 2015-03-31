#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongodb import db, conn

from sigma_product_detail import ProductDetail

p = ProductDetail(db_price=db.chromatography_product_price, db_detail=db.chromatography_product_detail)

pros = db.sigma_chromatography_product_urls.find(timeout=False)
for pro in pros:
    p.get_base_info(url=pro["url"])
conn.close()