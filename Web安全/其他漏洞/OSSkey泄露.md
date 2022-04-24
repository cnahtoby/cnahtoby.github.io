## 一、漏洞原理

### 1、简介

```python
# 解释
OSS服务提供文件上传、下载和存储服务，也被一些网站开发者用来搭建网站的上传功能（避免攻击者通过文件上传功能上传恶意脚本文件到网站）。当开发者用Javascript实现OSS上传下载服务时，免不了要配置对应的Accesskey，JS又是前端能够直接访问看到的，就造成了Accesskey泄露。
```

```python
# 危害
1、通过AccessKey访问公司内部资源
2、接管OSS服务器
3、修改/重置ECS密码信息
```

### 2、详情

```python
# OSS介绍
OSS(Object Storage Service)对象存储服务，是一种海量、安全、低成本、高可靠的云存储服务，适合存放任意类型的文件。容量和处理能力弹性扩展，多种存储类型供选择，全面优化存储成本。
```

```python
# OSS关键词
Bucket（存储空间）：存放文件的地址空间、文件容器。
Object（对象/文件）：存放在存储空间的文件，内容就是一个对象。
Region（地域）：存储空间的物理地址区域。
Endpoint（访问路径）：文件地址，OSS对外服务的访问域名。
AccessKey（访问密钥）：验证身份的钥匙，上传下载的账号密码。
```



## 二、漏洞特征

### 1、场景

```
1、使用云服务器的中小型企业或个人
```

### 2、发现

```python
# JS文件
内容搜索：key、accesskey
BurpSuite抓包：key、accesskey
解密：console.log(atob("加密字符串"))
```

```python
# GITHUB
内容搜索：
	key
    accesskey + [公司域名]
```

```PYTHON
# FOFA
内容搜索：
	key
	accesskey + [公司域名]
	"accessKeyId" && country="CN" && is_domain=true
    "accesskeyID"&&"Whoops! There was an error"
    title="Whoops! There was an error" && country="CN" && is_domain=true
   
```

```python
# 其他
APK反编译后的配置文件
低权限的WEBSHELL查看网站的配置文件
Swagger API泄露
Laravel框架信息泄露
ThinkPHP报错页面
```



## 三、利用条件

### 1、对方启用OSS服务



## 四、利用方法

### 1、API接口

```python
通过AccessKey ID和AccessKey Secret可调用API，完成对服务器ECS实例的管理和运维操作。
```

### 2、第三方管理工具

```python
# 登录即可直接g
OSSBrowser		 # OSS官方图形化管理工具
护卫神·云备份		# 一键备份数据到阿里云OSS
行云管家		 # 多云管理平台
```



## 五、相关工具

### 1、AliCloud-Tools

```python
# 介绍
辅助使用阿里云API操作ECS以及策略的工具，方便快速使用阿里云API执行操作
```

```python
# 下载
https://github.com/iiiusky/alicloud-tools
```

```python
# 参数
-a		--ak string 阿里云AccessKey
-r		--rid string 阿里云 地域ID
-s		--sk string 阿里云 SecretKey
ecs		ECS操作（查询/执行命令），当前命令支持地域ID设置
sg		安全组操作
```

```python
# 使用
1、查看所有地域信息
./AliCloud-Tools -a <AccessKey> -s <SecretKey> --regions
2、查看所有实例信息
./AliCloud-Tools -a <AccessKey> -s <SecretKey> ecs --list
3、查看所有正在运行的实例信息
./AliCloud-Tools -a <AccessKey> -s <SecretKey> ecs --list --runner
4、查看指定实例的信息
./AliCloud-Tools -a <AccessKey> -s <SecretKey> [-r <regionId>] ecs --eid <InstanceId>
5、执行命令
./AliCloud-Tools -a <AccessKey> -s <SecretKey> [-r <regionId>] ecs exec -I <InstanceId[,InstanceId,InstanceId,...]> -c "touch /tmp/123123aaaa.txt"
6、查看安全组策略
./AliCloud-Tools -a <AccessKey> -s <SecretKey> -r <regionId> sg --eid <SecruityGroupId>
7、增加安全组策略
./AliCloud-Tools -a <AccessKey> -s <SecretKey> -r <regionId> --eid <SecruityGroupId> --action add --protocol tcp --port 0/0 --ip 0.0.0.0/0
8、删除安全组策略
./AliCloud-Tools -a <AccessKey> -s <SecretKey> -r <regionId> --eid <SecruityGroupId> --action del --protocol tcp --port 0/0 --ip 0.0.0.0/0
```

### 2、行云管家

```python
# 介绍
多云管理平台，导入AccessKey，可重置服务器密码，接管服务器。
```

```python
# 下载
https://www.cloudbility.com/
```

### 3、OSSBrowser

```python
# 介绍
OSSBrowser是OSS官方提供的图形化管理工具，提供类似Windows资源管理的功能，用于浏览、上传、下载和管理文件。
```

```python
# 下载
http://gosspublic.alicdn.com/oss-browser/1.9.4/oss-browser-win32-x64.zip
```

### 4、护卫神·云备份

```python
# 介绍
一键备份数据到阿里云OSS，支持Bucket管理，支持鼠标拖放、剪贴板、断点续传、文件搜索等功能。
```

```python
# 下载
https://d.hws.com/free/HwsOSS.zip
```



## 六、防护措施

### 1、代码修复

```python
采用JavaScript客户端签名直传存在严重安全风险，建议采用服务端签名后直传。
```

### 2、信息保护

```
更换AccessKey
```

```
使用临时AccessKey
```

