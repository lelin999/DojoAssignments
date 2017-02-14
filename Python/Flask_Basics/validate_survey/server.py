from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "poop"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
	loc = request.form['loc']
	language = request.form['language']
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/')
	else:
		name = request.form['name']
	if len(request.form['comment']) > 120:
		flash("Comment is too damn long!")
		return redirect('/')
	else: 
		comment = request.form['comment']
	return render_template("results.html", name=name, loc=loc, language=language, comment=comment)

app.run(debug=True)