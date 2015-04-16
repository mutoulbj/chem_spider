#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
from mongodb import db, conn


def export_to_xlsx(collect, pre_book_name, skip_num, limit_num):
    # create a workbook
    book_name = pre_book_name + str(skip_num//limit_num+1) + '.xlsx'
    workbook = xlsxwriter.Workbook(book_name)  # create a worksheet and export data
    worksheet = workbook.add_worksheet(u"信息")
    worksheet.write(0, 0, u'产品编号')
    worksheet.write(0, 1, u'CAS号')
    worksheet.write(0, 2, u'品牌')
    worksheet.write(0, 3, u'产品名')
    worksheet.write(0, 4, u'英文名')
    worksheet.write(0, 5, u'纯度')
    worksheet.write(0, 6, u'线性分子式')
    worksheet.write(0, 7, u'分子量')
    worksheet.write(0, 8, u'Beilstein Registry Number')
    worksheet.write(0, 9, u'EINECS编号')
    worksheet.write(0, 10, u'MDL')
    worksheet.write(0, 11, u'Pubchem Substance ID')
    worksheet.write(0, 12, u'其他基本信息')

    worksheet.write(0, 13, u'Related categories')
    worksheet.write(0, 14, u'Grade')
    worksheet.write(0, 15, u'vapor density')
    worksheet.write(0, 16, u'vapor pressure')
    worksheet.write(0, 17, u'assay')
    worksheet.write(0, 18, u'autoignition temp')
    worksheet.write(0, 19, u'impurities')
    worksheet.write(0, 20, u'refractive index')
    worksheet.write(0, 21, u'bp')
    worksheet.write(0, 22, u'mp')
    worksheet.write(0, 23, u'density')
    worksheet.write(0, 24, u'expl. lim.')
    worksheet.write(0, 25, u'其他性质')
    # worksheet.write(0, 10, u'符号')
    # worksheet.write(0, 11, u'信号词')
    # worksheet.write(0, 12, u'危险声明')
    # worksheet.write(0, 13, u'其他安全信息')

    row = 1
    col = 0

    # remember to close the connection
    products = collect.find(timeout=False).skip(skip_num).limit(limit_num)
    for item in products:
        # baseinfo = ','.join([item.get("en_name", ""), item.get("pure",""), item.get("formula", ""),
        #                      item.get("registry_number", "",), item.get("einecs", ""), item.get("mdl", ""),
        #                      item.get("substance", "")])
        base_other = ','.join([i for i in item.get("base_other", {}).values()])
        # prop = ','.join([item.get("assay", ""), item.get("autoignition_temp", ""), item.get("bp", ""),
        #                  item.get("mp", ""), item.get("density", "")])
        prop_other = ','.join([i for i in item.get("prop_other", {}).values()])
        # safety = ','.join([item.get("sign_word", ""), item.get("danger_say", "")])
        # safety_other = ','.join([i for i in item.get("safety_other", {}).values()])

        worksheet.write(row, col, item.get('number', ''))
        worksheet.write(row, col + 1, item.get('cas', ''))
        worksheet.write(row, col + 2, item.get('brand', ''))
        worksheet.write(row, col + 3, item.get('name', ''))
        worksheet.write(row, col + 4, item.get('en_name', ''))
        worksheet.write(row, col + 5, item.get('pure', ''))
        worksheet.write(row, col + 6, item.get('formula', ''))
        worksheet.write(row, col + 7, item.get('weight', ''))
        worksheet.write(row, col + 8, item.get('registry_number', ''))
        worksheet.write(row, col + 9, item.get('einecs', ''))
        worksheet.write(row, col + 10, item.get('mdl', ''))
        worksheet.write(row, col + 11, item.get('substance', ''))
        worksheet.write(row, col + 12, base_other)

        worksheet.write(row, col + 13, item.get('related_cate', ''))
        worksheet.write(row, col + 14, item.get("prop_other", {}).get("grade", ''))
        worksheet.write(row, col + 15, item.get("safety_other", {}).get("vapor_density", ''))
        worksheet.write(row, col + 16, item.get("safety_other", {}).get("vapor_pressure", ''))
        worksheet.write(row, col + 17, item.get('assay', ''))
        worksheet.write(row, col + 18, item.get("autoignition_temp", ''))
        worksheet.write(row, col + 19, item.get("safety_other", {}).get("impurities", ''))
        worksheet.write(row, col + 20, item.get("safety_other", {}).get("refractive_index", ''))
        worksheet.write(row, col + 21, item.get('mp', ''))
        worksheet.write(row, col + 22, item.get('bp', ''))
        worksheet.write(row, col + 23, item.get("safety_other", {}).get("density", ''))
        worksheet.write(row, col + 24, item.get("safety_other", {}).get("expl-_lim-", ''))
        worksheet.write(row, col + 25, prop_other)
        # worksheet.write(row, col + 10, safety)
        # worksheet.write(row, col + 11, item.get('sign_word', ''))
        # worksheet.write(row, col + 12, item.get('danger_say', ''))
        # worksheet.write(row, col + 13, safety_other)
        row += 1

    # close the connection because has set timeout to False
    conn.close()
    workbook.close()


if __name__ == '__main__':
    collection = [
        {"db": db.chemistry_product_detail, "pre_book_name": u"sigma_化学_信息_"},
        {"db": db.materials_product_detail, "pre_book_name": u"sigma_材料科学_信息_"},
        {"db": db.chromatography_product_detail, "pre_book_name": u"sigma_分析色谱_信息_"}
    ]
    for item in collection:
        skip_num = 0
        limit_num = 5000
        while skip_num <= item["db"].count():
            export_to_xlsx(collect=item["db"], pre_book_name=item["pre_book_name"], skip_num=skip_num, limit_num=limit_num)
            skip_num += 5000