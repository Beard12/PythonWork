from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'Verysecretkeysupersecret'


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
  

	name = request.form['name']
	dojo = request.form['dojlocation']
	lang = request.form['favlang']
	comment = request.form['comment']

	print len(request.form['comment']) 

  	if len(request.form['name']) < 1 and len(request.form['comment']) < 1:
  		flash("Name and comment field cannot be empty please enter the required information!")
  		return redirect('/')
  	elif len(request.form['name'])< 1:
  		flash("Name field cannot be empty")
  		return redirect('/')
  	elif len(request.form['comment'])< 1:
  		flash("Comment field cannot be empty")
  		return redirect('/')
  	elif len(request.form['comment'])>120:
  		flash("You can type no more than 120 characters in the comment field")
  		return redirect('/')

	return render_template("result.html", name = name, dojo= dojo, lang= lang, comment=comment)

app.run(debug=True)