#!/usr/bin/python
#Winston Venderbush
import random #functions
from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__) 
app.secret_key = '\xe9$=P\nr\xbc\xcd\xa5\xe5I\xba\x86\xeb\x81L+%,\xcb\xcb\xf46d\xf9\x99\x1704\xcd(\xfc'

@app.route("/")
def root():
	return render_template('home.html', title = "Home")

@app.route("/login")
def login():
	return render_template('login.html', title = "Login")

@app.route("/logout")
def logout():
	return redirect(url_for("root"))

@app.route("/newsubmit", methods = ['POST'])
def newsubmit():
	title = request.form['title']
	entry = request.form['entry']
	if 'submission' in request.form:
		functions.newEntry(title,entry)
		return redirect(url_for("root"))
	else:
		return render_template('newsubmit.html', title = "Create Story")

@app.route("/posts")
def posts():
    return render_template('posts.html')
    
@app.route("/account")
def account():
    return render_template('account.html', title = "My Account")

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('account.html', title = "My Account", user = username);

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return render_template('account.html', title = "My Account", postid = post_id)

@app.route("/library")
def library():
    return render_template('library.html', title = "Library")

if __name__ == "__main__":
    app.debug = True 
    app.run()
