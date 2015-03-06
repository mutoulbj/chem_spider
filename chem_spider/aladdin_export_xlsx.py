#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
from mongodb import db, conn


def export_to_xlsx():
    # create a workbook
    workbook = xlsxwriter.Workbook(u'阿拉丁数据采集.xlsx')

    types = [
        {
            'key': 'clkx',
            'sheet_name': u'材料科学',
            'collection': db.aladdin_product_clkx,
        },
        {
            'key': 'fxkx',
            'sheet_name': u'分析科学',
            'collection': db.aladdin_product_fxkx,
        },
        {
            'key': 'smkx',
            'sheet_name': u'生命科学',
            'collection': db.aladdin_product_smkx,
        },
        {
            'key': 'gdhx',
            'sheet_name': u'高端化学',
            'collection': db.aladdin_product_gdhx,
        }
    ]

    for t in types:
        # create a worksheet and export data
        worksheet = workbook.add_worksheet(t['sheet_name'])
        worksheet.write(0, 0, u'编号')
        worksheet.write(0, 1, u'产品名')
        worksheet.write(0, 2, u'英文名')
        worksheet.write(0, 3, u'别名')
        worksheet.write(0, 4, u'CAS号')
        worksheet.write(0, 5, u'分子式')
        worksheet.write(0, 6, u'分子量')
        worksheet.write(0, 7, u'EINECS号')
        worksheet.write(0, 8, u'MDL号')
        worksheet.write(0, 9, u'货号')
        worksheet.write(0, 10, u'产品规格')
        worksheet.write(0, 11, u'销售价')
        worksheet.write(0, 12, u'您的折扣价')
        worksheet.write(0, 13, u'可用库存')

        row = 1
        col = 0

        products = t['collection'].find(timeout=False)  # remember to close the connection
        for item in products:
            worksheet.write(row, col, item.get('number', ''))
            worksheet.write(row, col+1, item.get('name', ''))
            worksheet.write(row, col+2, item.get('en_name', ''))
            worksheet.write(row, col+3, item.get('alias_name', ''))
            worksheet.write(row, col+4, item.get('cas', ''))
            worksheet.write(row, col+5, item.get('formula', '').replace(' ', ''))
            worksheet.write(row, col+6, item.get('weight', ''))
            worksheet.write(row, col+7, item.get('einecs', ''))
            worksheet.write(row, col+8, item.get('mdl', ''))
            worksheet.write(row, col+9, item.get('item_num', ''))
            worksheet.write(row, col+10, item.get('spec', ''))
            worksheet.write(row, col+11, item.get('sale_price', ''))
            worksheet.write(row, col+12, item.get('discounted_price', ''))
            worksheet.write(row, col+13, item.get('stock', ''))

        # close the connection because has set timeout to False
        conn.close()
    workbook.close()


if __name__ == '__main__':
    export_to_xlsx()