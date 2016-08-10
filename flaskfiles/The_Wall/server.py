from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
mysql = MySQLConnector(app,'thewall_db')
bcrypt = Bcrypt(app)
app.secret_key = 'secret for realssss'

@app.route('/')
def index():
	if not session.has_key('userid'):
		return render_template("index.html")
	else:
		return redirect("/wall")


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
	query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'password': pw_hash
	}
	mysql.query_db(query, data)

	email = request.form['email']
	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = {'email': email }
	user = mysql.query_db(query,data)
	session['last_name'] = user[0]['last_name']
	session['first_name']= user[0]['first_name']
	session['userid'] = user[0]['id']

	return redirect("/wall")
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
		session['last_name'] = user[0]['last_name']
		session['first_name']= user[0]['first_name']
		session['userid'] = user[0]['id']
		return redirect('/wall')

		
	else:
		flash("Login failure. Your password or email address did not match our records please try again or register if you do not have an account with us.", "loginerror")
		return redirect('/')
@app.route('/wall')
def wall():
	if not session.has_key('userid'):
		return redirect('/')
	query = "SELECT messages.user_id, users.first_name, users.last_name, messages.id, messages.message, messages.created_at FROM users JOIN messages ON user_id = users.id ORDER BY messages.created_at DESC"
	messages= mysql.query_db(query)
	query = "SELECT users.first_name, users.last_name,comments.message_id, comments.comment, comments.created_at FROM users JOIN comments ON user_id = users.id ORDER BY comments.created_at ASC"
	comments= mysql.query_db(query)

	return render_template("thewall.html", messages = messages, comments=comments)

@app.route('/logoff', methods=['POST'])
def logoff():
	session.clear()
	return redirect('/')

@app.route('/postmessage', methods=['POST'])
def postmessage():

	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES(:user_id, :message, NOW(), NOW())"
	data = {
			'user_id': session['userid'],
			'message': request.form['messagecontent']
	}
	mysql.query_db(query, data)
	return redirect('/wall')
@app.route('/postcomment/<id>', methods=['POST'])
def postcomment(id):

	query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :message_id, :comment, NOW(), NOW())"
	data = {
		'user_id': session['userid'],
		'comment': request.form['commentcontent'],
		'message_id': id

	}
	mysql.query_db(query, data)
	return redirect('/wall')

# josh@alley.com
# Jalapeno1

#caityilek@gmail.com
#nottelling






app.run(debug=True)







