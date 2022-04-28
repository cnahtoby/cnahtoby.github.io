import requests
import sys
import time

url = sys.argv[1]
dir = sys.argv[2]
with open(dir,"r") as f:
    for line in f.readlines():
        line =line.strip()
        request = requests.get(url + line)
        if request.status_code == 200:
            print(request.url + " 存在！")
            
            time.sleep(1)