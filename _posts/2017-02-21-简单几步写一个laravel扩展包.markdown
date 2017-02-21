> laravel使用composer来管理扩展包，理解composer和laravel的开发模式，可以通过简单的几个步骤，快速写出一个laravel扩展包。

#### 全新的laravel5.4环境安装

```
composer create-project laravel/laravel --prefer-dist .
```

#### 创建文件夹及整理目录结构

1. 在项目根目录下创建一个packages,所有的扩展文件都放在此目录下。
2. 进入到packages创建我们的目录结构。

> 扩展包的格式为：[vendor name]/[package name],

```
mkdir -p onlyus/helloworld/src
```
![目录结构图](/images/lavavel5-package-1.png)

#### 为扩展创建composer.json文件

每个扩展都需要有一个composer.json文件,进入到onlyus/helloworld文件夹下，执行：

```
composer init
```

最终结果如下所示：
```
{
    "name": "onlyus/helloworld",
    "description": "demo-package helloworld",
    "license": "MIT",
    "authors": [
        {
            "name": "zhoubo",
            "email": "congminghaoxue@foxmail.com"
        }
    ],
    "minimum-stability": "dev",
    "require": {}
}
```

#### 加载扩展

进到项目根目录下，修改项目的composer.json文件：

```
    "autoload": {
        "classmap": [
            "database"
        ],
        "psr-4": {
            "App\\": "app/",
            "Onlyus\\Helloworld\\": "packages/onlyus/helloworld/src"
        }
    },
```

然后，执行：

```composer dump-autoload```

#### 创建ServiceProvider

Service Provider是一个类，它将包含关于包的主要信息:使用什么控制器,用什么Routes文件或视图加载等,可以看它作为一组规则的包。

```
php artisan make:provider HelloworldServiceProvider
```

然后移动app/Providers/HelloworldServiceProvider.php到packages/onlyus/helloworld/src下，并修改相应的namespace,并添加注册新的Service Provider到config/app.php文件中。

#### 创建Controller和routes

分别创建文件packages/onlyus/helloworld/src/HelloworldController.php和packages/onlyus/helloworld/src/routes.php

```
namespace Onlyus\Helloworld;

use App\Http\Controllers\Controller;

class HelloworldController extends Controller
{

    public function index()
    {
        reutnr 'hello world';
    }

}
# routes.php内容
Route::get('helloworld',Onlyus\Helloworld@index);
```

#### 创建view文件

创建src/views文件夹，复制resource/views/welcome.blade.php到packages/onlyus/helloworld/src/views/helloworld.blade.php

在Service Provider注册view文件

```
public function boot()
{
    $this->loadViewsFrom(__DIR__.'/views', 'helloworld');
}
```

修改controller中index函数

```
public function index($params = NULL)
{
    return view('helloworld::helloworld', ['param'=> ($params?:'hello world')]);
}
```

[最终结果](https://onlyus.online/helloworld)

[代码](https://github.com/conginghaoxue/create-laravel-package)
