from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
	print "Got Post Info"
	name = request.form['name']
	loc = request.form['loc']
	language = request.form['language']
	comment = request.form['comment']
	return render_template("results.html", name=name, loc=loc, language=language, comment=comment)
	# return redirect('/results')

app.run(debug=True)