## 一、介绍

### 1、简介

```php
	Metasploit Framework(MSF)是一款开源安全漏洞检测工具，附带了数千个已知的软件漏洞，并保持持续更新。Metasploit可用来信息收集、漏洞检测、漏洞利用等渗透测试的全流程，被安全社区冠以"可以黑掉整个宇宙"之名。
```

### 2、下载地址

```php
	https://github.com/rapid7/metasploit-framework
```



## 二、实战基本流程

### 1、nmap端口扫描

```php
	nmap -sV [ip]		# 服务版本检测
```

### 2、search查找相关模块

```php
	search [指定服务]	
```

### 3、use使用模块

```
	use [索引号]
```

### 4、info查看模块信息

```
	info
```

### 5、选择payload

```
	show payloads
	set payload [payload]
```

### 6、设置攻击参数

```
	show options
	set [参数] [值]
```

### 7、渗透攻击

```
	exploit		# 或者使用run
```