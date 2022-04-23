## 一、基本库

### 1、urllib

​	1.1、request -- HTTP请求模块

- 基础用法

```python
urlopen()	//模拟浏览器发起请求
//用法
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

data参数		//
timeout参数	//设置超时时间
```

```python
Request()	//给请求添加参数
//用法
import urllib.request
request = urllib.request.Request('http://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

class urllib. request. Request ( url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)		//参数合集
```

- 高级用法

​	1.2、error -- 异常处理模块

```python
URLError	//处理request模块生成的错误
//reason返回错误原因
//用法
from urllib import request,error
try:
	response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
	print(e.reason)
```

```python
HTTPError	//处理HTTP请求错误，是URLError的子类
//reason返回错误原因，code返回状态码，headers返回请求头
//用法
from urllib import request,error
try:
	response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print(e.reason,e.code,e.headers,seq='\n')
```

​	1.3、parse -- 工具模块

```python
urlparse	//URL识别和分段
//用法
from urllib.parse import urlparse

result = urlopen('http://www.baidu.com/index.html;user?id=5#comment')
print(typr(result),result)
```

```python
urlunparse	//URL构造
//用法
from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))
```

```python
quote()		//将内容进行URL编码
//用法
from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
```

```python
unquote()	//将内容进行URL解码
//用法
from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
```

​	1.4、Robots协议

- 解释
  - Robots协议也称爬虫协议、机器人协议，全称为网络爬虫排除标准（Robots Exclusion Protocol），用来告诉爬虫和搜索引擎哪些页面可以爬取，哪些不可以爬取
- robots.txt文件

```python
User-agent: *		//对所有的User-agent有效
Disallow: /			//禁止访问的目录
Allow: /tmp			//可以访问的目录
```

- robotparser

```python
set_url()		//设置robots.txt文件的链接
read()			//读取robots.txt并分析
parse()			//解析robots.txt
can_fetch([UA],[URL])//检查该搜索引擎是否可以爬取该URL
mtime			//返回上次爬取和分析robots.txt时间
modified()		//将当前时间设置为上次抓取和分析robots.txt时间
//用法
from urllib.robotparser import RobotFileParser

rp = RobotFileParser('http://www.jianshu.com/robots.txt')	//爬取robots.txt
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))//检查是否可爬
print(rp.can_fetch('*',"http://www.jianshu.com/search?q=python&page=l&type=collections"))
```

### 2、requests

​	2.1、基础用法

```python
requests.get()			//get请求，等同于urllib.openurl()
//用法
import requests
x = requests.get('http://httpbin.org/get')
print(x.text)

//参数
params = [参数字典]		//在url中加入参数
print(x.json())			//将json格式打印成字典

//获取二进制数据
import requests
x = requests.get("https://github.com/favicon.ico")
with open('favicon.ico','wb') as f:
    f.write(x.content)
```

```python
requests.post()			//post请求
//用法
import requests
data = {'name':'tom','age':'22'}
x = requests.post{"http://httpbin.org/post",data=data}
print(x.text)
```

```python
#接收响应
x.code			#状态码
x.headers		#响应头
x.cookies		#cooikes
x.url		    #url
x.history		#请求历史
```

​	2.2、高级用法

```python
# 文件上传
import requests

files = {'file' : open('favicon.ico','rb')}
x = requests.post("http://httpbin.org/post",files=files)
print(x.text)

# Cookies获取
import requests

x = requests.get("https://www.baidu.com")
for key,value in x.cookies.items():
    print(key + '=' + value)
    
# Cookies维持登录
import requests

headers = {
    'Cookie': '[登录时的Cookie]',
    'Host': 'www.zhihu.com',
    'User-Agent':'[UA头]'
}
x = requests.get('https://www.zhihu.com',headers=headers)
print(x.text)

# Seesion会话维持
import requests

x = requests.Session()
x.get('http://httpbin.org/cookies/set/number/123456789')
y = x.get('http://httpbin.org/cookies')
print(y.text)

# proxies代理设置
# pip3 install 'requests[socks]'
import requests

proxies = {
    "http": "socks5://user:password@host:port",
    "https": "socks5://user:password@host:port",
}
requests.get("https://www.taobao.com",proxies=proxies)

# timeout超时设置
import requests

x = requests.get("https://www.taobao.com",timeout = 1)
print(x.status_code)

# HTTPBasicAuth身份认证
import requests
from requests.auth import HTTPBasicAuth

x = requests.get('http://host:port', auth=HTTPBasicAuth('username','password'))
print(x.status_code)	#HTTPBasicAuth也可以不写
```

### 3、re

```python
# 修饰符
re.I	# 大小写不敏感	
re.M	# 多行匹配
re.S	# 使.匹配包括换行在内的所有字符
re.U	# 根据Unicode字符集解析字符
```

