from flask import Flask #从flask包引入Flask类
app = Flask(__name__) #实例化

@app.route('/') #注册路由
def index():
    return '<h1>Hello,Flask!</h1>'