from flask import Flask

app = Flask(__name__)

app.debug = True


@app.route('/test02')
def test02():
    # 在下方写你的代码：使用render_template函数，返回test02.html
    return '111'


app.run(host='127.0.0.1', port=8001)
