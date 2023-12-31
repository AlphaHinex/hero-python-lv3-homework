from flask import Flask, render_template, request, redirect, jsonify

# 创建Flask应用
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
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    for user in users:
        if user['username'] == username:
            return user
    return None


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 在下方写你的代码：获取cookie，填充用户名
        username = request.cookies.get('username','')
        
        return render_template('login.html',username = username)
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = find(username)
        if user is None:
            return render_template('login.html', username=username, user_msg='用户名不存在')
        if user['password'] != password:
            return render_template('login.html', username=username, pass_msg='密码错误，请重试')
        # 在下方写你的代码：设置cookie，将用户名保存在Cookie中，并返回response
        response = redirect('/')
        response.set_cookie('username',username,max_age = 600)
        return response
        


@app.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 获取提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 判断用户名是否已存在
        user = find(username)
        if user is not None:
            return jsonify({'status': 'failure', 'msg': '该用户名已被注册'})

        # 注册成功，保存在字典中
        user = {'id': len(users) + 1, 'username': username, 'password': password}
        users.append(user)

        # 注册成功，重定向到登录页
        return jsonify({'status': 'success', 'msg': '恭喜注册成功'})


@app.route('/')
def index():
    # 在下方写你的代码：获取cookie，填充用户名

    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# 启动服务器程序
app.run(host='127.0.0.1', port=8000)
