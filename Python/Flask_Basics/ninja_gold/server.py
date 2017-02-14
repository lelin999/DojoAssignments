import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'KeyOne'

@app.route('/')
def index():
	if "gil" not in session:
		session['gil'] = 0
	if "log " not in session:
		session['log'] = ""
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def clicked():
	gil_earned = []
	if request.form['building'] == 'farm':	
		session['farm_gil'] = int(random.randrange(10,21))
		session['farm_gil_earned'] = "Earned {} gil from the farm!".format(session['farm_gil'])
		# above line works
		session['log'] += session['farm_gil_earned'] 
		session['gil'] += session['farm_gil']
	elif request.form['building'] == 'cave':
		session['cave_gil'] = int(random.randrange(5,11))
		session['cave_gil_earned'] = "Earned {} gil from the cave!".format(session['cave_gil'])
		session['log'] += session['cave_gil_earned']
		session['gil'] += session['cave_gil']
	elif request.form['building'] == 'house':
		session['house_gil'] = int(random.randrange(2,6))
		session['house_gil_earned'] = "Earned {} gil from the house".format(session['house_gil'])
		session['log'] += session['house_gil_earned']
		session['gil'] += session['house_gil']
	elif request.form['building'] == 'casino':
		session['casino_gil'] = int(random.randrange(-50, 50))
		if session['casino_gil'] < 0:
			session['casino_gil_made'] = "Unlucky...Lost {} gil from the casino :(".format(session['casino_gil'] * -1)
		elif session['casino_gil'] == 0:
			session['casino_gil_made'] = "Not unlucky, but not lucky either...Didn't make any gil!"
		else:
			session['casino_gil_made'] = "How lucky! Made {} gil from the casino!".format(session['casino_gil'])
		session['log'] += session['casino_gil_made']
		session['gil'] += session['casino_gil']
	return redirect('/')

app.run(debug=True)