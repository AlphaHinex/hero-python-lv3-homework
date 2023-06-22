from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# 调试模式
app.debug = True
app.secret_key = '123456'


@app.route('/')
def index():
    return render_template('test01.html')


@app.route('/save', methods=['POST'])
def save():
    money = int(request.form.get('money'))

    # 在下方写你的代码：设置session，保存用户存款金额
    if 'money'not in session:
        session['money'] = [money]
    else:
        h = session['money']
        h.append(money)
        session['money'] = h

    return '成功存储了%s元' % money

@app.route('/query', methods=['GET'])
def query():
    # 在下方写你的代码：获取session,计算总金额
    h = session.get('money')
    count = sum(h)
    return '余额:%s元' % count
if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=8001
    )
