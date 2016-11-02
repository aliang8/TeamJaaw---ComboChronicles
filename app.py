#!/usr/bin/python
#Winston Venderbush
import random
from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__) 


@app.route("/")
def root():
	return render_template('test.html', title = "Home")

@app.route("/login")
def login():
	return render_template('index.html', title = "Home", flag = "login")

@app.route("/logout")
def logout():
	return redirect(url_for("root"))

@app.route("/newsubmit")
def newsubmit():
	return render_template('newsubmit.html', title = "Submit")

@app.route("/posts")
def posts():
    return render_template('posts.html')
    
@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/library")
def library():
    return render_template('library.html')

if __name__ == "__main__":
    app.debug = True 
    app.run()
