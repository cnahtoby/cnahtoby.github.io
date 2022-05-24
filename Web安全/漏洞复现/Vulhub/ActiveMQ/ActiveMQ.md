## 一、介绍

### 1、解释

```python
	ActiveMQ是一个消息队列应用服务器（推送服务器），支持JMS规范。
```

### 2、JMS

```php
	JMS全称Java Message Service（Java消息服务），是一套Java消息服务的API接口。实现了JMS标准的胸痛，称之为JMS Provider。
```

### 3、消息队列

```php
	消息队列是在消息的传输过程中保存消息的容器，提供一种不同进程或者同一进程不同线程直接通讯的方式。
```

![image-20220525002552135](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220525002552135.png)

```python
# 术语
	Producer：消息发送者
	Broker：消息处理中心
	Consumer：消息接收者
```

```python
# 常见消息队列应用
1、ActiveMQ
	ActiveMQ是Apache出品，最流行的，能力强劲的开源消息总线。ActiveMQ是一个完全支持JMS1.1和J2EE 1.4规范的JMS Provider实现。
	
2、RabbitMQ
	RabbitMQ是一个在AMQP基础上完成的，可用的企业消息系统。遵循Mozilla Public License开源协议。开发语言为Erlang。
	
3、RocketMQ
	RocketMQ是由阿里巴巴定义开发的一套消息队列应用服务。
```



## 二、历史漏洞

### 1、ActiveMQ反序列化漏洞（CVE-2015-5254）

```python
# 发现
	端口：8161
	版本：5.x ~ 5.13.0
```

### 2、ActiveMQ任意文件上传漏洞（CVE-2016-3088）

```python
# 发现
	端口：8161
	版本：5.x ~ 5.14.0
```



## 三、利用工具

### 1、Ysoserial

```python
# 下载
	https://github.com/frohoff/ysoserial
```

```python
# 解释
	Ysoserial集合了各种Java反序列化Payload的工具。
```

### 2、Jmet

```python
# 下载
	https://github.com/matthiaskaiser/jmet/releases/download/0.1.0/jmet-0.1.0-all.jar
```

```php
# 解释
	Jmet原理是使用Ysoserial生成Payload并发送（其jar内自带Ysoserial，无需再自己下载），所以我们需要在Ysoserial是gadget中选择一个可以用的，比如ROME。
```



## 四、漏洞分析

### 1、ActiveMQ缺陷概述

```php
	ActiveMQ默认使用8161端口，管理后台地址为/admin，默认管理员密码admin/admin，反序列化漏洞利用涉及61616工作端口。可以通过工具进行批量检测，如小米范Web查找哦工具、Nmap。
```

### 2、CVE-2015-5254

```python
# 漏洞成因
	该漏洞源于程序没有限制可在代理中序列化的类，攻击者可借助特制的序列化的Java Message Service(JMS)Object Message对象利用该漏洞进行执行任意代码。
```

```python
# 流量分析
	1、从流量分析攻击者是否进行端口扫描，探测服务器的端口以确定运行服务。
	2、判断攻击者是否访问Web的8161端口，并尝试用弱口令进行登录。
	3、在数据流里分析攻击者是否向61616发送Payload。
	4、判断攻击者是否登录Web服务进行点击触发。
	5、判断请求ID是否与SessionInfo返回的消息ID一致。
	6、根据状态码以及内容判断执行是否成功。
	7、分析后续的流量判断主机是否已失陷。
```

```python
# 修复建议
	1、针对未授权访问，可修改conf/jetty.xml文件，bean id为securityConstranit下的authenticate修改值为true，重启服务即可。
	2、针对弱口令，可修改conf/jetty.xml文件，bean id为securityLoginService下的conf值获取用户properties，修改用户名密码，重启服务即可。
	3、升级版本至最新版本。
```

### 3、CVE-2016-3088

```python
# 漏洞成因
	ActiveMQ默认开启PUT、MOVE请求，当开启PUT时，构造好Payload，Response会返回相应的物理路径信息。
```

```php
# 修复建议
	1、通过移除conf/jetty.xml的以下配置来禁用ActiveMQ Fileserver功能。
	2、升级版本至最新版本。
```

