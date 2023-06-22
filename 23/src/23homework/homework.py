from flask import Flask, render_template, request, redirect

web = Flask(__name__)

web.debug = True


@web.route('/', methods=['GET'])
def dilidili():
    return render_template('d_home.html')


@web.route('/login', methods=['GET'])
def d_login_page():
    # 在下方写你的代码（获取cookie，判断cookie）：
    if request.cookies.get('auto_login') == 'yes':
        return redirect('/')
    else:
        return render_template('d_login.html')


@web.route('/login', methods=['POST'])
def d_login():
    username = request.form.get('username')
    password = request.form.get('password')

    response = redirect('/')
    # 在下方写你的代码（设置cookie）：
    response.set_cookie('auto_login','yes')

    return response


web.run(host='127.0.0.1', port=5000)
