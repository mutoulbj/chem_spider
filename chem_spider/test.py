import requests
# headers = {
#     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,ko;q=0.2,zh-TW;q=0.2'
# }
cookies = {
    'country': 'CHIM',
    'SialLocaleDef': 'CountryCode~CN|WebLang~-7|',
    # 'JSESSIONID': '141F893D9E3F645E5B86217E3B25C9B0.stltcat01b',
    # 'fsr.r': '{"d":30,"i":"de35431-94629287-8bc3-f1b6-553fd","e":1426517396463}',
    # 'TLTSID': '3941AC5CCEAB10CE0357F15351D5A5DE',
    # 'TLTUID': '3941AC5CCEAB10CE0357F15351D5A5DE',
    # 'cmTPSet': 'Y',
    # 'GUID': '5c066db5-8327-4173-89ed-9913c8416174|NULL|1427292870735',
    # '_dc_gtm_UA-51006100-1': '1',
    # '_gat_UA-51006100-1': '1',
    # 'Cck': 'present',
    # 'fsr.s': '{"cp":{"REGION":"Europe","ClientId":"Unknown","MemberId":"Unknown","SiteId":"SA","TLTSID":"3941AC5CCEAB10CE0357F15351D5A5DE","TLTUID":"3941AC5CCEAB10CE0357F15351D5A5DE","GUID":"5c066db5-8327-4173-89ed-9913c8416174|NULL|1427292870735"},"v":-1,"rid":"de358f8-93429366-4aea-1971-5f2f5","to":5,"c":"http://www.sigmaaldrich.com/china-mainland/zh/materials-science/material-science-products.html","pv":96,"lc":{"d0":{"v":96,"s":true}},"cd":0,"f":1427306062446,"sd":0}',
    # 'SessionPersistence': 'CLICKSTREAMCLOUD%3A%3DvisitorId%3Danonymous%7CPROFILEDATA%3A%3Davatar%3D%2Fetc%2Fdesigns%2Fdefault%2Fimages%2Fcollab%2Favatar.png%2CisLoggedIn%3Dtrue%2CisLoggedIn_xss%3Dtrue%2CauthorizableId%3Danonymous%2CauthorizableId_xss%3Danonymous%2CformattedName%3D%2CformattedName_xss%3D%7CSURFERINFO%3A%3DIP%3D141.247.239.190%2Ckeywords%3D%2Cbrowser%3DChrome%2COS%3DMac%20OS%20X%2Cresolution%3D1280x800%7C',
    # '__unam': '40e1073-14bfea75e24-15d68ec8-297',
    # '_ga': 'GA1.2.1911851944.1425866637',
    # 'fsr.a': '1427306068314',
    # 'cmRS': '&t1=1427306064842&t2=1427306068287&t3=1427306068343&t4=1427306062447&lti=1427306068342&ln=&hr=/catalog/product/aldrich/674419%3Flang%3Dzh%26region%3DCN&fti=&fn=SearchForm%3A0%3Bemailfriend%3A1%3BProductAddToCart%3A2%3BProductAddToCart%3A3%3BProductAddToShelf%3A4%3BsearchForm%3A5%3Bmyform%3A6%3B&ac=&fd=&uer=&fu=&pi=Catalog%20Page%3A%2019812733%20ZH&ho=cm.sigmaaldrich.com/eluminate%3F&ci=90142934'
}
# res = requests.get('http://www.sigmaaldrich.com/catalog/product/aldrich/h36206?lang=en&region=US', cookies=cookies)
# print res.content


