from flask import Flask, render_template, request

web = Flask(__name__)


@web.route('/test', methods=['GET'])
def login_page():
    return render_template('test02.html')


@web.route('/test', methods=['POST'])
def login():
    # 在下方写你的代码：获取请求参数用户名和密码
    text = request.form.get('text')
    return "欢迎您%s"%text


web.run(host='127.0.0.1', port=8002)
