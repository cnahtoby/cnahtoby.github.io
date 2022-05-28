## 一、介绍

### 1、简介

```php
	OpenSSL是一个安全套接字层密码库，囊括主要的密码算法、常用密钥、证书封装管理功能及实现ssh协议。可以实现：密钥密钥证书管理、对称加密和非对称加密。
```

### 2、端口号

```
	443
```

### 3、Logo

![img](https://www.bing.com/th?id=ODL.ffd13d6033dc0744f4e60b27d11bcb05&w=100&h=100&c=12&pcl=faf9f7&o=6&dpr=1.25&pid=13.1)

### 4、开发语言

```
	C	
```

### 5、默认密码

```
	无
```



## 二、历史漏洞

### 1、OpenSSL 心脏出血

### 2、OpenSSL无限循环DOS



## 三、利用工具

### 1、ssltest.py

```php
# 下载地址
	https://github.com/vulhub/vulhub/blob/master/openssl/CVE-2014-0160/ssltest.py
```

### 2、Metaspolit

```php
# 下载地址
	https://github.com/rapid7/metasploit-framework
```





## 四、漏洞分析

### 1、OpenSSL 心脏出血

```php
# CVE编号
	CVE-2014-0160
```

```php
# 版本
	OpenSSL1.0.1
```

```php
# 原理
	Heartbleed漏洞，这项严重缺陷的产生是由于未能在memcpy()调用受害用户输入内容作为长度参数之前正确进行边界检查。攻击者可以追踪OpenSSL所分配的64KB缓存、将超出必要范围的字节信息复制到缓存当中再返回缓存内容，这样一来受害者的内存内容就会以每次64KB的速度进行泄露。
```

### 2、OpenSSL无限循环DOS

```php
# CVE编号
	CVE-2022-0778
```

```php
# 版本
	OpenSSL == 1.0.2
	OpenSSL == 1.1.1
	OpenSSL == 3.0
```

```php
# 原理
	该版本OpenSSL存在一处逻辑缺陷，攻击者可以利用一个无效的椭圆曲线参数证书，触发一个无限循环导致耗尽目标CPU。由于证书解析发生在验证证书签名之前，任何解析外部提供的证书的进程都可能受到拒绝服务的攻击。
```