```python
# match() -- 需要以指定字符开头进行匹配，用于检测某个字符串是否符合规则
# 格式：re.match([正则表达式],[字符串])
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(l))
```

```python
# search() -- 扫描全文，返回第一个成功匹配的结果
# 格式：re.search([正则表达式],[字符串],re.S)	re.S匹配换行符
import re

result = re.search('<li.*?href="(.*?)".*?singer="(.*?)"</a>',html,re.S)
if result:
    print(result.group(1), result.group(2))
```

```python
# findall() -- 扫描全文，返回所有成功匹配的内容，并保存为元组列表，使用索引提取
# 格式：re.findall([正则表达式],[字符串],re.S)
import re

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)"</a>',html,re.S)
print(results)		    # 打印全部结果
print(type(results))	# 打印类型（列表）
for result in results:	
    print(result)		# 打印字典
    print(result[0],result[1],result[2])	# 打印字典中指定内容
```

```python
# sub() -- 修改指定字符串
# 格式：re.sub([正则表达式],[替换后],[字符串])
import re

content = "54aK54yr5oiRS4ixSL2g"
content = re.sub('\d+','',content)
print(content)
```

```python
# compile() -- 将正则字符串编译成正则表达式的规则对象，方便复用
import re
content1 = '2016-12-15 12:00'
content2 = '2022-04-03 14:00'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
print(result1,result2)
```



## 二、解析库

### 1、XPATH

​	1.1、介绍

- XML Path Language，起初用于搜索XML，同样适用于HTML。提供了非常简洁明了的路径选择表达式，几乎所有想要定位的节点，都可以用XPATH选择

​	1.2、常用规则

```python
nodename		# 选取此节点的所有子节点
/				# 从当前节点选取直接子节点
//				# 从当前节点选取子孙节点
.				# 选取当前节点
..				# 选取当前节点的父节点
@				# 选取属性

from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)		# tostring()输出修正后的HTML代码，bytes类型
print(result.decode('utf-8'))		# 使用decode('utf-8')转换成str类型
```

​	1.3、所有节点

```python
# //
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li')	 # 选取当前节点的子孙节点中所有li节点
print(result)
print(result[0])			# 选取子节点的第一个
```

​	1.4、子节点

```python
# /
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//ul//a')
print(result)
```

​	1.5、父节点

```python
# ../ 
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
```

​	1.6、属性匹配

```python
# @class=""

from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)
```

​	1.7、文本读取

```python
# /text()
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
```

​	1.8、属性读取

```python
# @href
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
```

​	1.9、属性多值匹配

```python
from lxml import etree
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)
```

​	1.10、多属性匹配

```python
# 运算符
or		# 或
and		# 与
mod		# 计算除法的余数
|		# 计算两个节点集
+		# 加法
-		# 减法
*		# 乘法
div		# 除法
=		# 等于
!=		# 不等于
<		# 小于
>		# 大于

from lxml imprt etree
html = etree.HTML([HTML文本])	# 使用etree.HTML将HTML文本转换为Elment对象
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')	# 使用对象.xptah提取关键信息
print(result)
```

### 2、Beautiful Soup

​	2.1、介绍

- Beautiful Soup是Python的一个HTML和XML的解析库，可以方便地从网页上爬取数据

​	2.2、准备

- 安装Beautiful Soup和lxml

​	2.3、解析器

```python
BeatifulSoup([文本],"html.parser")	# Python标准库
BeatifulSoup([文本],"lxml")		    # lxml HTML解析器
BeatifulSoup([文本],"xml")		    # lxml XML解析器
BeatifulSoup([文本],"html5lib")		# html5lib
```

​	2.4、基础用法

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())				# 以标准的缩进格式输出
print(soup.title.string)			# 输出title节点中的string属性的内容
```

​	2.5、节点选择器

```python
# 选择元素
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
```

```python
# 提取信息
# 1、获取名称
print(soup.title.name)

# 2、获取属性
print(soup.p.attrs)				# 返回字典形式
print(soup.p.attrs['name'])		 # 提取字典中的指定属性
print(soup.p['name'])			# 简化版
print(soup.p['class'])			# 简化版	

# 3、获取内容
print(soup.p.string)			
```

```python
# 嵌套选择
from bs4 import BeautifulSoup
soup = BeautifulSouop(html,'lxml')
print(soup.head.title)
print(soup.head.title.string)
```

```python
# 关联选择
# 1、contents子节点和 children子孙节点
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
for i,child in enumerate(soup.p.children):
    print(i,child)

for i,child in enumerate(soup.p.descendants):
    print(i,child)
    
# 2、parent父节点和 parents祖先节点
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.a.parent)

print(list(enumerate(soup.a.parents)))

# 3、next_sibling下一个节点 和 previous_sibling上一个节点
print('Next Sibling',soup.a.next_sibling)
print('Prev Sibling',soup.a.Prev_sibling)

