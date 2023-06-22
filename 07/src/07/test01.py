from flask import Flask,render_template


web = Flask(__name__)

web.debug = True

@web.route('/acre',methods=['GET'])
def acre():
	return render_template('test_acre.html')


@web.route('/startrek',methods=['GET'])
def startrek():
	return render_template('test_startrek.html')


web.run(host='127.0.0.1',port=8001)
