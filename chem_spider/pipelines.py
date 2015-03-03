#! /usr/bin/env python
# -*- coding: utf-8 -*-
from chem_spider import items

class ItemStoreProcess(object):
    def process_item(self, item, spider):
        if isinstance(item, items.AladdinItem):
            pass