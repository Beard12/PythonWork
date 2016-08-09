from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'secret for reals'



@app.route('/')
def index():
	
	                   
	return render_template('index.html', hidelist= True, error ="error") 
@app.route('/success', methods=['POST'])
def create():
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid")
		return redirect('/')
	else:
		query = "INSERT INTO emails (address, created_at, updated_at) VALUES(:address,NOW(), NOW())"
		data = {
				'address': request.form['email']
		}
		mysql.query_db(query, data)
		listing = "SELECT * FROM emails"                          
		emails = mysql.query_db(listing)
		flash("The email address you entered (" + request.form['email'] + ") is a valid email address! Thank you!")
	return render_template('index.html', hidelist=False,emails=emails, error="noerror")

@app.route('/delete', methods=['POST'])
def delete():
	query = "DELETE FROM emails WHERE address = :address"
	data = {'address': request.form['email']}
	mysql.query_db(query, data)

	listing = "SELECT * FROM emails"                          
	emails = mysql.query_db(listing)
	return render_template('index.html', hidelist=False, emails=emails, error="error")
@app.route('/goback', methods=['POST'])
def goback():
	return redirect('/')

app.run(debug=True)