### 1、介绍

```
# 携带Cookie的会话
访问某些网页时，会通过Set-Cookie设置Cookie值，以使下一次访问自动提交Cookie进行身份验证。
```



### 2、Python-Session

```python
session = requests.Session()	# 设置session属性
request = request.get(url)		# 携带sessions
```

