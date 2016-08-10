import random
import datetime
from datetime import datetime
from time import strftime


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():

	if not session.has_key('usergold'):
		session['usergold']=0
	if not session.has_key('activities'):
		session['activities']=[]
		session['classname']=[]
		session['dictionlen']=len(session['activities'])
	print session['usergold']
	return render_template("ninjagold.html", usergold=session['usergold'])


@app.route('/process_money', methods=['POST'])
def guess():
	time=datetime.now().strftime("%Y-%m-%d %I:%M")
	session['check'] = True
	if request.form['building'] == 'farm':

		money=random.randint(10,20)
		session['usergold'] += money
		session['activities'].append('Earned ' + str(money) + ' golds from the farm!' + '( ' + str(time) + ')')
		session['classname'].append("greentext")
	elif request.form['building'] == 'cave':
		money = random.randint(5,10)
		session['usergold'] += money
		session['activities'].append('Earned ' + str(money) + ' golds from the cave!' + '( ' + str(time) + ')')
		session['classname'].append("greentext")
	elif request.form['building'] == 'house':
		money = random.randint(2,5)
		session['usergold'] += money
		session['activities'].append('Earned ' + str(money) + ' golds from the house!' + '( ' + str(time) + ')')
		session['classname'].append("greentext")
	elif request.form['building'] == 'casino':
		money= random.randint(-50,50)
		if money >= 0: 
			session['usergold'] += money
			session['activities'].append('Earned ' + str(money) + ' golds from the casino!' + '( ' + str(time) + ')')
			session['classname'].append("greentext")
		else:
			session['usergold'] += money
			session['activities'].append('Entered a casino and lost ' + str(money) + ' golds... Ouch.. ' + '( ' + str(time) + ')')
			session['classname'].append("redtext")

	session['dictionlen']+=1
	
	return redirect('/')


 

app.run(debug=True)