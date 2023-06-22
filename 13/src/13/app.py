from flask import Flask, render_template, request

# 创建Falsk应用
app = Flask(__name__)
app.debug = True

# 已经注册用户的列表
users = [
    {'id': '1', 'username': 'xiaotong', 'password': '123456'},
    {'id': '2', 'username': 'xiaomei', 'password': '000000'},
    {'id': '3', 'username': 'xiaoming', 'password': '888888'}
]

def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，
        如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None

# 下方完成你的代码：设置访问路径：/user/login

    
    
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
