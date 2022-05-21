## 一、介绍

```python
# 解释
	Repeater（中继器）模块是用于修改并补发个别HTTP请求，并分析他们的响应的工具。
```



## 二、模块

### 1、功能点

```python
Send：发送
Cancel：取消
<：返回上一步
>：返回下一步
```

### 2、显示界面

```
Pretty：美观页面
Raw：纯文本格式
Hex：二进制
Render：返回页面
Search：查找
```

### 3、菜单栏

```python
Update Content-Length：更新头部长度
Unpack gzip / deflate：控制Burp是否自动解压缩在收到的gzip和deflate
Follow redirections：遇到重定向时的处理方式
Process cookies in redirections：当被重定向后是否提交cookie
Enforce protocol choice on cross-domain redirections：强制跨域重定向上的协议选择
Normalize HTTP/1 line endings：规范化HTTP/1的行结尾
Enable HTTP/2 connection reuse：启用HTTP/2连接重用
Strip Connection header over HTTP/2：通过HTTP/2去除连接头
Allow HTTP/2 ALPN override：允许HTTP/2 ALPN覆盖
Action：等同于右键菜单
```

