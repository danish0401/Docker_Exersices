# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
import re
import mysql.connector

app = Flask(__name__)

app.secret_key = 'Danish.123'

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor,connection = connect()
		sqlcmd="""SELECT * FROM geeklogin.accounts WHERE username = %s AND password = %s"""
		value=(username, password, )
		cursor.execute(sqlcmd, value)
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account[0]
			session['username'] = account[1]
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor,connection = connect()
		sqlcmd="SELECT * FROM geeklogin.accounts WHERE username = %s"
		value=(username, )
		cursor.execute(sqlcmd, value)
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			sqlcmd="""INSERT INTO geeklogin.accounts VALUES (NULL, %s, %s, %s)"""
			value=(username, password, email, )
			cursor.execute(sqlcmd, value)
			connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

def connect():
	config = {
        'user': 'root',
        'password': 'password',
        'host': 'db',
        'port': '3306',
        'database': 'geeklogin'
   		}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	return cursor,connection

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)