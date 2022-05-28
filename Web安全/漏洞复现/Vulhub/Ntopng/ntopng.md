## 一、介绍

### 1、简介

```php
	ntopng是监控服务器网络流量的工具，对外提供web页面。
```

### 2、端口

```
	3000
```

### 3、Logo

![See the source image](https://th.bing.com/th/id/R.84f4cdb5e749495241cdcd3ceea195a7?rik=4f2KKlQOaJS9qA&pid=ImgRaw&r=0)

### 4、开发语言

```
	Web：Lua
	后端：C++
```

### 5、默认密码

```php
	admin/admin
	第一次登录进系统后需要改密码
```





## 二、历史漏洞

### 1、ntopng权限绕过



## 三、利用工具



## 四、漏洞原理

### 1、ntopng权限绕过

```php
# CVE编号
	CVE-2021-28073
```

```php
# 版本
	ntopng <= 4.2
```

```php
# 漏洞原理
	Ntopng对外提供Web页面，其4.2及其以前版本Web接口的权限认证绕过，导致攻击者可以在未授权的情况下请求符合漏洞利用条件的接口，并最终利用服务器端请求伪造和高危服务实现远程代码执行。
```

