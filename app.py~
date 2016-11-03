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


if __name__ == "__main__":
    app.debug = True 
    app.run()