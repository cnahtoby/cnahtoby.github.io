## 一、介绍

### 1、简介

```
	Nexus Repository Manager 3是一款软件仓库，可以用来存储和分发Maven、NuGET等软件源仓库。
```

### 2、端口

```
	8081
```

### 3、Logo

![See the source image](https://th.bing.com/th/id/OIP.A7aXBUtJZ2kiuztZVDFTGgHaHa?pid=ImgDet&rs=1)

### 4、开发语言

```
	Java
```

### 5、默认密码

```php
	Nexus 3.17之前：admin/admin123
```



## 二、历史漏洞

### 1、Nexus Repository Manager 3远程命令执行

### 2、Nexus Repository Manager 3远程命令执行2

### 3、Nexus Repository Manager 3远程命令执行3



## 三、利用工具



## 四、漏洞分析

### 1、Nexus Repository Manager 3远程命令执行

```php
# CVE编号
	CVE-2019-7238
```

```php
# 版本
	Nexus Repository Manager OSS/Pro 3.6.2-3.14.0
```

```php
# 原理
	其3.14.0及之前版本中，存在一处基于OrientDB自定义函数的任意JEXL表达式执行功能，而这处功能存在未授权访问漏洞，导致了任意命令执行漏洞。
```

### 2、Nexus Repository Manager 3远程命令执行2

```php
# CVE编号
	CVE-2020-10199
```

```php
# 版本
	Nexus Repository Manager OSS/Pro 3.x <= 3.21.1
```

```php
# 原理
	在其3.21.1及之前版本中，存在移除任意EL表达式注入漏洞。
```

### 3、Nexus Repository Manager 3远程命令执行3

```php
# CVE编号
	CVE-2020-10204
```

```php
# 版本
	Nexus Repository Manager OSS/Pro 3.x <= 3.21.1
```

```php
# 原理
	在其3.21.1及之前版本中，存在移除任意EL表达式注入漏洞，这个漏洞是CVE-2018-16621的绕过。
```

