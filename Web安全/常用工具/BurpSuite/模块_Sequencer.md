## 一、介绍

### 1、解释

```php
	Sequencer定序器，是一种用于分析数据项的一个样本中的随机性质量的工具。可以用它来测试应用程序的Session token或其他重要数据项。
```



## 二、模块

### 1、Live capture 信息截取

```php
# Select Live Capture Request 选择实时捕获请求
	从其他工具发送并捕获该请求
```

```php
# Token Location Within Response 令牌在响应中的位置
```

```php
# Live Capture Options 实时捕获选项
	Number of threads：线程数
	Throttle between requests：请求间隔速度
	Ignore tokens whose length deviates by ... charcters：忽略长度偏离字符的标记
```

### 2、Manual load 手动加载

```php
	Analyze now：立即分析
	Tokens loaded：令牌加载
	Shortest：最短
	Longest：最长
```

### 3、Analysis options 选项分析

```php
# Token Handling	令牌处理
	Pad short tokens：填充短Token
	Pad with (single character or 2-digit ASCII hex code)：填充单字符或2位ASCII十六进制代码
```

```php
# Token Analysis	令牌分析
	Count：统计
	Transitions：转换
```

