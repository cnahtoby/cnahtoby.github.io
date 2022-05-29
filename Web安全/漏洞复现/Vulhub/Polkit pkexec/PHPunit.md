## 一、介绍

### 1、简介

```php
	phpunit是php轻量级的单元测试框架，只需要编写好单元测试代码，运行即可测试结果是否和预期结果一样，如果不一样则会报错。
```

### 2、端口

```
	无
```

### 3、Logo

![PHPUnit](https://phpunit.de/img/phpunit.svg)

### 4、开发语言

```
	PHP
```

### 5、默认密码

```
	无	
```



## 二、历史漏洞

### 1、phpunit 远程代码执行



## 三、利用工具

```
	w
```



## 四、漏洞分析

### 1、phpunit 远程代码执行

```php
# CVE编号
	CVE-2017-9841
```

```php
# 版本
	phpunit 4.8.19~4.8.27
	phpunit 5.0.10~5.6.2
```

```php
# 原理
	其4.8.19 ~ 4.8.27和5.0.10 ~ 5.6.2版本的vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php 文件有如下代码：eval('?>'.file_get_contents('php://input'));如果该文件被用户直接访问到，可造成远程代码执行。
```

