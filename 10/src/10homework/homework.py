from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

role = {'name': '美人鱼', 'location': '强大的团队辅助，有效保护生存能力差的单位。'}

# 请在下方写你的代码


app.run(host='127.0.0.1', port=5000)
