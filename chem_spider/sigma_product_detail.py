#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
from lxml.etree import XMLSyntaxError
import requests
import urllib
import copy

from pyquery import PyQuery as pq

from chem_log import log


class ProductDetail(object):
    """
    获取产品详情
    """
    def __init__(self, db_price, db_detail):
        super(ProductDetail, self).__init__()
        self.db_price = db_price
        self.db_detail = db_detail
        self.cookies = {
            'country': 'CHIM',
            'SialLocaleDef': 'CountryCode~CN|WebLang~-7|'
        }
        self.data = {'loadFor': 'PRD_RS'}
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=57F5320EB3E12CCBC1EEE5604531AC63.stltcat01b; country=CHIM; SialLocaleDef=CountryCode~CN|WebLang~-7|; fsr.r={"d":30,"i":"de35431-94629287-8bc3-f1b6-553fd","e":1426517396463}; TLTSID=3941AC5CCEAB10CE0357F15351D5A5DE; TLTUID=3941AC5CCEAB10CE0357F15351D5A5DE; cmTPSet=Y; SessionPersistence=CLICKSTREAMCLOUD%3A%3DvisitorId%3Danonymous%7CPROFILEDATA%3A%3Davatar%3D%2Fetc%2Fdesigns%2Fdefault%2Fimages%2Fcollab%2Favatar.png%2CisLoggedIn%3Dtrue%2CisLoggedIn_xss%3Dtrue%2CauthorizableId%3Danonymous%2CauthorizableId_xss%3Danonymous%2CformattedName%3D%2CformattedName_xss%3D%7CSURFERINFO%3A%3DIP%3D141.247.239.190%2Ckeywords%3D%2Cbrowser%3DChrome%2COS%3DMac%20OS%20X%2Cresolution%3D1280x800%7C; __unam=40e1073-14bfea75e24-15d68ec8-297; GUID=5c066db5-8327-4173-89ed-9913c8416174|NULL|1427738534996; _ga=GA1.2.1911851944.1425866637; Cck=present; fsr.s={"cp":{"REGION":"Europe","ClientId":"Unknown","MemberId":"Unknown","SiteId":"SA","TLTSID":"3941AC5CCEAB10CE0357F15351D5A5DE","TLTUID":"3941AC5CCEAB10CE0357F15351D5A5DE","GUID":"5c066db5-8327-4173-89ed-9913c8416174|NULL|1427738534996"},"v":-1,"rid":"de358f8-93429366-4aea-1971-5f2f5","to":5,"c":"http://www.sigmaaldrich.com/catalog/product/fluka/87708","pv":119,"lc":{"d0":{"v":119,"s":true}},"cd":0,"f":1427812524452,"sd":0}; fsr.a=1427812533888',
            'RA-Ver': '2.9.0',
            'RA-Sid': '3A65D2DE-20140808-051402-1053d8-0c4bf5'
        }

    def get_base_info(self, url):
        try:
            res = self.get_res(url)
            if res:
                d = {}
                p = pq(res.text)
                pd = p("div#productDetailHero div.contentStage div.productInfo")

                strongs = pq(pd).find("strong")
                for st in strongs:
                    if u"产品编号" in pq(st).text():
                        d["number"] = pq(st).text().replace(u"产品编号","").replace("|", "").strip()
                    elif u"CAS号" in pq(st).text():
                        d["cas"] = pq(st).text().replace(u"CAS号","").replace("|", "").strip()
                    elif pq(st).attr("itemprop") == "brand":
                        d["brand"] = pq(st).text().strip()

                h1s = pq(pd).find("h1")
                for h1 in h1s:
                    if pq(h1).attr("itemprop") == "name":
                        d["name"] = pq(h1).text().strip()

                h2s = pq(pd).find("h2")
                for h2 in h2s:
                    if pq(h2).attr("class") == "english_subtitle":
                        d["en_name"] = pq(h2).text().strip()
                    elif pq(h2).attr("itemprop") == "description":
                        d["pure"] = pq(h2).text().strip()  # 纯度

                ps = pq(pd).find("p")
                for x in ps:
                    if u"别名" in pq(x).text():
                        d["alias_name"] = pq(x).text().replace(u"别名:", "").strip()

                lis = pq(pd)("ul").find("li")
                if lis:
                    d["base_other"] = {}
                    for li in lis:
                        if u"分子式" in pq(li).text():
                            d["formula"] = pq(li).text().strip().split(" ")[1]
                        elif u"分子量" in pq(li).text():
                            d["weight"] = pq(li).text().strip().split(" ")[-1]
                        elif "MDL" in pq(li).text():
                            d["mdl"] = pq(li).text().strip().split(" ")[-1]
                        elif "Registry Number" in pq(li).text():
                            d["registry_number"] = pq(li).text().strip().split(" ")[-1]
                        elif "EINECS" in pq(li).text():
                            d["einecs"] = pq(li).text().strip().split(" ")[-1]
                        elif "Substance" in pq(li).text():
                            d["substance"] = pq(li).text().strip().split(" ")[-1]
                        else:
                            l = pq(li).text().strip().split(" ")
                            k = "_".join(l[0: -1]).strip().replace('.', '-')
                            d["base_other"][k] = l[-1]

                # 性质
                prop = p("div#productDetailProperties table")
                if prop:
                    trs = pq(prop).find("tr")
                    d["prop_other"] = {}
                    for tr in trs:
                        td0 = pq(pq(tr)("td").eq(0)).text().strip()
                        td1 = pq(pq(tr)("td").eq(1)).text().replace(u"更多...", "").strip()
                        if "Related Categories" in td0:
                            d["related_cate"] = td1
                        elif "vapor pressure" in td0:
                            d["vapor"] = td1
                        elif "assay" in td0:
                            d["assay"] = td1
                        elif "autoignition temp" in td0:
                            d["autoignition_temp"] = td1
                        elif "bp" in td0:
                            d["bp"] = td1
                        elif "mp" in td0:
                            d["mp"] = td1
                        elif "density" in td0:
                            d["density"] = td1
                        else:
                            k = td0.strip().replace(" ", "_").replace('.', '-')
                            d["prop_other"][k] = td1

                # 安全信息
                safety = p("div#productDetailSafety table")
                if safety:
                    trs = pq(prop).find("tr")[1:]
                    d["safety_other"] = {}
                    for tr in trs:
                        td0 = pq(pq(tr)("td").eq(0)).text().strip()
                        td1 = pq(pq(tr)("td").eq(1)).text().strip()
                        if u"信号词" in td0:
                            d["sign_word"] = td1  # 信号词
                        elif u"危险声明" in td0:
                            d["danger_say"] = td1  # 危险声明
                        else:
                            k = td0.strip().replace(' ', '_').replace('.', '-')
                            d["safety_other"][k] = td1

                # 产品描述
                desc = p("div#productDescription div.descriptionContent")
                if desc:
                    d["desc"] = pq(desc).text().strip()

                # 保存基本信息
                self.db_detail.update({"number": d["number"]}, {"$set": d}, upsert=True)

                # 库存与价格
                p_url = "http://www.sigmaaldrich.com/catalog/PricingAvailability.do?"
                payload = {
                    "productNumber": d.get("number", ""),
                    "brandKey": d.get("brand", ""),
                    "divId": "pricingContainerMessage"
                }
                r_url = p_url+urllib.urlencode(payload)
                r = self.post_res(r_url)
                if r:
                    d_price = {
                        "number": d.get("number", ""),
                        "cas": d.get("cas", ""),
                        "name": d.get("name" ""),
                        "en_name": d.get("en_name", ""),
                        "pure": d.get("pure", "")
                    }
                    s = r.content
                    try:
                        index = r.text.index("clearfix")
                        if s[index+9] == ' ':
                            l = list(s)
                            l[index + 9] = ">"
                            c = pq("".join(l))
                        else:
                            c = pq(s)
                    except ValueError, e:
                        c = pq(s)

                    pro_detail_inner = c("div.product-details-outer div.product-details-inner")

                    message = pq(pro_detail_inner)("div.product-discontinued").text().strip().replace(" ", "")
                    if not message:
                        message = pq(pro_detail_inner)("div.priceError").text().strip().replace(" ", "")

                    trs = pq(pro_detail_inner)("table").find("tr")[1:]
                    if trs:
                        for tr in trs:
                            td_0 = pq(tr)("td").eq(0)
                            td_1 = pq(tr)("td").eq(1)
                            td_2 = pq(tr)("td").eq(3)
                            spec = pq(td_0).text().strip()
                            shipping = pq(td_1).text().strip()
                            price = pq(td_2).text().strip()
                            d_copy = copy.deepcopy(d_price)
                            d_copy["spec"] = spec
                            d_copy["shipping"] = shipping
                            d_copy["price"] = price
                            self.db_price.update({"number": d_copy["number"], "spec": d_copy["spec"]},
                                                 {"$set": d_copy}, upsert=True)
                    if message:
                        d_copy = copy.deepcopy(d_price)
                        d_copy["spec"] = message
                        self.db_price.update({"number": d_copy["number"], "spec": d_copy["spec"]},
                                             {"$set": d_copy}, upsert=True)
        except Exception, e:
            print str(e)
            pass





    def get_res(self, url):
        """
        使用requests获取结果
        :param url:
        :return:
        """
        try:
            requests.adapters.DEFAULT_RETRIES = 5
            res = requests.get(url, cookies=self.cookies)
            time.sleep(random.randint(0, 3))
            if res.status_code == 200:
                return res
            return None
        except Exception, e:
            time.sleep(20)
            log.debug(str(e) + ' error')
            return None

    def post_res(self, url):
        try:
            res = requests.post(url, headers=self.headers, data=self.data)
            time.sleep(random.randint(0, 3))
            if res.status_code == 200:
                return res
            return None
        except Exception, e:
            time.sleep(20)
            log.debug(str(e) + ' error')
            return None