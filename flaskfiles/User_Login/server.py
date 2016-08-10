from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
mysql = MySQLConnector(app,'users')
bcrypt = Bcrypt(app)
app.secret_key = 'secret for realssss'

@app.route('/')
def index():
	pass
	return render_template("index.html")


@app.route('/register', methods=['POST'])
def create():
	if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
		flash("Your first or last name has to be at least 2 characters.", "nameerror")
		return redirect('/')
	elif not (request.form['first_name']).isalpha() or not (request.form['last_name']).isalpha():
		flash("Your first orlast name cannot contain numbers", "nameerror")
		return redirect('/')
		
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!", "emailerror")
		return redirect('/')

	if request.form['password'] != request.form['cf_password']:
		flash("Both password fields need to be equivalent", "passworderror")
		return redirect('/')
	elif len(request.form['password']) < 9:
		flash("Your password needs to be longer than 8 characters", "passworderror")
		return redirect('/')
	
	



	password = request.form['password']
	pw_hash = bcrypt.generate_password_hash(password)
	query = "INSERT INTO users (first_name, last_name, email, password) VALUES(:first_name, :last_name, :email, :password)"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'password': pw_hash
	}
	mysql.query_db(query, data)

	return render_template("success.html", success="Thank you for registering " + request.form['first_name'] + " " + request.form['last_name'] + ". We look forward to serving your business needs!")

@app.route('/login', methods=['POST'])
def login():

	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address please enter again", "loginerror")
		return redirect('/') 
	email = request.form['email']
	password = request.form['password']
	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = { 'email': email }
	user = mysql.query_db(query, data) 
	if bcrypt.check_password_hash(user[0]['password'], password):
		return render_template("success.html", success="Welcome back " + user[0]['first_name'] + " " + user[0]['last_name'] + ". Enjoy your stay. We hope you never leave!")
	else:
		flash("Login failure. Your password or email address did not match our records please try again or register if you do not have an account with us.", "loginerror")
		return redirect("/")
app.run(debug=True)







