## 一、介绍

### 1、简介

```php
	PostgreSQL是一个功能非常强大的、源代码开放的客户/服务器关系型数据库（RDBMS）。PostgreSQL最初设想下1986年，当时被叫做Berkley Postgres Project。
```

### 2、端口

```
	5432
```

### 3、Logo

![Image result for PostgreSQL Icon](https://th.bing.com/th/id/OIP.CG8qTeTuoei796LdScT2bwHaIP?w=157&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7)

### 4、开发语言

```
	C
```

### 5、默认密码

```
	postgres/空
```



## 二、历史漏洞

### 1、PostgreSQL提权

### 2、PostgreSQL高权限命令执行



## 三、利用工具

```
	无
```



## 四、漏洞分析

### 1、PostgreSQL提权

```php
# CVE编号
	CVE-2018-1058
```

```php
# 版本
	PostgreSQL 9.3 ~ 10
```

```php
# 原理
	该版本范围中存在一个逻辑错误，导致超级用户在不知情的情况下触发普通用户创建的恶意代码，导致执行一些不可预期的操作。
```

### 2、PostgreSQL高权限命令执行

```php
# CVE编号
	CVE-2019-9193
```

```php
# 版本
	PostgreSQL 9.3 ~ 11
```

```php
# 原理
	该版本范围中存在一处"特性"，管理员或具有"COPY TO/FROM PROGRAM"权限的用户，可以使用这个特性执行任意命令。
```

