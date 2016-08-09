from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re


app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')
app.secret_key = 'secret for realssss'

@app.route('/')
def index():
	query = "SELECT * FROM friends"                          
	friends = mysql.query_db(query)                          
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES(:first_name, :last_name, :email, NOW())"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id = :specific_id"
	data = {'specific_id': id}
	friend = mysql.query_db(query, data)
	return render_template('edit.html', friends=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
	data = {
			'first_name': request.form['first_name'], 
			'last_name':  request.form['last_name'],
			'email': request.form['email'],
			'id': id
           }
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)
	return redirect('/')


app.run(debug=True)


















app.run(debug=True)