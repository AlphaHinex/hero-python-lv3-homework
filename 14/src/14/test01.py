from flask import Flask, render_template, request

web = Flask(__name__)


# 在下方写你的代码：设置接收GET请求方式
@web.route('/login',methods=['GET'])
def login_page():
    return render_template('test01.html')


# 在下方写你的代码：设置接收POST请求方式
@web.route('/login',methods=['POST'])
def login():
    # 在下方写你的代码：获取请求参数用户名和密码



web.run(host='127.0.0.1', port=8005)
