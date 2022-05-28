## 一、介绍

### 1、简介

```php
	Apache OfBiz是一个非常著名的开源电子商务平台，提供了创建基于最近J2EE/XML规范的技术标准，构建大中型企业、跨平台、跨数据库、跨应用服务器的多层、分布式电子商务类WEB应用程序的组件和工具。包括实体引擎、服务引擎、消息引擎、工作流引擎、规则引擎等。
```

### 2、端口

```
	8080
	8443
```

### 3、Logo

![img](https://ofbiz.apache.org/images/ofbiz_logo.png)

### 4、开发语言

```
	Java
```

### 5、默认密码

```
	admin/ofbiz
```



## 二、历史漏洞

### 1、Apache OfBiz反序列化命令执行



## 三、利用工具

### 1、ysoserial

```php
# 下载地址
	https://github.com/frohoff/ysoserial
```



## 四、漏洞分析

### 1、Apache OfBiz反序列化命令执行

```php
# CVE编号
	CVE-2020-9496
```

```php
# 版本
	Apache OfBiz < 17.12.04
```

```php
# 原理
	其17.12.04版本之前的XMLRPC接口存在一处反序列化漏洞，攻击者利用这个漏洞可以再目标服务器上执行任意命令
```

