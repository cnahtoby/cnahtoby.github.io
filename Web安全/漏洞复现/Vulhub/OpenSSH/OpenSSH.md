## 一、介绍

### 1、简介

```php
	OpenSSH是SSH协议的免费开源实现。SSH协议族可以用来进行远程控制，或在计算机之间传送文件。
```

### 2、端口

```
	22
```

### 3、Logo

![[OpenSSH]](https://www.openssh.com/images/openssh.gif)

### 4、开发语言

```
	C++
```

### 5、默认密码

```
	无
```



## 二、历史漏洞

### 1、OpenSSH用户名枚举



## 三、利用工具

### 1、POC脚本

```php
# 下载地址
	https://github.com/Rhynorater/CVE-2018-15473-Exploit
```



## 四、漏洞分析

### 1、OpenSSH用户名枚举

```php
# CVE编号
	CVE-2018-15473
```

```php
# 版本
	OpenSSH >= 2.3 && <= 7.7
```

```php
# 原理
	该漏洞源于程序会对有效的和无效的用户身份呢验证请求发出不同的响应。攻击者可通过发送特制的请求利用该漏洞枚举用户名称。
```

