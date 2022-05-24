## 一、介绍

### 1、解释

```python
	Extender模块（扩展模块），Burp在软件中提供了支持第三方拓展插件的功能，方便使用者编写自己的自定义插件或从软件商店中安装拓展插件。
```



## 二、模块

### 1、Extensions 扩展

```python
# 功能按钮
	Details：细节
	Output：输出
	Errors：错误
```

```python
# 日志信息输出方式
	1、系统控制台输出
	2、存储到指定的文件中
	3、Burp界面输出，默认情况下，会选择Burp的界面输出
```

### 2、BApp Store 应用商店

```php
# 功能按钮
	Install：安装
	Reinstall：重新安装
	Submit rating：提交评分
	Manual install：手动安装
```

### 3、APIs 扩展API

### 4、Options 选项

```php
# Settings 设置
	Automatically reload extensions on startup：启动时自动重新加载扩展程序
	Automatically update installed BApps on startup：启动时自动更新已安装的扩展程序
```

```php
# Java Environment	Java环境
	Folder for loading library JAR files (optional)：用于加载库JAR文件的文件夹
	Select folder：选择文件夹
```

```python
# Python Environment	Python环境
	Location of Jython standalone JAR file：Jython独立的JAR文件位置
	Folder for loading modules (optional)：用于加载模块的文件夹
```

```python
# Ruby Environment
	Location of JRuby JAR file：JRuby JAR文件的位置
```

