from flask import Flask, render_template

# 创建Flask应用
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# 在下方完成登录页


# 启动服务器程序
app.run(host='127.0.0.1', port=8011)