headers = {
    # 'Host': 'www.sigmaaldrich.com',
# 'Connection': 'keep-alive',
# 'Content-Length': '14',
# 'Pragma': 'no-cache',
# 'Cache-Control': 'no-cache',
# 'Accept': 'text/html, */*; q=0.01',
# 'Origin': 'http://www.sigmaaldrich.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 'Referer': 'http://www.sigmaaldrich.com/catalog/product/fluka/87708?lang=zh&region=CN',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,ko;q=0.2,zh-TW;q=0.2',
'Cookie': 'JSESSIONID=57F5320EB3E12CCBC1EEE5604531AC63.stltcat01b; country=CHIM; SialLocaleDef=CountryCode~CN|WebLang~-7|; fsr.r={"d":30,"i":"de35431-94629287-8bc3-f1b6-553fd","e":1426517396463}; TLTSID=3941AC5CCEAB10CE0357F15351D5A5DE; TLTUID=3941AC5CCEAB10CE0357F15351D5A5DE; cmTPSet=Y; SessionPersistence=CLICKSTREAMCLOUD%3A%3DvisitorId%3Danonymous%7CPROFILEDATA%3A%3Davatar%3D%2Fetc%2Fdesigns%2Fdefault%2Fimages%2Fcollab%2Favatar.png%2CisLoggedIn%3Dtrue%2CisLoggedIn_xss%3Dtrue%2CauthorizableId%3Danonymous%2CauthorizableId_xss%3Danonymous%2CformattedName%3D%2CformattedName_xss%3D%7CSURFERINFO%3A%3DIP%3D141.247.239.190%2Ckeywords%3D%2Cbrowser%3DChrome%2COS%3DMac%20OS%20X%2Cresolution%3D1280x800%7C; __unam=40e1073-14bfea75e24-15d68ec8-297; GUID=5c066db5-8327-4173-89ed-9913c8416174|NULL|1427738534996; _ga=GA1.2.1911851944.1425866637; Cck=present; fsr.s={"cp":{"REGION":"Europe","ClientId":"Unknown","MemberId":"Unknown","SiteId":"SA","TLTSID":"3941AC5CCEAB10CE0357F15351D5A5DE","TLTUID":"3941AC5CCEAB10CE0357F15351D5A5DE","GUID":"5c066db5-8327-4173-89ed-9913c8416174|NULL|1427738534996"},"v":-1,"rid":"de358f8-93429366-4aea-1971-5f2f5","to":5,"c":"http://www.sigmaaldrich.com/catalog/product/fluka/87708","pv":119,"lc":{"d0":{"v":119,"s":true}},"cd":0,"f":1427812524452,"sd":0}; fsr.a=1427812533888',
'RA-Ver': '2.9.0',
'RA-Sid': '3A65D2DE-20140808-051402-1053d8-0c4bf5'
}

# cookies = {
#     'JSESSIONID': '57F5320EB3E12CCBC1EEE5604531AC63.stltcat01b',
#     'country': 'CHIM',
#     'SialLocaleDef': 'CountryCode~CN | WebLang~-7 |',
#     'fsr.r': '{"d": 30, "i": "de35431-94629287-8bc3-f1b6-553fd", "e": 1426517396463}',
#     'TLTSID': '3941AC5CCEAB10CE0357F15351D5A5DE',
#     'TLTUID': '3941AC5CCEAB10CE0357F15351D5A5DE',
#     'cmTPSet': 'Y',
#     'SessionPersistence': 'CLICKSTREAMCLOUD % 3A % 3DvisitorId % 3Danonymous % 7CPROFILEDATA % 3A % 3Davatar % 3D % 2Fetc % 2Fdesigns % 2Fdefault % 2Fimages % 2Fcollab % 2Favatar.png % 2CisLoggedIn % 3Dtrue % 2CisLoggedIn_xss % 3Dtrue % 2CauthorizableId % 3Danonymous % 2CauthorizableId_xss % 3Danonymous % 2CformattedName % 3D % 2CformattedName_xss % 3D % 7CSURFERINFO % 3A % 3DIP % 3D141.247.239.190 % 2Ckeywords % 3D % 2Cbrowser % 3DChrome % 2COS % 3DMac % 20OS % 20X % 2Cresolution % 3D1280x800 % 7C',
#     '__unam': '40e1073 - 14bfea75e24 - 15d68ec8 - 297',
#     'GUID': '5c066db5 - 8327 - 4173 - 89ed - 9913c8416174 | NULL | 1427738534996;_ga = GA1.2.1911851944.1425866637',
#     'Cck': 'present',
#     'fsr.s': '{"cp": {"REGION": "Europe", "ClientId": "Unknown", "MemberId": "Unknown", "SiteId": "SA","TLTSID": "3941AC5CCEAB10CE0357F15351D5A5DE", "TLTUID": "3941AC5CCEAB10CE0357F15351D5A5DE","GUID": "5c066db5-8327-4173-89ed-9913c8416174|NULL|1427738534996"}, "v": -1,"rid": "de358f8-93429366-4aea-1971-5f2f5", "to": 5,"c": "http://www.sigmaaldrich.com/catalog/product/fluka/87708", "pv": 119, "lc": {"d0": {"v": 119, "s": true}},"cd": 0, "f": 1427812524452, "sd": 0}',
#     'fsr.a': '1427812533888'
# }

# data = {'loadFor': 'PRD_RS'}
# res = requests.post('http://www.sigmaaldrich.com/catalog/PricingAvailability.do?divId=pricingContainerMessage&brandKey=Sigma&productNumber=A9949', headers=headers, data=data)
# print dir(res)
# print res.content
# print res.text
# print res.status_code

from mongodb import db
from sigma_product_detail import ProductDetail

p = ProductDetail(db_price=db.test_price, db_detail=db.test_detail)
p.get_base_info('http://www.sigmaaldrich.com/catalog/product/aldrich/452238?lang=zh&region=CN')