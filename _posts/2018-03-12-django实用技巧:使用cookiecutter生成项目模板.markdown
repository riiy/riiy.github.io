> 使用Django的默认项目布局有许多问题，虽然在练习时候很有用，但一旦您开始开发一个真正的项目，这个布局它就不那么有用。cookiecutter是一个从项目模板创建项目的命令行工具，支持windows、mac osx、linux/unix。 可以创建Python包项目，jQuery插件项目等。

#### cookiecutter-django的官方教程

[Cookiecutter Django’s documentation](https://cookiecutter-django.readthedocs.io/en/latest/)

#### 下载安装

执行下列命令
```python
pip install cookiecutter
cookiecutter https://github.com/pydanny/cookiecutter-django
```

> cookiecutter-django是一个用于快速生成Django项目的框架模板。

如果要生成特定的版本，加上tag即可：

```python
cookiecutter https://github.com/pydanny/cookiecutter-django/tree/1.11.10
```

#### 配置django

之后会出现一系列对话框，根据你的需要填写即可。

#### 安装依赖包

进入myapp工作目录，执行
```python
pip install -r myapp\requirements\base.txt
pip install -r myapp\requirements\local.txt
# or
pip install -r myapp\requirements\production.txt
```

#### 优点

1. 使用100％的测试覆盖率渲染Django项目
2. 前端使用Twitter Bootstrap v4.0.0 开发模板
3. 通过django-environ进行环境变量设置
1. 优化开发和生产设置
1. 通过django-allauth注册
1. 自定义用户模型
1. 可以基于Grunt和livereload构建
1. 可以多平台部署（主要是国外平台）
1. 使用unittest或py.test运行测试


#### 集成第三方工具到项目
> 这些工具可以在初始化项目期间来启用。
1. Celery:第三方异步任务队列
1. MailHog:进行本地电子邮件测试
1. Sentry:进行错误记录
1. Opbeat:进行性能监控

