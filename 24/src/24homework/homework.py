from flask import Flask, render_template, request, redirect, jsonify
from datetime import timedelta

web = Flask(__name__)

web.debug = True
web.send_file_max_age_default = timedelta(seconds=1)


@web.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    response = jsonify({'code': 0, 'data': 'success'})
    # 请在下方写你的代码：设置cookie


@web.route('/login', methods=['GET'])
def login_page():
    # 请在下方写你的代码：获取cookie并自动登录

    return render_template('login.html')


@web.route('/index', methods=['GET'])
def home():
    return render_template('index.html')


web.run(host='127.0.0.1', port=5000)
