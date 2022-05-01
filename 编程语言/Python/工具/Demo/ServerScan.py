import sys
import requests

url = sys.argv[1]
request = requests.get(url)
script = 'X-Powered-By'
server = 'Server'

# print(request.headers)
if server in request.headers: 
    print("中间件: " + request.headers['Server'])
else:
    print("中间件：" + "")
if script in request.headers:
    print("脚本语言: " + request.headers['X-Powered-By'])
else:
    print("脚本语言: " + "")