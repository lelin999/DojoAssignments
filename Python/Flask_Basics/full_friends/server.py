from flask import Flask, render_template, redirect, request, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')
app.secret_key = 'iknowwhatyoudid'

@app.route('/')
def index():
	return render_template("index.html")

app.run(debug=True)