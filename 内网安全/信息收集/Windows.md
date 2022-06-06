## 一、主机信息

### 1、系统程序

```php
# 查询简易系统信息
	net config workstation/server
```

```php
# 查询全部内容
	systeminfo
```

```php
# 查询已安装的补丁列表
	wmic qfe get Caption,Description,HotFixID,InstalledOn
```

### 2、进程服务

```php
# 查询正在运行的进程
	tasklist /v
```

```php
# 查询所有安装过的软件及版本
	wmic product get name,version
```

```php
# 使用powershell查询所有安装过的软件及版本，效果和wmic相同
	powershell "Get-WmiObject-class Win32_Product|Select-Object-Property name,version"
```

```php
# 查询当前机器的服务信息
	wmic service list brief
```

```php
# 查看启动项
	wmic startup get command,caption
```

### 3、用户信息

```php
# 当前用户
	whoami
```

```php
# 查询登录用户
	quser
```

```php
# 查询登录用户
	qwinsta
```

```php
# 查询登录用户
	query user
```

```php
# 查询会话
	query session
```

```php
# 查询远程桌面主机列表
	query termserver
```

```php
# 查询域密码策略
	net accounts
```

```php
# 查询本地用户列表
	net user
```

```php
# 查询指定用户
	net user "$username"
```

```php
# 查询本地用户组列表
	net localgroup
```

```php
# 查询指定用户组成员
	net localgroup Guests
```

```php
# 查询用户组列表，仅域控可执行
	net group
```

```php
# 查询用户组成员，仅域控可执行
	net group "$groupname"
```

### 4、操作记录

```php
# 查看posershell当前窗口历史操作记录
	Get-History | Format-List -Property
```

```php
# 删除powershell当前窗口历史操作记录
	Clear-History
```

```php
# 删除powershell当前窗口指定ID的历史操作记录
	Clear-History -Id 3
```

```php
# 查看cmd的历史操作记录
	doskey /h
```

```php
# 删除cmd的历史操作记录
	doskey /reinstall
```



## 二、网络信息

### 1、基本信息收集

```php
# 列出当前主机详细网络信息
	ipconfig /all
```

```php
# 列出dns缓存信息
	ipconfig /displaydns
```

```php
# 查询路由表
	route print
```

```php
# 地址解析协议缓存表
	arp -a
```

```php
# 端口使用情况
	netstat -ano
```

```php
# 查看共享信息
	net share
```

```php
# 查看共享资源列表
	net view
```

```php
# 查看共享信息
	wmic share get name,path,status
```

```php
# 查看hosts文件
	type c:Windows\system32\drivers\etc\hosts
```

### 2、系统日志

```php
# 查询登录日志
	wevtuil qe security /f:text /q:*[System[EventID=4624]]
```

```php
# 查询所有登录、注销相关的日志语法
	wevtuil qe security /rd:true /f:text /q:"*[System/eventid=4624 and 4623 and 4627]"
```



## 三、域信息

### 1、基本信息收集

```php
# 查询当前登录域
	net config workstation
```

```php
# 同步时间，通常为域控
	net time
```

```php
# 查询域密码策略
	net accounts /domain
```

```php
# 列出当前域成员列表
	net user /domain
```

```php
# 查询域列表
	net view /domain
```

```php
# 查询test域中计算机列表
	net view /domain.test
```

```php
# 查询域内的所有DC
	nltest /dclist:domain
```

```php
# 拿到DC当前的认证信息
	nltest /dsgetdc:domain
```

```php
# 查询域信任信息
	nltest /domain_trusts
```

```php
# 得到用户信息
	nltest /user:"username"
```



## 四、配置文件收集

### 1、配置文件

```php
# IIS配置文件路径
	%windir%\system32\inetsrv\config\applicationHost.config
```

```php
# 使用appcmd快速导出所需内容
	%windir%\system32\inetsrv\appcmd list site /config
	%windir%\system32\inetsrv\appcmd list site /config /xml > c:\sites.xml
```

### 2、密码保存

```php
# navicat
```

| **数据库**    | **路径**                                                     |
| ------------- | ------------------------------------------------------------ |
| MySQL         | HKEYCURRENTUSER\Software\PremiumSoft\Navicat\Servers\        |
| MariaDB       | HKEYCURRENTUSER\Software\PremiumSoft\NavicatMARIADB\Servers\ |
| MongoDB       | HKEYCURRENTUSER\Software\PremiumSoft\NavicatMONGODB\Servers\ |
| Microsoft SQL | HKEYCURRENTUSER\Software\PremiumSoft\NavicatMSSQL\Servers\   |
| Oracle        | HKEYCURRENTUSER\Software\PremiumSoft\NavicatOra\Servers\     |
| PostgreSQL    | HKEYCURRENTUSER\Software\PremiumSoft\NavicatPG\Servers\      |
| SQLite        | HKEYCURRENTUSER\Software\PremiumSoft\NavicatSQLite\Servers\  |

```php
# SecureCRT
```

| **系统版本**     | **路径**                                                     |
| ---------------- | ------------------------------------------------------------ |
| xp/win2003       | C:\Documents and Settings\USERNAME\Application Data\VanDyke\Config\Sessions |
| win7/win2008以上 | C:\Users\USERNAME\AppData\Roaming\VanDyke\Config\Sessions    |

```php
# Xshell
```

| 版本     | **路径**                                                     |
| -------- | ------------------------------------------------------------ |
| Xshell 5 | %userprofile%\Documents\NetSarang\Xshell\Sessions            |
| Xshell 6 | %userprofile%\Documents\NetSarang Computer\6\Xshell\Sessions |

```php
# WinSCP
	HKCU\Software\Martin Prikryl\WinSCP 2\Sessions
```

```php
# VNC
```

| **版本** | **路径**                                       | **类型**                     |
| -------- | ---------------------------------------------- | ---------------------------- |
| RealVNC  | HKEYLOCALMACHINE\SOFTWARE\RealVNC\vncserver    | Password                     |
| TightVNC | HKEYCURRENTUSER\Software\TightVNC\Server Value | Password or PasswordViewOnly |
| TigerVNC | HKEYLOCALUSER\Software\TigerVNC\WinVNC4        | Password                     |
| UltraVNC | C:\Program Files\UltraVNC\ultravnc.ini         | passwd or passwd2            |

