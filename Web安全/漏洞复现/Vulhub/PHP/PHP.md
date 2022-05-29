## 一、介绍

### 1、简介

```php
	PHP（Hypertext Preprocessor）即"超文本预处理器"，是在服务器端执行的脚本语言，尤其适用于Web开发并可嵌入HTML中。
```

### 2、端口

```
	无
```

### 3、Logo

![PHP logo](https://www.php.net//images/logos/new-php-logo.svg)

### 4、开发语言

```
	PHP
```

### 5、默认密码

```
	w
```



## 二、历史漏洞

### 1、PHP 8.1.0-dev 开发版本后门事件

### 2、PHP-CGI远程代码执行

### 3、PHP-FPM远程代码执行

### 4、PHP-FPM Fastcgi未授权访问

### 5、PHP文件包含

### 6、PHP XML实体注入

### 7、XDebug远程调试



## 三、利用工具

### 1、PHP-FPM Fastcgi未授权访问 EXP

```php
# 下载地址
	https://gist.github.com/phith0n/9615e2420f31048f7e30f3937356cf75
```



## 四、漏洞分析

### 1、PHP 8.1.0-dev 开发版本后门事件

```php
# CVE编号
	无
```

```php
# 版本
	8.1.0
```

```php
# 原理
	PHP 8.1.0-dev 版本在2021年3月28日被植入后门，但是后门很快被发现并清除。当服务器存在该后门时，攻击者可以通过发送User-Agentt头来执行任意代码。
```

### 2、PHP-CGI远程代码执行

```php
# CVE编号
	CVE-2012-1823
```

```php
# 版本
	php < 5.3.12
	php < 5.4.2
```

```php
# 原理
	用户请求的querystring（querystring字面上的意思就是查询字符串，一般是对HTTP请求所带的数据进行解析，这里也是只HTTP请求中所带的数据）被作为了PHP-CGI的参数，最终导致远程代码执行。
	CGI模式下可用参数：
        -c：指定php.ini文件的位置
        -n：不要加载php.ini文件
        -d：指定配置项
        -b：启动fastcgi进程
        -s：显示文件源码
        -T：执行指定次该文件
        -h/-?：显示帮助
```

### 3、PHP-FPM远程代码执行

```php
# CVE编号
	CVE-2019-11043
```

```php
# 版本
	PHP 5.6 ~ 7.x
	Nginx >= 0.7.31
```

```php
# 原理
	Nginx上fastcgi_split_path_info在处理带有%0a的请求时，会因为遇到换行符\n导致PATH_INFO为空。而php-fpm在处理PATH_INFO为空的情况下，存在逻辑缺陷。攻击者通过精心的构造和利用，可以导致远程代码执行。
```

### 4、PHP-FPM Fastcgi未授权访问

```php
# CVE编号
	无
```

```php
# 版本
	无
```

```php
# 原理
	PHP-FPM是一个fastcgi协议解析器，Nginx等服务器中间件将用户请求按照fastcgi的规则打包好传给FPM。FPM按照fastcgi的协议将TCP流解析成真正的数据。PHP-FPM默认监听9000端口，如果这个端口暴露在公网，则我们可以自己构造fastcgi协议，和fpm进行通信。
```

### 5、PHP文件包含

```php
# CVE编号
	无
```

```php
# 版本
	无
```

```php
# 原理
	PHP文件包含漏洞中，如果找不到可以包含的文件，我们可以通过包含临时文件的方法来getshell。因为临时文件名是随机的，如果目标网站上存在phpinfo，则可以通过phpinfo来获取临时文件名，进而进行包含。
```

### 6、PHP XML实体注入

```php
# CVE编号
	无
```

```php
# 版本
	PHP 7.0.30
	libxml2.8.0
```

```php
# 原理
	如果开发人员在开发时允许引用外部实体时，恶意用户便会利用这一漏洞构造恶意语句，从而引发文件读取、命令执行、内网端口扫描、攻击内网网站、发起ODS攻击等。libxml2.9.0之后，默认不解析外部实体，导致XXE漏洞逐渐消亡。
```

### 7、XDebug远程调试

```php
# CVE编号
	无
```

```php
# 版本
	无
```

```php
# 原理
	XDebug是PHP的一个扩展，用于调试PHP代码。如果目标开启了远程调试模式，并设置remote_connect_back=1，我们访问http://ip/index.php?XDEBUG_SESSION_START=phpstorm，目标服务器的XDebug将会连接访问者的IP(或X-Forwarded-For头指定的地址)并通过dbgp协议与其通信，我们通过dbgp中提供的eval方法即可在目标服务器上执行任意PHP代码。
```

