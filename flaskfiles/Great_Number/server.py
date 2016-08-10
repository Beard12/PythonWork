import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():

	if not session.has_key('rannumber'):
		session['rannumber']=random.randint(1,100)
		return render_template("game.html", hidden= "hidden", hidden1= "hidden")
	elif not session.has_key('number'):
	 	return render_template("game.html", hidden= "hidden", hidden1= "hidden")
	elif session['number'] < str(session['rannumber']):
		session.pop('number')
		return render_template("game.html", message="Too Low", hidden = "", hidden1= "hidden")
	elif session['number'] > str(session['rannumber']):
		session.pop('number')
		return render_template("game.html", message= "Too High", hidden = "", hidden1= "hidden")
	elif session['number'] == str(session['rannumber']):
		return render_template("game.html", hidden1 = "", hidden="hidden")

@app.route('/guess', methods=['POST'])
def guess():
	session['number'] = request.form['guess']
	return redirect('/')

@app.route('/playagain', methods=['POST'])
def playagain():
	session.pop('rannumber')
	session.pop('number')
	return redirect("/")
 

app.run(debug=True)