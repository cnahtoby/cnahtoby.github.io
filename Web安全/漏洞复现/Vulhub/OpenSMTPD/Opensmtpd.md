## 一、介绍

### 1、简介

```php
	OpenSMTPD是面向unix操作系统（BSD、MacOS、GNU/Linux）的一个smtp服务程序，遵循RFC 5321 SMTP协议，OpenSMTP最初为OpenBSD操作系统开发的，是OpenBSD项目的一部分，由于其开源的特性，进而分发到其他UNIX平台。根据ISC许可，该软件可免费供所有人使用和重用。
```

### 2、端口

```
	8825
```

### 3、Logo

![img](https://www.opensmtpd.org/images/opensmtpd.png)

### 4、开发语言

```
	C++
```

### 5、默认密码

```
	无
```



## 二、历史漏洞

### 1、OpenSMTPD 远程命令执行



## 三、利用工具

### 1、POC脚本

```php
# 下载地址
	https://www.exploit-db.com/exploits/47984
```



## 四、漏洞分析

### 1、OpenSMTPD 远程命令执行

```PHP
# CVE编号
	CVE-2020-7247
```

```PHP
# 版本
	OpenSMTPD 6.6
```

```php
# 原理
	OpenSMTPD 6.6版本中的smtp_session.c文件的smtp_mailaddr函数存在安全漏洞，在实现RFC 5321的过程中对 发件人/收件人 收件人校验不严而导致的，远程攻击者可通过特制的SMTP session利用该漏洞以root权限执行任意命令。
```

