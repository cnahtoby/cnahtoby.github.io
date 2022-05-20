## 一、介绍

```python
	代理模块，BurpSuite的核心功能模块，拦截HTTP/S的代理服务器，作为浏览器和目标服务器之间的中间人，可以拦截、查看、修改两个方向的原始数据流。通过恶意的方式修改浏览器的请求，可实现SQL注入、目录遍历、会话劫持、Cookie欺骗等攻击。
```



## 二、模块

### 1、Intercept

```python
# 解释
	用于显示和修改浏览器与服务器之间的HTTP请求和响应。在该模块中，可以配置拦截规则来确定请求
```

```python
# 消息类型
	1、Raw：纯文本
	2、Hex：二进制
```

```python
# 功能按钮
	1、Forward：发送
	2、Drop：丢弃
	3、Interception is on/off：开启/关闭拦截
	4、Action：可用操作
```

```python
# 可用操作
	1、Scan：扫描
	2、Do passive scan：执行被动扫描
	3、Do active scan：执行主动扫描
	4、Send to Intruder：发送到入侵者模块
	5、Send to Repeater：发送到中继器模块
	6、Send to Comparer：发送到对比模块
	7、Send to Decoder：发送到解码器
	8、Request in browser：在浏览器中请求
	9、Extensions：扩展
	10、Engagement tools：参与工具
	11、Change request method：改变请求方法
	12、Change body encoding：改变body的编码
	13、Copy URL：复制网址
	14、Copy as curl command：作为curl命令
	15、Copy to file：导出成文件
	16、Paste from file：导入文件
	17、Save item：保存项目
	18、Don't intercept requests：不拦截请求
	19、Do intercept：做拦截
	20、Convert selection：转换选择
	21、URL-encode as you type：你需要URL编码的内容
	22、Cut：剪切
	23、Copy：复制
	24、Paste：粘贴
	25、Message editor documentation：消息编辑帮助
	26、Proxy interception documentation：代理拦截帮助
```

### 2、HTTP history

```python
# 解释
	用于显示所有请求产生的细节，显示的有目标服务器和端口，HTTP方法，URL等。
```

```python
# 字段
	#：索引
	Host：主机名
	Method：请求方法
	URL：请求地址
	Params：参数
	Edited：编辑
	Status：状态
	Length：响应字节长度
	MIME type：响应MIME类型
	Extension：地址文件扩展名
	Title：标题
	Comment：注释
	TLS：TLS协议
	IP：目标IP地址
	Cookies：Cookies
	Time：请求时间
	Listener port：端口
```

```python
# 可用操作
	1、Add to scope：添加范围
	2、Scan：扫描
	3、Do passive scan：执行被动扫描
	4、Do active scan：执行主动扫描
	5、Send to Intruder：发送到入侵者模块
	6、Send to Repeater：发送到中继器模块
	7、Send to Sequencer：发送到序列生成器
	8、Send to Comparer(request)：发送到比较器（请求）
	9、Send to Comparer(response)：发送到比较器（响应）
	10、Show response in browser：在浏览器中显示响应
	11、Request in browser：在浏览器中请求
	12、Engagement tools：接合工具
	13、Show new history window：显示新的历史窗口
	14、Add comment：添加注释
	15、Highlight：高亮
	16、Delete item：删除项目
	17、Clear history：清除历史记录
	18、Copy URL：复制网址
	19、Copy as curl command：复制为curl命令
	20、Copy links：复制链接
    21、Save item：保存项目
    22、Proxy history help：代理历史帮助
```

```python
# 过滤设置
	1、Filter by request type：根据请求类型过滤
    	· Show only in-scope items：仅显示范围内项目
        · Hide items without response：隐藏没有回复的项目
        · Show only parameterized requests：仅显示参数化请求
	2、Filter by MIME type：根据MIME类型过滤
	3、Filter by status code：根据状态码过滤
	4、Filter by search term：根据关键字过滤
	5、Filter by file extension：根据文件后缀过滤
	6、Filter by annotation：根据注释过滤
    	· Show only commented items：仅显示已备注的项目
        · Show only highlighted items：仅显示高亮的项目
    7、Filter by listener：根据端口号过滤
```

### 3、WebSockets history

```python
# 解释
	用于记录WebSockets的数据包，定义了一个全双工的通信信道，只需Web上的一个Socket即可进行通信，能减少不必要的网络流量并降低网络延迟。
```

