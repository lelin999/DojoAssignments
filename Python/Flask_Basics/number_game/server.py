import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'KeyOne'

@app.route('/')
def index():
	try: 
		session['setValue']
	except KeyError:
		session['setValue'] = random.randrange(1,101,1)
	return render_template("index.html")

@app.route('/', methods=['POST'])
def clicked():
	number = int(request.form['number'])
	if request.form['button'] == 'Guess':
		if number > int(100) or number < int(1):
			return render_template('index.html', message="Pick a number in the range you dingdong")
		elif number < int(session['setValue']):
			return render_template('index.html', message="Too low!")
		elif number > int(session['setValue']):
			return render_template('index.html', message="Too high!")
		elif number == int(session['setValue']):
			session.pop('setValue')
			return render_template('index.html', message="JUST RIGHT")

app.run(debug=True)