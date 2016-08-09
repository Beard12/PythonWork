from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'



@app.route('/')
def index():
	if not session.has_key('count'):
		session['count']=1
		return render_template("user.html", counter = session['count'])
	session['count']+=1
  	return render_template("user.html", counter = session['count'])

@app.route('/two', methods=['POST'])
def add_two():
	session['count']+=1
	return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
	session['count']=0
	return redirect("/")
 

app.run(debug=True)