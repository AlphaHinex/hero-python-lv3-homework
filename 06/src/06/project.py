from flask import Flask, render_template


project = Flask(__name__)


@project.route('/', methods=['GET'])
def baidu():
    return render_template('baidu.html')


@project.route('/search', methods=['GET'])
def search():
    # 在下方写你的代码：获取GET请求传递的数据

    return ''


project.run(host='127.0.0.1', port=8000)
