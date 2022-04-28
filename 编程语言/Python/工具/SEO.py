from unittest import result
import requests
from lxml import etree
import time

url = "https://trends.chinaz.com/ranklist/baidupc/20220428-1-"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Cookie": "cz_statistics_visitor=962d164b-b790-099a-c3d5-a669a5b71244; UM_distinctid=18018fbdecf341-082a96fbf8631f-a3e3164-144000-18018fbded123; toolbox_urls=129.211.73.13|www.weiboreach.com; auth-token=c9780ac7-819c-41ef-8b19-6bebcb2aba8d; user-temp=85f486e8-5b1f-c8dc-61f6-6bf9c5763bef; __gads=ID=b7d1418f0c405b2f-22d68abc5cd20044:T=1650546772:RT=1650546772:S=ALNI_Mb3ZCNHMn6r5b23MGGMobyC46FHgQ; chinaz_topuser=6a73bf44-f0e9-a791-cdf4-c761e6085f7a; qHistory=aHR0cDovL3RyZW5kcy5jaGluYXouY29tL3JhbmsvdHJlbmQuYXNweF/mlbDmja7lhoXlj4J8aHR0cDovL3Nlby5jaGluYXouY29tX1NFT+e7vOWQiOafpeivonxodHRwOi8vdHJlbmRzLmNoaW5hei5jb20vcmFua2xpc3QvX+aVsOaNruWGheWPgnxodHRwOi8vdG9vbC5jaGluYXouY29tL3Rvb2xzL2R3ei5hc3B4X+efremTvueUn+aIkHxodHRwOi8vd2hvaXMuY2hpbmF6LmNvbS9fV2hvaXPmn6Xor6J8aHR0cDovL3Rvb2wuY2hpbmF6LmNvbS90b29scy91cmxlbmNvZGUuYXNweF9VcmxFbmNvZGXnvJbnoIEv6Kej56CBfGhleC9fSGV457yW56CBL0hleOino+eggXxodHRwOi8vdG9vbC5jaGluYXouY29tL3Rvb2xzL25hdGl2ZV9hc2NpaS5hc3B4X05BVElWRS9BU0NJSee8lueggeS6kui9rHxodHRwOi8vcmFuay5jaGluYXouY29tX+e7vOWQiOadg+mHjeafpeivonxodHRwOi8vdG9vbC5jaGluYXouY29tL3Rvb2xzL3VuaWNvZGUuYXNweF9Vbmljb2Rl57yW56CB6L2s5o2i; __gpi=UID=0000050d80a12c00:T=1651058430:RT=1651058430:S=ALNI_MYDUd36a7z6PxStAZJFLp1ozrwQDw; Hm_lvt_ca96c3507ee04e182fb6d097cb2a1a4c=1650546677,1650616391,1651038223,1651158859; CNZZDATA5082706=cnzz_eid%3D998368790-1650545730-null%26ntime%3D1651149568; ucvalidate=8c5a7eb1-43f0-dd67-f17b-5c4d6fb67ace; bbsmax_user=d22e9c1f-31e1-c484-0834-4c276098260a; Hm_lpvt_ca96c3507ee04e182fb6d097cb2a1a4c=1651159248"
}

for i in range(10,50):
    i = str(i)
    newUrl = url + i
    request = requests.get(newUrl,headers=headers).text
    response = etree.HTML(request)
    result = response.xpath('//div[@class="col-4 tl"]/a/text()')
    for j in result:
        print(j)
    
    time.sleep(2)
    