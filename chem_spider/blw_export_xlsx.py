#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
from mongodb import db, conn


def export_to_xlsx():
    # create a workbook
    workbook = xlsxwriter.Workbook(u'百灵威数据采集.xlsx')  # create a worksheet and export data
    worksheet = workbook.add_worksheet(u'百灵威')
    worksheet.write(0, 0, u'英文名称')
    worksheet.write(0, 1, u'中文名称')
    worksheet.write(0, 2, u'纯度')
    worksheet.write(0, 3, u'CAS')
    worksheet.write(0, 4, u'MDL')
    worksheet.write(0, 5, u'产品编号')
    worksheet.write(0, 6, u'分子式')
    worksheet.write(0, 7, u'规格')
    worksheet.write(0, 8, u'单价')
    worksheet.write(0, 9, u'预计发货期')

    row = 1
    col = 0

    products = db.blw_product_detail.find(timeout=False)  # remember to close the connection
    for item in products:
        worksheet.write(row, col, item.get('en_name', ''))
        worksheet.write(row, col + 1, item.get('name', ''))
        worksheet.write(row, col + 2, item.get('pure', ''))
        worksheet.write(row, col + 3, item.get('cas', ''))
        worksheet.write(row, col + 4, item.get('mdl', ''))
        worksheet.write(row, col + 5, item.get('item_num', '').replace(' ', ''))
        worksheet.write(row, col + 6, item.get('formula', ''))
        worksheet.write(row, col + 7, item.get('spec', ''))
        worksheet.write(row, col + 8, item.get('price', ''))
        worksheet.write(row, col + 9, item.get('deliver_time', ''))
        row += 1

    # close the connection because has set timeout to False
    conn.close()
    workbook.close()


if __name__ == '__main__':
    export_to_xlsx()