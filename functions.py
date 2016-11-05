import sqlite3 as sql 
import hashlib

#CONNECT DATABASE
f= "data/stories.db"
db = sql.connect(f)
c = db.cursor()

#Initialize databases. Only works once.
def initializeTables():    
	c.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY autoincrement, username TEXT NOT NULL, password TEXT NOT NULL)")
	c.execute("CREATE TABLE IF NOT EXISTS entries (entryID INTEGER PRIMARY KEY autoincrement, title TEXT NOT NULL, content TEXT NOT NULL)")
	
	
#========================================================GENERIC CREATE FUNCTIONS=============================================================
def newStory(title, storyid, content, contributor, timestamp):
	db = sql.connect(f)
	c = db.cursor()
	c.execute("INSERT INTO entries VALUES(%s, '%s', %s, '%s', %s)" % (storyid, content, 1, contributor, timestamp))
	c.execute("INSERT INTO stories VALUES(%s, '%s')" % (storyid, title))
	db.commit()
	db.close()
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

def returnLatest(numStories):
    data = c.execute("SELECT DISTINCT storyid FROM entries ORDER BY timestamp ASC LIMIT %s" % numStories)
    stories = []
    for item in data:
        stories.append(item[0])

    return stories
        
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

def myStoryListID(username):
    allIDs = []
    allTitles = []
    myStories = returnContributed(username)

    for storyid in myStories:
        allIDs.append(storyid);

        data = c.execute("SELECT * FROM stories WHERE stories.storyid == %s" % (storyid))
        allTitles.append(data.fetchone()[1]) #First (and only) entry fetch. fetch[1] = title

    return (allIDs, allTitles)

def myStoryListDict(username):
    storyDict = {}
    myStories = returnContributed(username)

    for storyid in myStories:
        data = c.execute("SELECT * FROM stories WHERE stories.storyid == %s" % (storyid))
        title = data.fetchone()[1] #First (and only) entry fetch. fetch[1] = title
        storyDict[storyid] = title

    return storyDict
    
    
#Returns the list of stories for the main page
def menuStories(numStories):
    latestStories = returnLatest(numStories)
    latestEntries = []
    latestTitles = []
    
    for story in latest:
        data = c.execute("SELECT * FROM entries WHERE story.id == %s ORDER BY entrynum DES" % story)
        entry = data.fetchone()
        latestEntries.append(entry[1]) #Entry[1] = content

        data = c.execute("SELECT * FROM stories WHERE story.id == %s" % story)
        entry = data.fetchone()
        latestTitles.append(entry[1]) #Entry[1] = title

    return (latestTitles, latestStories,  latestEntries)
        
#=============================================================================================================================================

initializeTables()
db.commit()
db.close()



