from flask import Flask, render_template, request
import ssl, startools

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
app.debug = True


@app.route('/star', methods=['GET'])
def star():
    # 在下方写你的代码：获取星座数据

    return render_template('star_home.html')


@app.route('/sx', methods=['GET'])
def sx():
    sx = startools.sx_list()
    return render_template('sx_home.html', sx=sx)


@app.route('/star/fortune', methods=['GET'])
def star_fortune():
    # 在下方写你的代码:获取选择的星座并讲星座信息返回给前端

    return render_template('star_fortune.html')


@app.route('/sx/fortune', methods=['GET'])
def sx_fortune():
    sx = request.args.get('sx')
    fortune = startools.sx_fortune(sx)
    return render_template('sx_fortune.html', fortune=fortune)


app.run(host='127.0.0.1', port=8000)
