from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
app.secret_key = "IsItASecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def processing():
	if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid!")
		return redirect('/')
	else:
		data = {
			'email': request.form['email']
		}
		query = "INSERT INTO user_emails (email, created_at, updated_at) VALUES(:email, NOW(), NOW())"
		query2 = "SELECT id, email FROM user_emails"
		mysql.query_db(query, data)
		results = mysql.query_db(query2, data)
		return render_template('success.html', all_user_emails=results)

app.run(debug=True)