# 4、提取信息
print(type(soup.a.next_sibling))	# 提取下一个节点的类型
print(soup.a.next_sibling)			# 提取下一个节点的内容
print(soup.a.next_sibling.string)	# 提取下一个节点的文本内容
print(type(soup.a.parents))			# 提取祖先节点的类型
print(soup.a.parents)[0]			# 提取祖先节点的第一个节点内容
print(list(soup.a.parents)[0].attrs['class'])	# 提取祖先节点的第一个节点属性
print(list(soup.a.parents)[0].string) # 提取祖先节点的一个节点内容
```

​	2.6、方法选择器

```python
# find_all()  查询所有符合条件的元素
# 格式：find_all(name , attrs , recursive , text , **kwargs)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))

# 遍历打印内容
for ul in soup.find_all(name='ul'):
    for li in soup.find_all(name='li'):
        print(li.string)
```

```python
# find()  查询第一个符合条件的元素
soup = BeautifulSoup(html,'lxml')
print(soup.find(name='ul'))
print(soup.find(clss_='list'))
```

### 3、Pyquery

​	3.1、初始化

```python
# 字符串初始化
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))
```

```python
# URL初始化
from pyquery import PyQuery as pq
doc = pq(url='https://cuiqingcai.com'.text
print(doc('title'))
```

```python
# 文件初始化
from pyquery import PyQuery as pq
doc = pq(filename='demo.html')
print(doc('li'))
```

​	3.2、基础CSS选择器

```python
from pyquery import PyQuery as gg
doc = gg(html)
print(doc('#container .list li'))
```

​	3.3、查找节点

```python
# 子节点 children()
from pyquery import PyQuery as gg
doc = gg(html)
items = doc('.list')
print(items)
lis = items.find('li')
print(lis)
```

```python
# 父节点 parent()	parents()
```

```python
# 兄弟节点 siblings()
from pyquery import PyQuery as gg
doc = gg(html)
li = doc('.list .item-0.active')
print(li.siblings())
```

​	3.4、遍历

```python
from pyquery import PyQuery as gg
doc = gg(html)
lis = doc('li').items()
for li in lis:
    print(li,type(li))
```

​	3.5、获取信息

```python
# 获取属性
from pyquery import PyQuery as gg
doc = gg(html)
a = doc('.item-0.active a')
print(a.attr('href'))
```

```python
# 获取文本
from pyquery import PyQuery as gg
doc = gg(html)
a = doc('.item-0.active a')
print(a.text())
```

​	3.6、节点操作

```python
# addClass & removeClass
from pyquery import PyQuery as gg
doc = gg(html)
li = doc('.item-0.active')
li.removeClass('active')
print(li)
li.addClass('active')
print(li)
```

```python
# attr & text & html
from pyquery import PyQuery as gg
doc = gg(html)
li = doc('item-0.active')
li.attr('name','link')
li.text('hello')
li.html('<span>Hello!</span>')
```



## 三、文件存储

### 	1、TXT

```python
# 实例
使用requests获取源码，pyquery解析提取，保存到文本
```

```python
# 打开方式
r	只读
rb	二进制只读
r+	读写
rb+	二进制读写
w	写
wb	二进制写入。存在则写入，不存在则创建
w+	读写
wb+	二进制读写。存在则写入，不存在则创建
a	追加
ab	二进制追加
a+	读写。文件指针在结尾，不存在则追加
ab+	二进制追加。文件指针在结尾，不存在则追加
```

```python
# 简写
with open('explore.txt','a',encoding='utf-8') as file:
	file.write('\n'.join([question,author,answer]))
	file.write('\n' + '=' * 50 + '\n')
```

### 	1、JSON

```python
# 对象和数组
对象：使用花括号{}包裹起来，数据结构为{key1:value1,key2:value2,...}的键值对结构
数组：使用方括号[]包裹起来，数据结构为{'aa','bb','cc'...}的索引结构
```

```python
# 读取JSON
import json
print(type(str))
data = json.loads(str)	# loads()转文本为json
print(data)
```

```PYTHON
# 输出JSON
import json
data = [{
	'name':'Tom',
	'gender':'male',
	'birthday':'1992-10-10'
}]
with open('data.json','w') as file:
	file.write(json.dumps(data))
```

### 	3、CSV

```
# 介绍
CSV(Comma-Separated Values)，逗号分隔值/字符分隔值，其文件以纯文本形式存储表格数据。
```

```python
# 写入

# 1、基本写入
import csv
with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['101','Tom','18'])
    writer.writerow(['102','Jerry','19'])
    writer.writerow(['103','Bob','20'])   
# 2、中文编码
import csv
with open('data.csv','a',encoding='utf-8') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({'id':'104','name':'王伟','age':22})
```

```python
# 读取
import csv
with open('data.csv','r',encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```
