#!/usr/bin/python
#Winston Venderbush
import random #functions
from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__) 
app.secret_key = '\xe9$=P\nr\xbc\xcd\xa5\xe5I\xba\x86\xeb\x81L+%,\xcb\xcb\xf46d\xf9\x99\x1704\xcd(\xfc'

@app.route("/")
def root():
	return render_template('home.html', title = "Home")

@app.route("/authenticate", methods = ['POST'])
def auth():
    user = request.form['user']
    pasz = request.form['pass']
    hashpass = hashlib.sha224(pasz).hexdigest()
    status = functions.register(user,pasz)
    if 'login' in request.form:
        if functions.signin(user,pasz):
            session['username'] = user
            return redirect(url_for('root'))
        else:
            return render_template('home.html',message = 'Login Failed')
    else:
        if status == 1:
            return render_template('home.html',
                                   message = 'Registration failed. User already exists.')
        elif status == 2:
            return render_template('home.html',
                                   message = 'Registration failed. Username and password too short.')
        elif status == 3:
            return render_template('home.html',
                                   message = 'Registration failed. Password too short')
        elif status == 4:
            return render_template('home.html',
                                   message = 'Registration failed. Username too short')
        elif status == 5:
            return render_template('home.html',
                                   message = 'Registration failed. Username or password too short')
        else:
            return render_template('home.html',
                                   message = 'Registration successful')
        
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
    return render_template('account.html', title =  username+ "'s Account", user = username);

@app.route('/story/<int:post_id>')
def show_post(post_id):
    return render_template('post.html', title = "", postid = post_id)

@app.route("/library")
def library():
    return render_template('library.html', title = "Library")

if __name__ == "__main__":
    app.debug = True 
    app.run()
