## 一、基础

### 1、查看系统名称

```
	cat /etc/issue
```

### 2、查看主机名

```
	hostname
	uname-a
```

### 3、查看内核信息

```
	uname -mrs
	rpm -q kernel
	dmesg | grep linux
	ls /boot | grep vmlinuz-
```

### 4、显示有效用户和组

```
	id
```

### 5、当前用户

```
	whoami
```

### 6、查看当前组

```
	groups
```

### 7、当前登录信息

```
	who
```

### 8、找带suid的文件

```
	find / -perm -u=s 2>/dev/null
```

### 9、查看当前用户执行哪些sudo命令无需密码

```
	sudo -l
```

### 10、当前用户可用的所有命令

```
	compgen -c
```

### 11、密码信息

```
	cat /etc/passwd
	
```

