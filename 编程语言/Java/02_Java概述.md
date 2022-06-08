## 一、介绍

### 1、简介

```php
	Java是可跨平台面向对象且健壮的语言，Java的强类型机制、异常处理、垃圾的自动收集等是Java程序健壮性的重要保证。
```

### 2、历史

```php
	1990 sun公司启动绿色计划
	1992 创建oak语言 -> Java
	1994 gosling参加硅谷大会，演示java功能，震惊世界
	1995 sun正式发布Java的第一个版本
	2009 甲骨文收购sun
	2011 发布java7
```

### 3、技术体系

```php
# Java SE 标准版
	支持面向桌面及应用（如Windows下的应用程序）的Java平台，提供了完整的Java核心API，此版本以前成为J2SE
```

```php
# Java EE 企业版
	是为开发企业环境下的应用程序提供的一套解决方案。该技术体系中包含的技术如：Servlet、JSP等，主要针对于Web应用程序开发。版本以前成为J2EE
```

```php
# Java ME 小型版
	支持Java程序运行在移动端上的平台，对Java API有所精简，并加入了针对移动端的支持，此版本以前成为J2ME
```

### 4、运行过程

![image-20220606000243829](C:\Users\Toby\AppData\Roaming\Typora\typora-user-images\image-20220606000243829.png)

### 5、运行机制

```php
# 核心机制 - Java虚拟机（JVM java virtual machine）
	1、JVM是一个虚拟机，具有指令集并使用不同的存储区域。辅助执行命令，管理数据、内存、寄存器，包含在JDK中
	2、对于不同的平台，有不同的虚拟机
	3、Java虚拟机机制屏蔽了底层运行平台的差别，实现了"一次编译，到处运行"
```

### 6、相关概念

```php
# JDK
	1、JDK（Java Development Kit）Java开发工具包
	2、JDK是提供给Java开发人员使用的，其中包含了Java的开发工具，也包括了JRE
```

```php
# JRE
	1、JRE（Java Runtime Environment）Java运行环境
	2、包括Java虚拟机和Java程序所需的核心类库等，如果想要运行一个开发好的Java程序，计算机中只需要安装JRE即可
```



## 二、JDK安装

### 1、下载地址

```
https://www.oracle.com/java/technologies/downloads/
```

### 2、安装步骤

```java
	1、点击安装，一路下一步
	2、自定义安装路径
```

### 3、细节说明

```java
	1、安装路径不要有中文或特殊符号，如空格等
	2、当提示安装JRE时，可选可不选
```

### 4、配置环境变量

```php
# 为什么要配置环境变量path
	当执行的程序不在当前目录时，Win10会在系统中已有的path的环境变量指定的目录中查找，如果仍未找到，则会报错"xxx不是内部或外部命令，也不是可运行的程序或批处理文件"。当在path环境变量中加入了当前文件的安装目录时，就可以在计算机任意目录运行。
```

```php
# 步骤
	1、我的电脑 -> 属性 -> 高级系统设置 -> 环境变量
	2、增加 JAVA_HOME 环境变量，内容为java安装的绝对路径
	3、编辑 path 环境变量，增加 %JAVA_HOME%\bin 
	4、打开DOS命令行，任意目录下输入javac，如果出现javac的参数信息，配置成功
```



## 三、Java快速入门

### 1、开发Hello.java

```php
# Hello.java
//1、public class Hello 表示Hello是public的公有类
//2、Hello{ } 表示一个类的开始和结束
//3、public static void main(String[] args) 表示一个主方法，即程序的入口
//4、main() {} 表示方法的开始和结束
//5、System.out.println("Hello,world~");表示将"Hello,world~"输出到屏幕
//6、;表示语句结束
public class Hello {
	public class void main(String[] args) {
		System.out.println("Hello,World~");
	}
}

class Dog {
    public class void main(String[] args) {
        System.out.println("Hello,Dog~");
    }
}

class Cat {
    public class void main(String[] args) {
        System.out.println("Hello,Cat~");
    }
}
```

```php
# 运行步骤
	1、javac Hello.java	//编译Hello.java文件（源文件）
	2、java Hello	    //运行java类（字节码文件）
```

### 2、细节说明

```php
# 什么是编译
	1、有了java源文件，通过编译器将其编译成JVM可以识别的字节码文件
	2、在该源文件目录下，通过javac编译工具对Hello.java文件进行编译
	3、如果程序没有错误，也没有任何提示，但在当前目录下出现一个Hello.clss文件，即编译成功，该文件称为字节码文件，也是可以执行的java程序
```

```php
# 什么是运行
	1、有了可执行的java程序（Hello.class字节码文件）
	2、通过运行工具java.exe对字节码文件进行执行，本质就是.class装载到jvm机执行
```

```php
# 注意事项
	1、文件有中文时，在文件 -> 设置文件编码 -> GBK
	2、修改过后的Hello.java源文件需要重新编译，生成新的class文件后，再进行执行，才能生效
```

### 3、开发注意事项

```java
	1、Java源文件以.java为扩展名。源文件的基本组成部分是类（class），如本类中的Hello类
	2、Java应用程序的执行入口是main()方法。它有固定的书写格式：
		public static void main(String[] args) {...}
	3、Java语言严格区分大小写
	4、Java方法由一条条语句构成，每个语句以";"结束
	5、大括号都是成对出现的，缺一不可，培养先写括号再写代码的习惯。
	6、一个源文件中最多只能有一个public类，其它类的个数不限
	7、如果源文件包含一个public类，则文件名必须按该类名命名
	8、一个源文件中最多只能有一个public类。其他类的个数不限，也可以将main方法写入非public类中，然后指定运行非public类，这样入口方法就是非public的main方法
```

### 4、学习方法

```php
	1、确认需求
	2、分析传统技术能否解决
	3、引出需要学习的新技术和知识点
	4、学习新技术/知识的基本原理和基本语法（不要考虑细节）
	5、快速入门（基本程序，增删改查）
	6、开始研究技术的注意事项、使用细节、使用规范、如何优化
	7、递归回1，形成闭环
```

### 5、常见错误

```java
	1、找不到文件
	2、主类名和文件名不一致
	3、缺少分号
	4、拼写错误
```

### 6、注释

```php
# 单号注释
	//
```

```php
# 多行注释
	/**/
```

```php
# 文档注释
	/** */
	注释内容会被JDK提供的javadoc解析，生成一套以网页文件形式体现该程序的说明文档，一般写在类
	javadoc -d [文件夹名] -[注释字段] -[注释字段] test.java
```

### 7、代码规范

```php
	1、类、方法的注释，使用javadoc方式
	2、非java doc的注释，着重告诉读者为什么这么写，需要注意的问题
	3、使用tab整体右移，使用shift+tab整体左移
	4、运算符和等号左右两边都留一个空格
	5、源文件使用utf-8编码
	6、行宽度不要超过80字符
	7、代码编写使用次行风格 / 行尾风格
```

### 8、DOS命令

```
	dir		列出目录
	cd		切换目录
	\		根目录
	..\		上一级目录
	tree	目录树
	cls		清屏
	exit	退出
	md		创建文件
	rd		删除文件
	copy	复制
	del		删除
	echo	输出
	type	输出
	move	剪切
```

