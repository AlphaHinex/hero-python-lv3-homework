from flask import Flask, render_template

# 创建Falsk应用
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


# 请在下方写你的代码


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
