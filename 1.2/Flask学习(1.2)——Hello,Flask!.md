# Flask学习（1.2）——Hello,Flask!

对于简单的程序来说，一般使用app.py来作为程序的主模块。也可以使用其他名称，但不能使用flask.py，因为这和flask本身冲突。

## 创建程序实例

从flask包中导入Flask类，这个类表示一个Flask程序。实例化这个类，就得到程序实例app。

```python
from flask import Flask
app = Flask(__name__)
```

传入Flask类构造方法的第一个参数是模块或包的名称，我们应该使用特殊变量`__name__`。

python会根据所处的模块来赋予`__name__`变量相应的值，对于这个程序来说，`__name__`被赋值为app。

除此之外，这也会帮助Flask在相应的文件夹找到需要的资源，比如模板和静态资源。

## 注册路由

在Web应用中，客户端和服务器上的Flask程序交互可以简单概况：

1. 用户在浏览器输入url访问某个资源
2. Flask接收用户请求并分析请求的url
3. 为url找到对应的处理函数
4. 执行函数并生成响应，将信息展示在页面中

路由，即“按路线发送”，调用与请求url对应的视图函数。

Flask帮我们完成了大多数步骤，我们只需要建立处理请求的函数，并为其定义对应的url规则。

只需要为函数附加app.route()装饰器，为传入url规则作为参数，我们就可以让url与函数建立关联。这个过程称为注册路由（route）。路由负责管理url和函数之间的映射，而这个函数称为视图函数(view function)。

```python
@app.route('/')
def index():
    return '<h1>Hello,World!</h1>'
```

在上面这段代码中，app.route()装饰器把根地址`\`和`index()`函数绑定起来,当用户访问这个地址时就会触发`index()`函数。视图函数返回的值将作为相应的主体，一般来说，响应的主体就是呈现在浏览器窗口的HTML页面。

### 为视图绑定多个url

一个视图函数可以绑定多个url。比如下面的代码把`/hi`和`/hello`都绑定到`say_hello()`函数上。

```python

```

### 动态url

我们可以在url规则中添加变量部分,使用`<变量名>`的形式表示。Flask处理变量时会把变量传入视图函数，所以我们可以添加参数获取这个变量值。

下面的代码中，url规则包含了一个`name`变量。

```python
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name
```

当url规则中包含变量时，如果用户访问的url中没有添加变量，比如访问`\greet`,那么Flask在访问失败后会返回一个404错误。我们可以在`app.route()`装饰器中使用`defaults`参数设置url变量的默认值，这个参数接收字典作为输入，存储url变量和默认值的映射。

```python

```

在上面的代码中，我们为`/greet`设置了默认的`name`值。

这时当用户访问`/greet`时，那么变量`name`将会使用默认值`Programmer`。

在函数内设置变量默认值也可以达到同样的效果。