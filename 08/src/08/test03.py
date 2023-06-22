from flask import Flask, render_template

web = Flask(__name__)

activity = None
news = '【活动】一份耕耘！一份收获！'


@web.route('/wiki')
def wiki():
    # 在下方写你的代码：返回模板变量
    return render_template('wiki.html')


web.run(host='127.0.0.1', port=8003)
