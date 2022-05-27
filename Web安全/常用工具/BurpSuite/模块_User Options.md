## 一、介绍

### 1、解释

```php
	User options模块主要用来配置一些常用的选项。
```



## 二、模块

### 1、Connections 连接

```php
# Platform Authentication：平台验证
	- 这些设置允许您配置burp以自动执行到目标web服务器的平台身份验证
	Do platform authentication：执行平台认证
	Prompt for credentials on planform authentication failure：子啊平台身份验证失败时提示凭据
```

```php
# Upstream Proxy Servers：上游代理服务器
	- 以下规则确定Burp是将每个传出请求发送到代理还是直接发送到目标Web服务器，匹配每个目标主机的第一个规则将用于将所有流量发送到单个代理服务器，创建一个带有*作为目标主机的规则。
```

```php
# Socks Proxy：Socks代理
	Use SOCKS proxy：使用SOCKS代理
	SOCKS proxy host：SOCKS代理主机
	SOCKS proxy port：SOCKS代理端口
	Do DNS lookups over SOCKS proxy：通过SOCKS代理进行DNS查找
```

### 2、TLS

```php
# Java TLS Options：Java TLS选项
	- 这些设置可用于启用成功连接到某些服务器可能需要的某些SSL功能
	Enable algorithms blocked by Java security policy：启用由JAVA安全策略阻止的算法
	Disable Java SNI extension：禁用JAVA SNI扩展
```

```php
# Client TLS Certificates：客户端TLS证书
	- 这些设置允许您配置客户端TSL证书，当目标主机请求一个打印将使用主机配置与被联系的主机的名称匹配的列表的第一个证书时，Burp将使用这些证书，您可以双击项目以查看证书的全部详细信息
```

### 3、Display

```php
# User Interface：用户界面
	- 这些设置允许您控制Burp suite用户界面的外观
	Font size：字体大小
	Theme：外观和感觉
```

```php
# HTTP Message Display：HTTP消息显示
	- 这些设置允许您控制http消息在原始http查看器/编辑器中的显示方式
	Highlight request syntax：突出显示请求参数
	Highlight response syntax：突出显示响应参数
	Pretty print by default：自动打印漂亮格式
```

```php
# Character Sets：字符集
	- 这些设置控制控制在显示原始HTTP消息时如何处理不同的字符集，注意到一些字体不支持所有字体，如果您需要使用扩展或异常字符集，应首先尝试系统字符，如couier new或dialog
	Recognize automatically based on message headers：基于邮件头自动识别
	Use the platform default：使用平台默认（GBK）
	Display as raw bytes：显示为原始字节
	Use a specific character set：使用特定的字符集
```

```php
# HTML Rendering：HTML呈现
	- 这些设置控制如何处理HTML内容的工具内渲染
	Allow renderer to make HTTP requests：允许渲染器发出HTTP请求
```

```php
# Inspector and Message Editor：检查器和消息编辑器
	- 通过这些设置，您可以自定义消息编辑器、inspector面板上显示的小部件，以及自定义显示的信息
	Open Inspector and Message Editor settings：打开检查器和消息编辑器设置
```

### 4、Misc 杂项

```php
# Hotkeys：热键
	- 这些设置允许为公共操作配置热键，其中包括特定于项目的操作，例如"发送到中继器"全局操作（如"切换到代理"）和编辑器操作（如"剪切"和"撤销"）
```

```php
# Temporary Files Location：临时文件位置
	- 这些设置让您配置Burp存储其临时文件更改的位置
```

```php
# Rest API

	Service running：服务启动
	Allow access without API key：允许无API密钥访问
```

```php
# Proxy Interception：代理拦截
	- 这些设置控制启动时代理拦截的状态
	Enable interception at startup：在启动时启用拦截
        Always enable：总是启用
        Always disable：总是禁用
        Restore setting from when Burp was last closed：恢复上次关闭burp时的设置形式
```

```php
# Proxy History Logging：代理历史日志
	- 这些设置控制HTTP请求和响应的日志
```

```php
# Performance Feedback：性能反馈
	- 你可以通过提交关于Burp的性能的匿名反馈帮助改善Burpsuite
	Submit anonymous feedback about Burp's performance
	Log exceptions to a local directory
```

```php
# HTTP Message Search：HTTP消息搜索
	Case sensitive：区分大小写
	Regex：正则表达式
	Auto-scroll to match when text changes：文本更改时自动滚动匹配
```

```php
# Burp's Browser：Burp浏览器
	Allow Burp's browser to store settings and history：允许Burp的浏览器存储设置和历史记录
```

```php
# Tasks：任务
	"Pause automated tasks" option selected by default：默认选择"暂停自动任务"选项
```

```php
# Learn Tab：学习选项卡
	Show the learn tab：显示"学习"选项卡
```

