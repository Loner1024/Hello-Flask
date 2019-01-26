from flask import Flask #从flask包引入Flask类
app = Flask(__name__) #实例化

@app.route('/<name>') #注册路由
def index(name):
    return '<h1>Hello,Flask! 你好，%s</h1>' % name