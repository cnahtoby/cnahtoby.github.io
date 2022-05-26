## 一、介绍

```python
# 解释
	Intruder（暴力破解）模块，用于自动对Web应用程序进行自定义的攻击，被广泛用于自动化攻击。可以使用Intruder执行例如枚举标识符、获取有用数据、漏洞模糊测试等。
```



## 二、模块

### 1、Positions 位置

```python
# 解释
	设置Payloads的插入点以及攻击类型。
```

```php
# Attack Type：攻击模式设置
	1、Sniper：狙击手，使用一个字典，对单个变量进行破解
	2、Battering ram：破城锤，使用一个字典，对多个变量同时进行破解
	3、Pitchfork：音叉，使用多个字典，一个字典分别对应一个变量，同时进行破解
	4、Cluster bomb：集束炸弹，使用多个字典，多个字典进行交叉替换，同时进行破解
```

```php
# Payload Positions：Payload位置
	1、Add $：添加
	2、Clear $：清除
	3、Auto $：自动
	4、Refresh $：刷新
	5、Clear：删除整个编辑器内容
```

### 2、Payloads 有效载荷

```php
# 解释
	设置Payload，配置字典
```

```php
# Payload Sets：Payload数量类型设置
	1、Simple list：简单字典
	2、Runtime file：运行文件
	3、Custom iterator：自定义迭代器
	4、Character substitution：字符替换
	5、Case modification：事例修改
	6、Recursive grep：递归查找
	7、Illegal Unicode：非法字符
	8、Character blocks：字符块
	9、Numbers：数字组合
	10、Dates：日期组合
	11、Brute forcer：暴力破解
	12、Null payloads：空Payload
	13、Character frobber：字符跳转器
	14、Username generator：用户名生成
	15、Copy other payload：复制其他Payload
```

```php
# Payload Options [Simple list]：根据选项1中Payload type的设置而改变
```

```php
# Payload Processing 对生成的Payload进行编码、加密、截取等操作
	1、Add prefix：添加一个文字前缀
	2、Add suffix：添加一个文字后缀
	3、Match/replace：将替换匹配的正则表达式
	4、Substring：截取字符串的长度从0开始
	5、Reverse substring：倒着匹配字符串
	6、Modify case：切换字母的大小写
	7、Encode：通过URL，HTML，Base64，ASCII码或16进制字符串对Payload进行编码
	8、Decode：通过URL，HTML，Base64，ASCII码或16进制字符串对Payload进行解码
	9、Hash：取Payload的Hash值，MD5、SHA-512等
	10、Add raw payload：在编码后的Payload上再加上原来的Payload
	11、Skip if matchers regex：如果匹配到正则表达式就跳过
	12、Invoke Burp extension：调用扩展
```

```php
# Payload Encoding：配置哪些Payload中的字符应该是URL编码
```

### 3、Resource Pool 资源池

```php
# 解释
	设置爆破的线程数及请求间隔
```

```php
# Create new resource pool：创建新的资源池
	1、Maximum concurrent requests：最大线程
	2、Delay between requests：延迟时间
	3、Milliseconds：毫秒
	4、Fixed：固定
	5、With random variations：随机变化
	6、Increase delay in increments of：以多少毫秒为增量增加延迟
```

### 4、Options

```php
# 解释
	选项卡，你可以在发起攻击之前，在主要Intruder的UI上编辑这些选项，大部分设置也可以在攻击时对已在运行的窗口进行修改。
```

```
# Save Options：保存选项
```

```php
# Request Headers：请求头
	Update Content-Length header：更新请求头
	Set Connection : close：设置连接关闭
```

```php
# Error Handling：错误头
	Number of retries on network failure：网络故障重试次数
	Pause before retry(milliseconds)：重试前暂停多少毫秒
```

```php
# Attack Results：攻击结果
	Store requests：保存请求
	Store response：保存响应
	Make unmodified baseline request：发出未修改的原始请求
	Use denial-of-service mode(no results)：使用拒绝服务模式（无结果）
	Store full payloads：保存完整Payloads
```

```php
# Grep - Match：正则匹配
	Match type：匹配类型
        Simple string：简单字符串
        Regex：正则表达式
	Case sensitive match：区分大小写匹配
	Exclude HTTP headers：排除HTTP标头
```

```php
# Grep - Extract：正则提取
	Extract the following items from response：从响应中提取以下项目
	Maximum capture length：最大捕获长度
```

```php
# Grep - Payloads：正则Payload
	Search response for payload strings：查找响应中的payload字符串
		Case sensitive match：区分大小写匹配
		Exclude HTTP headers：排除HTTP标头
		Match against pre-URL-encoded payloads：匹配预URL编码的Payload
```

```php
# Redirections：重定向响应
	Follow redirections：跟随重定向
		Never：从不
		On-site only：仅在当场
		In-scope only：仅在范围内
		Always：总是
	Process cookies in redirections：携带Cookie重定向
```

### 5、Intruder菜单栏

```php
# 模块1
	Start attack：开始攻击
	Open saved attack：打开已保存的攻击
	Scan defined insertion points：扫描定义的插入点
	Do passive scan：主动扫描
	Do active scan：被动扫描
```

```php
# 模块2
	Send to Repeater：发送到Repeater
```

```php
# 模块3
	Save attack config：保存攻击配置
        with payload positions：带有Payload位置
        without payload positions：没有Payload位置
	Load attack config：加载攻击配置
        with payload positions：带有Payload位置
        without payload positions：没有Payload位置
	Copy attack config：复制攻击配置
        with payload positions：带有Payload位置
        without payload positions：没有Payload位置
```

```php
# 模块4
	New tab behavior：新建选项卡
        Use default attack configuration：使用默认攻击配置
        Copy configuration from first tab：从第一个选项卡复制配置
        Copy configuration from last tab：从最后一个选项卡复制配置
	Automatic payloada positions：自动Payload位置
        Replace base parameter value：替换基本参数值
        Append to base parameter value：添加到基本参数值
```

```php
# 模块5
	Configure predefined payload lists：配置预定义的Payload列表
```

```php
# 模块6
	Close attack results preferences：关闭攻击结果首选项
```

