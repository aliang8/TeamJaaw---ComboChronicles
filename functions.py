import sqlite3 
import hashlib

#CONNECT DATABASE
f= "data/stories.db"
db = sqlite3.connect(f)
c = db.cursor()



#Initialize databases. Only works once.
def initializeTables():    
	c.execute("CREATE TABLE IF NOT EXISTS accounts (user TEXT, pass VARCHAR(60))")
	c.execute("CREATE TABLE IF NOT EXISTS entries (storyid INTEGER, content TEXT, entrynum INTEGER, contributor TEXT, timestamp INTEGER)")
	c.execute("CREATE TABLE IF NOT EXISTS stories (storyid INTEGER, title TEXT)")


#========================================================GENERIC CREATE FUNCTIONS=============================================================
#Need to add functions that handles all these inputs
def newAccount(username, password):
    hashpass = hashlib.sha512(password).hexdigest()
    c.execute("INSERT INTO accounts VALUES('%s', %s)" % (username, hashpass))

def newStory(title, storyid, content, contributor, timestamp):
    c.execute("INSERT INTO entries VALUES(%s, '%s', %s, '%s', %s)" % (storyid, content, 1, contributor, timestamp))
    c.execute("INSERT INTO stories VALUES(%s, '%s')" % (storyid, title))

def newEntry(storyid, content, entrynum, contributor):
    c.execute("INSERT INTO entries VALUES(%s, '%s', %s, '%s', %s)" % (storyid, content, entrynum, contributor, timestamp))
#=============================================================================================================================================


#===========================================================OUTPUT FUNCTIONS=================================================================

#Returns a list of all posts a user has contributed to
def returnContributed(username):
    data = c.execute("SELECT DISTINCT storyid FROM entries WHERE entries.contributor == %s ORDER BY timestamp ASC" % (username))
    stories = []
    for item in data:
	stories.append(item[0])	#Item[0] = storyid
    return stories
    
#Returns one entire story as a string
def returnStory(storyid):
    data = c.execute("SELECT * FROM entries WHERE entries.storyid == %s ORDER BY entrynum ASC" % (storyid))
    story = []
    for item in data:
	story.append(item[1]) # Item 1 = Story content of one entry
    return story

#Returns a list of all contributors to a story in order
def returnContributors(storyid):
    data = c.execute("SELECT * FROM entries WHERE entries.storyid == %s ORDER BY entrynum ASC" % (storyid))
    contributors = []
    for item in data:
	contributors.append(item[3]) #Item[3] = contributor
    return contributors

#==============================================================================================================================================



#=============================================================FOR DISPLAY FUNCTIONS============================================================

#Returns a tuple (All titles of stories user contributed to, 
#                 all stories contents of the contributed to stories,
#                 all contributors of the respective stories)
#
# Tuple represented in components : ([], [][], [][])
# For my account/my stories page
def myStoryList(username):
    myStories = returnContributed(username)
    allStories = []
    allContributors = []
    allTitles = []

    for storyid in myStories:
	allStories.append(returnStory(storyid))
	allContributors.append(returnContributors(storyid))

    	data = c.execute("SELECT * FROM stories WHERE stories.storyid == %s" % (storyid))
	allTitles.append(data.fetchone()[1]) #First (and only) entry fetch. fetch[1] = title
	
    return (allTitles, allStories, allContributors)

#Returns the list of stories for the main page
#UNFINISHED
def menuStories(numStories):
    #data = c.execute("SELECT ")

#=============================================================================================================================================

def signin(username,password):
    hashpass = hashlib.sha24(password).hexdigest()
    users = c.execute("SELECT pass FROM users WHERE user == %s" % (username))
    if users and users[0] == hashpass:
        return True
    else:
        return False

def register(username,password):
    user = c.execute("SELECT user FROM users WHERE user == %s" % (username))
    if user:
        return 1
    elif len(username) < 3 and len(password) < 3:
        return 2
    elif len(password) < 3
        return 3
    elif len(username) < 3
        return 4
    elif not(username.isalum()) or not(password.isalum()):
        return 5
    else:
        c.execute("INSERT INTO users VALUES (%s,%s)" % (username,password))
        return 6


