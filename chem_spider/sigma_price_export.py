#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
from mongodb import db, conn


def export_to_xlsx(collect, pre_book_name, skip_num, limit_num):
    # create a workbook
    book_name = pre_book_name + str(skip_num//limit_num+1) + '.xlsx'
    workbook = xlsxwriter.Workbook(book_name)  # create a worksheet and export data
    worksheet = workbook.add_worksheet(u"价格")
    worksheet.write(0, 0, u'编号')
    worksheet.write(0, 1, u'CAS')
    worksheet.write(0, 2, u'产品名')
    worksheet.write(0, 3, u'英文名')
    worksheet.write(0, 4, u'纯度')
    worksheet.write(0, 5, u'货号')
    worksheet.write(0, 6, u'库存')
    worksheet.write(0, 7, u'价格')

    row = 1
    col = 0

    # remember to close the connection
    products = collect.find(timeout=False).skip(skip_num).limit(limit_num)
    for item in products:
        worksheet.write(row, col, item.get('number', ''))
        worksheet.write(row, col + 1, item.get('cas', ''))
        worksheet.write(row, col + 2, item.get('name', ''))
        worksheet.write(row, col + 3, item.get('en_name', ''))
        worksheet.write(row, col + 4, item.get('pure', ''))
        worksheet.write(row, col + 5, unicode(item.get('spec', '').encode('iso-8859-1').decode('utf-8', 'ignore')).replace(u"加入购物车","").replace(u"查询库存","").replace(u"请输入数量","").replace(u"关闭 ：",""))
        worksheet.write(row, col + 6, unicode(item.get('shipping', '').encode('iso-8859-1').decode('utf-8', 'ignore')).replace(u"加入购物车","").replace(u"查询库存","").replace(u"请输入数量","").replace(u"关闭 ：",""))
        worksheet.write(row, col + 7, item.get('price', ''))
        row += 1

    # close the connection because has set timeout to False
    conn.close()
    workbook.close()


if __name__ == '__main__':
    collection = [
        # {"db": db.chemistry_product_price, "pre_book_name": u"sigma_化学_价格_"},
        {"db": db.materials_product_price, "pre_book_name": u"sigma_材料科学_价格_"},
        {"db": db.chromatography_product_price, "pre_book_name": u"sigma_分析色谱_价格_"}
    ]
    for item in collection:
        skip_num = 0
        limit_num = 5000
        while skip_num <= item["db"].count():
            export_to_xlsx(collect=item["db"], pre_book_name=item["pre_book_name"], skip_num=skip_num, limit_num=limit_num)
            skip_num += 5000