#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
from mongodb import db, conn


def export_to_xlsx(collect, pre_book_name, skip_num, limit_num):
    # create a workbook
    book_name = pre_book_name + str(skip_num//limit_num+1) + '.xlsx'
    workbook = xlsxwriter.Workbook(book_name)  # create a worksheet and export data
    worksheet = workbook.add_worksheet(u"信息")
    worksheet.write(0, 0, u'基本信息')
    worksheet.write(0, 1, u'产品编号')
    worksheet.write(0, 2, u'CAS号')
    worksheet.write(0, 3, u'品牌')
    worksheet.write(0, 4, u'产品名')
    worksheet.write(0, 5, u'其他基本信息')
    worksheet.write(0, 6, u'性质')
    worksheet.write(0, 7, u'Related categories')
    worksheet.write(0, 8, u'vapor pressure')
    worksheet.write(0, 9, u'其他性质')
    worksheet.write(0, 10, u'安全信息')
    worksheet.write(0, 11, u'信号词')
    worksheet.write(0, 12, u'危险声明')
    worksheet.write(0, 13, u'其他安全信息')

    row = 1
    col = 0

    # remember to close the connection
    products = collect.find(timeout=False).skip(skip_num).limit(limit_num)
    for item in products:
        baseinfo = ','.join([item.get("en_name", ""), item.get("pure",""), item.get("formula", ""),
                             item.get("registry_number", "",), item.get("einecs", ""), item.get("mdl", ""),
                             item.get("substance", "")])
        base_other = ','.join([i for i in item.get("base_other", {}).values()])
        prop = ','.join([item.get("assay", ""), item.get("autoignition_temp", ""), item.get("bp", ""),
                         item.get("mp", ""), item.get("density", "")])
        prop_other = ','.join([i for i in item.get("prop_other", {}).values()])
        safety = ','.join([item.get("sign_word", ""), item.get("danger_say", "")])
        safety_other = ','.join([i for i in item.get("safety_other", {}).values()])

        worksheet.write(row, col, baseinfo)
        worksheet.write(row, col + 1, item.get('number', ''))
        worksheet.write(row, col + 2, item.get('cas', ''))
        worksheet.write(row, col + 3, item.get('brand', ''))
        worksheet.write(row, col + 4, item.get('name', ''))
        worksheet.write(row, col + 5, base_other)
        worksheet.write(row, col + 6, prop)
        worksheet.write(row, col + 7, item.get('related_cate', ''))
        worksheet.write(row, col + 8, item.get('vapor', ''))
        worksheet.write(row, col + 9, prop_other)
        worksheet.write(row, col + 10, safety)
        worksheet.write(row, col + 11, item.get('sign_word', ''))
        worksheet.write(row, col + 12, item.get('danger_say', ''))
        worksheet.write(row, col + 13, safety_other)
        row += 1

    # close the connection because has set timeout to False
    conn.close()
    workbook.close()


if __name__ == '__main__':
    collection = [
        # {"db": db.chemistry_product_detail, "pre_book_name": u"sigma_化学_信息_"},
        {"db": db.materials_product_detail, "pre_book_name": u"sigma_材料科学_信息_"},
        {"db": db.chromatography_product_detail, "pre_book_name": u"sigma_分析色谱_信息_"}
    ]
    for item in collection:
        skip_num = 0
        limit_num = 5000
        while skip_num <= item["db"].count():
            export_to_xlsx(collect=item["db"], pre_book_name=item["pre_book_name"], skip_num=skip_num, limit_num=limit_num)
            skip_num += 5000