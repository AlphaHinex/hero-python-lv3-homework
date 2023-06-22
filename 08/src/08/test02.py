from flask import Flask, render_template

web = Flask(__name__)
web.debug = True

inform = '【资料站开张福利】快来和熊猫菌一起玩吧~'


@web.route('/yrzx')
def yrzx():
    # 在下方写你的代码：返回模板变量
    return render_template('yrzx.html')


web.run(host='127.0.0.1', port=8012)
