from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
@app.route('/ninja')
def ninjas():
	ninjas = True
	return render_template('ninjacolor.html', ninjas = ninjas)
@app.route('/ninja/<picture>')
def ninjacolor(picture):
	if picture == "blue":
		filename="leonardo.jpg"
	elif picture == "orange":
		filename="michelangelo.jpg"
	elif picture == "red":
		filename="raphael.jpg"
	elif picture == "purple":
		filename="donatello.jpg"
	else:
		filename="notapril.jpg"
	return render_template("ninjacolor.html", name=filename)
app.run(debug=True)