from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret2'

@app.route('/')
def index():
	try:
		session['counter'] +=1
	except KeyError:
		session['counter'] = 1
	return render_template("index.html")

@app.route('/', methods=['POST'])
def clicked():
	if request.form['button'] == 'Ninja +2':
		session['counter'] += 2
	elif request.form['button'] == 'Reset':
		session['counter'] = 0
	return render_template("index.html")

app.run(debug=True)