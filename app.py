import random, functions, hashlib, sqlite3, auth, stories
from flask import Flask, render_template, session, redirect, url_for, request
from datetime import datetime

app = Flask(__name__) 
app.secret_key = '\xe9$=P\nr\xbc\xcd\xa5\xe5I\xba\x86\xeb\x81L+%,\xcb\xcb\xf46d\xf9\x99\x1704\xcd(\xfc'

f = 'data/stories.db'

@app.route("/", methods = ['POST','GET'])
def home():
	return render_template('home.html', title = "ComboChronicles")

@app.route("/login/", methods = ['POST','GET'])
def login():
	return render_template('login.html', title = "login")

@app.route("/authenticate/", methods = ['POST','GET'])
def authenticate():
	if request.method == 'POST':
		username = request.form['user']
		password = request.form['pass']
		hashpass = hashlib.sha224(password).hexdigest()
		if 'login' in request.form:
			if auth.login(username,password):
				session['username'] = user
				return render_template('home.html',message = 'Login Successful')
			else:
				return render_template('home.html',message = 'Login Failed')
		else:
			if auth.register(username,password):
				return render_template('home.html',message = 'Registration Successful')
			else:
				return render_template('home.html',message = 'Registration Failed')
	else:
		return redirect(url_for("home"))
	
@app.route("/logout/")
def logout():
	return redirect(url_for("home"))

@app.route("/newentry/", methods=['GET', 'POST'])
def newentry():
	if request.method == 'POST':
		title = request.form['title']
		entry = request.form['entry']
		stories.newEntry(title,entry)
		return redirect(url_for("newentry"))
	else:
		return render_template('newentry.html', title = "Create Story")
	
@app.route("/posts/")
def posts():
	return render_template('posts.html')
	
@app.route("/account/")
def account():
	return render_template('account.html', title = "My Account")

@app.route('/user/<username>/')
def show_user_profile(username):
	return render_template('account.html', title =  username+ "'s Account", user = username);

@app.route('/story/<int:post_id>/')
def show_post(post_id):
	return render_template('post.html', title = "", postid = post_id)

@app.route("/library/")
def library():
	return render_template('library.html', title = "Library")

if __name__ == "__main__":
	app.debug = True 
	app.run()

db.commit()
db.close()
