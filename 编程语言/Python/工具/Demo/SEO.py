import requests
from lxml import etree
import time

url = "https://trends.chinaz.com/ranklist/baidupc/20220428-1-"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Cookie": "输入自己的Cookie"
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
    