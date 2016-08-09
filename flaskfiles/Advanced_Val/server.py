from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)

def passwordCheck(strin):
	num = 0
	upcase = 0
	for x in xrange(len(strin)):
		if strin[x].isdigit():
			num +=1
		elif strin[x].isupper():
			upcase+=1
	if num > 0 and upcase > 0:
		return True
	else: 
		return False


app.secret_key = "ThisIsSecret! Really secret"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['fname']) < 1:
		flash("First name cannot be blank", "fnameerror")
	elif not (request.form['fname']).isalpha():
		flash("First name cannot include numbers", "fnameerror")
	else:
		flash("Success in saving your first name", "fnameerror")

	if len(request.form['lname']) < 1:
		flash("Last name cannot be blank", "lnameerror")
	elif not (request.form['fname']).isalpha():
		flash("Last name cannot include numbers", "lnameerror")
	else:
		flash("Success in saving your last name", "lnameerror")

	if request.form['password'] != request.form['confirmpassword']:
		flash("Both password fields need to be equivalent", "passworderror")	
	elif len(request.form['password']) < 9:
		flash("Your password needs to be longer than 8 characters", "passworderror")
	elif not passwordCheck(request.form['password']):
		flash("Your password needs to have at least one uppercase character and one number", "passworderror")
	else:
		flash("Success in saving your password", "passworderror")

	if len(request.form['email']) < 1:
		flash("Email cannot be blank!", "emailerror")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!", "emailerror")
	else:
		flash("Success in saving your email", "emailerror")

	return redirect('/')
app.run(debug=True)