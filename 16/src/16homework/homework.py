from flask import Flask, url_for, redirect, render_template, request
from datetime import timedelta

web = Flask(__name__)

web.debug = True


@web.route('/login', methods=['GET'])
def login_page():
    return render_template('qsdzz_login.html')


@web.route('/qsdzz', methods=['GET'])
def home():
    return render_template('qsdzz.html')


@web.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # 请在下方写你的代码:验证用户名和密码正确之后，重定向到首页/qsdzz，否则重定向到登录页。


web.run(host='127.0.0.1', port=5000)
