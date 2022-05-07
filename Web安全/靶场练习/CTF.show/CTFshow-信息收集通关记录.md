## 1、查看源码



## 2、查看源码View-source



## 3、查看Response



## 4、Robots.txt

```php
# Payload
/Robots.txt
/flagishere.txt
```



## 5、PHP Source

```php
# Payload
/index.phps
```



## 6、www.zip

```php
# Payload
/www.zip
```



## 7、.git

```php
# Payload
/.git/index.php
```



## 8、.svn

```php
# Payload
/.svn/index.php
```



## 9、.swp

```php
# Payload
/index.php.swp
```



## 10、抓包Cookie



## 11、域名解析记录

```php
# 思路
1、访问http://www.jsons.cn/nslookup/
2、输入ctfshow.com
3、查看TXT记录（目前已被删除），里面存有主机名/域名设置的说明
```



## 12、页面敏感词

```php
# Payload
/robots.txt
/admin/
账号：admin
密码：372619038
```



## 13、技术文档

```php
# 思路
1、点击主页下方的document，跳转到产品说明页面
2、发现默认密码和登录接口
3、访问登录接口，输入默认密码
```

```php
# Payload
/document.pdf
/system1103/login.php
	用户名：admin
	密码：admin1103
```



## 14、editor

```php
# 思路
1、访问/editor目录
2、点击添加图片功能
3、在访问空间里找到/var/www/html/nothinghere/fl00g.txt
4、访问/nothinghere/fl00g.txt
```

```php
# Payload
/nothinghere/fl000g.txt
```



## 15、社工

```php
# 思路
1、首页找到联系方式1156631961@qq.com
2、访问登录点/admin
3、点击忘记密码，提示验证所在城市
4、通过QQ查找好友，确定该用户所在地为西安
5、填写西安，获得密码admin7789
6、用户名：admin，密码：admin7789登录，获得flag
```

```php
# Payload
/admin
	账号：admin
	密码：admin7789
```



## 16、php探针

```php
# 思路
1、访问tz.php
2、找到并点击phpinfo
3、phpinfo界面有flag
```

```php
# Payload
/tz.php
/tz.php?act=phpinfo
```



## 17、backup.sql

```php
# Payload
/backup.sql
```



## 18、JS文件提示

```php
# 思路
1、查看源代码
2、点击并跳转JS文件
3、查看底部的unicode编码字符：\u4f60\u8d62\u4e86\uff0c\u53bb\u5e7a\u5e7a\u96f6\u70b9\u76ae\u7231\u5403\u76ae\u770b\u770b
4、解码后发现为提示110.php
5、访问110.php获取flag
```

```php
# Payload
/110.php
```



## 19、JS文件密码

```php
# 思路
1、查看源代码
2、发现接收POST传输的账号和密码
3、输入任意用户名密码，点击提交
4、Burp抓包修改正确的用户名和密码，得到flag
```



## 20、db.mdb

```php
# Payload
/db/db.mdb
```



## N、知识点

### 1、Robots.txt

```php
# 解释
	该文件中为针对爬虫权限设置的配置文件，里面可能存在程序员设置的敏感目录
```

### 2、editor

```php
# 解释
	通过该编辑器的添加图片功能，尝试访问网站内部文件
```

### 3、db.mdb

```php
# 解释
	db.mdb是早期asp + access结构的数据库文件，直接在url后添加/db/db.mdb即可下载该文件
```

