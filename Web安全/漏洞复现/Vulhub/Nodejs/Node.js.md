## 一、介绍

### 1、简介

```
	Nodejs是基于Chrome的V8引擎开发的一个C++程序，目的是提供一个JS运行环境。
```

### 2、端口

```
	无
```

### 3、Logo

![See the source image](https://th.bing.com/th/id/R.c3315bc0ba17f85d6784fce416139e4f?rik=y8afSszmUyyekw&pid=ImgRaw&r=0)

![See the source image](https://th.bing.com/th/id/R.c502658a509d27b53679b3ef73c0d82f?rik=dFP%2b9LyCq64MMg&pid=ImgRaw&r=0)

### 4、开发语言

```
	C++
```

### 5、默认密码

```
	无
```



## 二、历史漏洞

### 1、Node.js目录穿越

### 2、node-postgres代码执行漏洞



## 三、利用工具

```
	无
```



## 四、漏洞分析

### 1、Node.js目录穿越

```php
# CVE编号
	CVE-2017-14849
```

```php
# 版本
	Node.js 8.5.0 + Express 3.19.0-3.21.2
	Node.js 8.5.0 + Express 4.11.0-4.15.5
```

```php
# 原理
	由于Node.js 8.5.0对目录进行normalize操作时出现了逻辑错误，导致向上层跳跃的时候（如../../../../../../etc/passwd），在中间位置增加foo/../（如../../../foo/../../../../etc/passwd），即可使normalize返回/etc/passwd，但实际上正确结果应该使../../../../../../etc/passwd。
```

### 2、node-postgres代码执行漏洞

```php
# CVE编号
	CVE-2017-16082
```

```php
# 版本
	7.1.0
```

```php
# 原理
	node-postgres在处理类型为 Row Description 的postgres返回包时，将字段名拼接到代码中。由于没有进行合理转义，导致一个特殊构造的字段名可逃逸出代码单引号限制，造成代码执行漏洞。
```

