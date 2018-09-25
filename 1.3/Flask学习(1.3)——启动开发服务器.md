# Flask学习(1.3)——启动开发服务器

## Run,Flask!

Flask内置了一个CLI(Command Line Interface，命令行交互界面)系统。我们可以通过flask命令执行内置命令、扩展提供的命令、或是我们自己定义的命令。其中，`flask run`用来启动内置的开发服务器：

```shell
> flask run
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

我们还可以使用`flask --help`来查看所有可用命令。

`flask run`这个命令运行的开发服务器默认会监听 http://127.0.0.1:5000/，并开启多线程支持。

注意：旧的启动开发服务器的方式是`app.run()`方法，目前已经不推荐使用。

### 自动发现程序实例

我们可以直接运行程序而不需要提供程序实例所在位置，这是因为Flask会自动探测程序实例，自动探测存在下面这些规则：

- 从当前目录寻找名为`app.py`或`wsgi.py`模块，并从中寻找名为`app`或`application`的程序实例
- 从环境变量`FLASK_APP`寻找`app`或`application`的程序实例

如果我们的主程序模块是其他名称，比如`hello.py`，那么需要设置环境变量`FLASK_APP`，将包含程序实例的模块赋值给这个变量。

Windows使用`set`命令：

```shell

```

### 管理环境变量

如果安装了`python-dotenv`,那么在使用`flask run`或其他命令时会使用它自动从`.flaskenv`文件和`.env`文件中加载环境变量。

使用`python-dotenv`可以帮助我们方便的管理环境变量。

安装`python-dotenv`到虚拟环境：

```shell
pipenv install python-dotenv
```

我们在项目根目录下创建