from flask import Flask, render_template

web = Flask(__name__)


@web.route('/', methods=['GET'])
def index():
    return render_template('order.html')


@web.route('/order', methods=['GET'])
def order():
    # 在下方写你的代码：获取GET请求传递的数据


    return ''


web.run(host='127.0.0.1', port=8001)
