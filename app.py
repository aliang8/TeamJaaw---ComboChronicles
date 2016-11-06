import random, functions, hashlib, sqlite3, time
from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__) 
app.secret_key = '\xe9$=P\nr\xbc\xcd\xa5\xe5I\xba\x86\xeb\x81L+%,\xcb\xcb\xf46d\xf9\x99\x1704\xcd(\xfc'

f = 'data/stories.db'
db = sqlite3.connect(f)
c = db.cursor()

@app.route("/", methods = ['POST','GET'])
def new():
	return render_template('home.html', title = "ComboChronicles", titles_stories = zip(functions.menuStories(10)[0], functions.menuStories(10)[1], functions.menuStories(10)[2], functions.menuStories(10)[3]))

@app.route("/<message>", methods = ['POST','GET'])
def home(message):	
	return render_template('home.html', title = "ComboChronicles", message = message, titles_stories = zip(functions.menuStories(10)[0], functions.menuStories(10)[1], functions.menuStories(10)[2], functions.menuStories(10)[3])) 

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
			if functions.login(username,password):
				session['username'] = username
				return redirect(url_for("home",message = "Login Successful"))
			else:
				return redirect(url_for("home",message = "Login Failed"))
		else:
			if functions.register(username,password):
				return redirect(url_for("home",message = "Registration Successful"))
			else:
				return redirect(url_for("home",message = "Registration Failed"))
	else:
		return redirect(url_for("login"))
	
@app.route("/logout/")
def logout():
        session.pop('username')
	return redirect(url_for("home", message = "Successfully logged out"))

# @app.route("/newentry/", methods=['GET','POST'])
# def newentry():
# 	if request.method == 'POST':
# 		storyTitle = request.form.keys()[1]
# 		storyID = functions.getstoryID(storyTitle)
# 		entry = request.form['entry']
# 		functions.newEntry(storyID,entry,session['username'],time.strftime("%Y-%m-%d %H:%M:%S"))
# 		return redirect(url_for("home", message = "Awesome, new entry for " + storyTitle + " submitted!"))
# 	else:
# 		storyTitle = request.args.get('title')
# 		return render_template('newentry.html', title = "New Entry", story = storyTitle)

@app.route("/newentry/<storyid>", methods=['GET','POST'])
def newentry(storyid):
	if request.method == 'POST':
		storyTitle = request.form.keys()[1]
		storyID = storyid
		entry = request.form['entry']
		functions.newEntry(storyID,entry,session['username'],time.strftime("%Y-%m-%d %H:%M:%S"))
		return redirect(url_for("home", message = "Awesome, new entry for " + storyTitle + " submitted!"))
	else:
		storyTitle = request.args.get('title')
		return render_template('newentry.html', title = "New Entry", story = storyTitle)


@app.route("/newstory/", methods=['GET','POST'])
def newstory():
	if request.method == 'POST':
		title = request.form['title']
		story = request.form['story']
		functions.newStory(title,story,session['username'],time.strftime("%Y-%m-%d %H:%M:%S"))
		return redirect(url_for('home', message = "Awesome, you started a new story!"))
	else:
		return render_template('newstory.html', title = "Create Story")
	
@app.route("/posts/")
def posts():
	return render_template('posts.html')
	
@app.route("/account/")
def account():
	return render_template('account.html', title = "My Account", userstories = functions.myStoryListDict(session['username']))

@app.route('/user/<username>/')
def show_user_profile(username):
	return render_template('account.html', title =  username+ "'s Account", user = username, userstories = functions.myStoryListDict(user))

@app.route('/story/<int:post_id>/')
def show_post(post_id):
	return render_template('post.html', title = "", postid = post_id)

@app.route("/library/")
def library():
	return render_template('library.html', title = "Library", titles = functions.libraryStories()[0], entries = functions.libraryStories()[2])

if __name__ == "__main__":
	app.debug = True 
	app.run()
	functions.initializeTables()