```python
# 字段
	#：索引
	URL：请求地址
	Direction：方向
	Edited：编辑
	Length：长度
	Comment：备注
	TSL：TSL协议
	Time：时间
	Listener port：端口
	WebSocket ID：WebSocket ID
```

### 4、Options

```python
# 解释
	选项配置
```

```python
# Proxy Listeners：代理监听
	1、Running：运行
	2、Interface：接口
	3、Invisible：隐藏
	4、Redirect：重定向
	5、Certificate：证书
	6、TLS Protocols：TLS协议
	7、Import / export CA certificate：导入/导出CA证书
	8、Regenerate CA certificate：重新生成CA证书
# Add a new proxy listener：添加一个新的代理监听
	1、Binding：绑定新的代理地址和端口
    2、Request handling：控制是否将接收到的请求重定向，并向其他地方发出请求
    3、Certificate：选择CA证书
    4、TLS Protocols：TLS协议
    5、HTTP：HTTP协议
```

```python
# Intercept Client Requests：客户端请求拦截规则
	1、Enabled：复选框
	2、Operator：操作
	3、Match type：匹配类型
	4、Relationship：关系
	5、Condition：条件
	6、Intercept requests based on the following rules：根据以下规则拦截请求
	7、Automatically fix missing or superfluous new lines at end of request：在请求结束时自动修复缺失或多余的新行
	8、Automatically update Content-Length header when the request is edited：编辑请求时自动更新内容长度标题
```

```python
# Intercept Server Response：服务器响应拦截规则
	1、Enabled：复选框
	2、Operator：操作
	3、Match type：匹配类型
	4、Relationship：关系
	5、Condition：条件
	6、Intercept response based on the following rules：根据以下规则拦截响应
	7、Automatically update Content-Length header when the response is edited：编辑响应时自动更新内容长度标题
```

```python
# Intercept WebSockets Messages：拦截WebSocket消息
	1、Intercept client-to-server messages：拦截客户端发送给服务器的消息
	2、Intercept server-to-client messages：拦截服务器发送给客户端的消息
```

```python
# Response Modification：响应修改
	1、Unhide hidden form fields：不隐藏隐藏的表单字段
	2、Enable disabled form fields：启用禁用的表单字段
	3、Remove input field length limits：删除输入字段长度限制
	4、Remove JavaScript form validation：删除Javascript表单验证
	5、Remove all Javascript：删除所有Javascript
	6、Remove <object> tags：删除所有对象标签
	7、Convert HTTPS links to HTTP：将HTTPS链接转换为HTTP
	8、Remove secure flag from cookies：从Cookie中删除安全标志
```

```python
# Match and Replace：匹配替换
	1、Enabled：开启
	2、Item：选项
	3、Match：匹配内容
	4、Replace：替换为
	5、Type：类型
	6、Comment：备注
```

```python
# TLS Pass Through：TLS通过
	1、Enabled：开启
	2、Host / IP range：主机名/IP范围
	3、Port：端口
```

```python
# Miscellaneous：其他
	1、Use HTTP/1.0 in requests to server：在对服务器的请求中使用HTTP/1.0
	2、Use HTTP/1.0 in responses to client：在对客户端的响应中使用HTTP/1.0
	3、Set response header "Connection:close"：设置响应头“连接：关闭”
	4、Set "Connection close" on incoming requests when using HTTP/1：当传入的请求为HTTP/1.0时，设置连接关闭
	5、Strip Proxy-* headers in incoming requests：去除传入的请求中的代理标头
	6、Remove unsupported encodings from Accept-Encoding headers in incoming requests：在传入的请求中移除不支持Accept-Encoding的编码
	7、Strip Sec-WebSocket-Extensions headers in incoming requests：在传入的请求中去除Sec-WebSocket-Extensions标头
	8、Unpack gzip / deflate in requests：在请求中解压gzip / deflate
	9、Unpack gzip / deflate in response：在响应中解压gzip / deflate
	10、Disable web interface at http://burpsuite：禁用HTTP Web接口：http://burpsuite
	11、Suppress Burp error messages in browser：抑制Burp在browser的错误消息 
	12、Don't send items to Proxy history or live tasks：不将项目发送到代理历史记录或实时任务
	13、Don't send items to Proxy histoty or live tasks,if out of scope：如果超出范围，不将项目发送到代理历史记录或实时任务
```
