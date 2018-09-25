# Flask学习（1.1）——开发环境搭建

## pipenv工作流

### 安装Pipenv

`pipenv`是基于`pip`的`python`包管理工具

```
pip install pipenv
```

使用`pipenv --version`检查`pipenv`的安装情况

```powershell
> pipenv --version
pipenv, version 2018.7.1
```

### 创建虚拟环境

使用虚拟环境保持全局`Pyhton`解释器环境的干净，同时方便在新环境下复现依赖环境。

在`Pipenv`中已经集成了`Virtualenv`虚拟环境。

```
pipenv install
```

### 激活Pipenv

当执行`pipenv shell`或`pipenv run`时，`pipenv`会自动从项目下的`.env`文件中加载环境变量

使用`exit`退出虚拟环境

pipenv run命令可以允许你不显式激活虚拟环境，直接在当前项目的虚拟环境中执行命令。

```
pipenv run python hello.py
```

## 安装Flask

```
pipenv install flask
```

在安装过程中，除了flask本身被安装之外，同时安装的还有5个依赖包

| yi名称       | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| Jinjia2      | 模板渲染引擎                                                 |
| MarkupSafe   | HTML字符转义工具                                             |
| Werkzeug     | WSGI工具集，处理请求与响应，内置WSGI开发服务器，调试器和重载器 |
| click        | 命令行工具                                                   |
| itsdangerous | 提供各种加密签名工具                                         |

## 集成开发环境

### 并安装pycharm

pycharm有社区版和专业版，社区版免费，专业版付费，如果你是在校学生，提供相关的证明文件可以免费使用专业版

https://www.jetbrains.com/pycharm-edu/

