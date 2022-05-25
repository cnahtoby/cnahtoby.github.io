## 一、介绍

### 1、解释

```php
	Dashboard仪表盘，用于显示任务、日志信息。
```



## 二、模块

### 1、Tasks 任务区

```php
# 解释
	新建的扫描任务或正在运行的任务都会在该区域显示。
```

```php
# New scan 主动扫描
	1、Scan details：详细信息
		1.1、Scan Type：扫描类型
			Crawl and audit：爬虫并审计
			Crawl：爬虫
		1.2、URLs to Scan：要扫描的URL
		1.3、Protocol settings：协议设置
			Scan using HTTP & HTTPS：使用HTTP/HTTPS协议扫描
			Scan using my specified protocols：使用指定的协议扫描
	2、Scan configuration：扫描配置
	3、Application login：应用程序登录
	4、Resource pool：资源池
```

```php
# New live task 新建实时任务
	1、Live passive crawl from Proxy：自动爬取经过代理的流量
	2、Live audit from Proxy：审计经过代理的流量
	3、Scan details：详细信息
	4、Scan configuration：扫描配置
	5、Resource pool：资源池
```

### 2、Event log 事件区

```php
# 解释
	BurpSuit报错或者事件的状态（扫描开始，扫描结束）都会在该区域显示。
```

### 3、Issue activity 漏洞

```php
# 解释
	该区域显示扫描出的漏洞，通过High、Medium、Low查看不同危险等级的漏洞。
```

