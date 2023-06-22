# coding=utf-8
from flask import Flask,render_template

app = Flask(__name__)


# 请在下方写你的代码：打开调试模式

@app.route('/')
def hello():
    # 请在下方写你的代码：放回页面
    return render_template('')


app.run(host='127.0.0.1',port=8004)
