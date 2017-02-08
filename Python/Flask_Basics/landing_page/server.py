from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja')
def shuriken():
	return render_template("ninja.html")

@app.route('/dojos/new')
def form_in_new():
	return render_template("new_dojo.html")

app.run(debug=True)