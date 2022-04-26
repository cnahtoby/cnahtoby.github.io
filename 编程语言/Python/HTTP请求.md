### 1、GET

#### 	1.1、不带参数

```python
import requests

url = "http://www.baidu.com"
request = requests.get(url)
```

#### 	1.2、带参数

```python
import requests

url = "http://www.baidu.com"
params = {username = "xxx",password = "xxx"}
request = requests.get(url,params = params)
```



### 2、POST

#### 	2.1、不带参数

```python
import requests

url = "http://www.baidu.com"
request = requests.post(url)
```

#### 	2.2、带参数

```python
import requests

url = "http://www.baidu.com"
data = {username = "xxx",password = "xxx"}
request = requests.post(url,data = data)
```



### 3、自定义请求头

```python
import requests

url = "http://www.baidu.com"
headers = {UserAgent: "xxx"}
request = requests.get(url,headers = headers)
```



### 4、其他请求

```python
import requests

data = {'key':'value'}
request = request.put('http://www.baidu.com/put',data = data)
request = request.delete('http://www.baidu.com/delete',data = data)
request = request.head('http://www.baidu.com/get',data = data)
request = request.options('http://www.baidu.com/get',data = data)
```

