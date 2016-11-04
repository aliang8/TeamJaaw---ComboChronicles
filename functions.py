import sqlite3 
import hashlib

#CONNECT DATABASE
f= "data/stories.db"
db = sqlite3.connect(f)
c = db.cursor()



#Initialize databases. Only works once.
def initializeTables():    
	c.execute("CREATE TABLE IF NOT EXISTS accounts (user TEXT, pass VARCHAR(60))")
	c.execute("CREATE TABLE IF NOT EXISTS entries (storyid INTEGER, content TEXT, entrynum INTEGER, contributor TEXT)")
	c.execute("CREATE TABLE IF NOT EXISTS stories (storyid INTEGER, title TEXT)")


#========================================================GENERIC CREATE FUNCTIONS=============================================================
#Need to add functions that handles all these inputs
def newAccount(username, password):
    hashpass = hashlib.sha512(password).hexdigest()
    c.execute("INSERT INTO accounts VALUES('%s', %s)" % (username, hashpass))

def newStory(title, storyid, content, contributor):
    c.execute("INSERT INTO entries VALUES(%s, '%s', %s, '%s')" % (storyid, content, 1, contributor))
    c.execute("INSERT INTO stories VALUES(%s, '%s')" % (storyid, title))

def newEntry(storyid, content, entrynum, contributor):
    c.execute("INSERT INTO entries VALUES(%s, '%s', %s, '%s')" % (storyid, content, entrynum, contributor))
#=============================================================================================================================================


#===========================================================DISPLAY FUNCTIONS=================================================================

#Shows all entries and stories that a user has contributed to
#To be used in My Acccount/My Stories page
def showEntries(username):
    data = c.execute("SELECT FROM stories WHERE entries.contributor == %s" % (username))

def menuStories(numStories):
    data = c.execute("SELECT ")

#=============================================================================================================================================



