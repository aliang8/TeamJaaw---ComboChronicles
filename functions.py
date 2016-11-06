import sqlite3 as sql 
import hashlib

#CONNECT DATABASE
STORIES = "data/stories.db"

#Initialize databases. Only works once.
def initializeTables():    
	db = sql.connect(STORIES)
	c = db.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS accounts (username TEXT NOT NULL, password TEXT NOT NULL)")
	c.execute("CREATE TABLE IF NOT EXISTS entries (storyid INTEGER, content TEXT NOT NULL, entryID INTEGER PRIMARY KEY autoincrement, contributor TEXT NOT NULL, timestamp TEXT NOT NULL)")
	c.execute("CREATE TABLE IF NOT EXISTS stories (storyid INTEGER PRIMARY KEY, title TEXT NOT NULL)")
	db.commit()
	db.close()

#========================================================GENERIC CREATE FUNCTIONS=============================================================
def newStory(title, content, contributor, timestamp):
	db = sql.connect(STORIES)
	c = db.cursor()
	c.execute("INSERT INTO stories (title) VALUES (?)", (title,))
	c.execute("INSERT INTO entries (storyid, content, contributor, timestamp) VALUES(?, ?, ?, ?)" , (c.lastrowid, content.strip(), contributor, timestamp,))
	db.commit()

def newEntry(storyid, content, contributor, timestamp):
	c.execute("INSERT INTO entries VALUES(?, ?, ?, ?, ?)" , (storyid, content, NULL, contributor, timestamp,))
	db.commit()

#=============================================================================================================================================


#===========================================================OUTPUT FUNCTIONS=================================================================


#Returns a list of all posts a user has contributed to
def returnContributed(username):
	db = sql.connect(STORIES)
	c = db.cursor()
	data = c.execute("SELECT DISTINCT storyid FROM entries WHERE entries.contributor == ? ORDER BY timestamp ASC" , (username,))
	stories = []
	for item in data:
		stories.append(item[0])	#Item[0] = storyid
	return stories

#Returns one entire story as a list
def returnStory(storyid):
	db = sql.connect(STORIES)
	c = db.cursor()
	data = c.execute("SELECT * FROM entries WHERE entries.storyid == ? ORDER BY entryID ASC" , (storyid,))
	story = []
	for item in data:
		story.append(item[1]) # Item 1 = Story content of one entry
	return story

#Returns a list of all contributors to a story in order
def returnContributors(storyid):
	db = sql.connect(STORIES)
	c = db.cursor()
	data = c.execute("SELECT * FROM entries WHERE entries.storyid == ? ORDER BY entryID ASC" , (storyid,))
	contributors = []
	for item in data:
		contributors.append(item[3]) #Item[3] = contributor
	return contributors

def returnLatest(numStories):
	db = sql.connect(STORIES)
	c = db.cursor()
	data = c.execute("SELECT DISTINCT storyid FROM entries ORDER BY timestamp ASC LIMIT ?" , (numStories,))
	stories = []
	for item in data:
		stories.append(item[0])
	return stories

#Returns list of all completed story ids ordered
def returnFinished(sortOrder):
	db = sql.connect(STORIES)
	c1 = db.cursor()
	c2 = db.cursor()
	stories = c1.execute("SELECT DISTINCT storyid FROM entries ORDER BY ? ASC" , (sortOrder,))
	storyList = []
	for story in stories:
		l = list(c2.execute("SELECT * FROM entries WHERE entries.storyid == ?" , story))
		if len(l) == 10:
			storyList.append(story[0])			
	return storyList
        
#==============================================================================================================================================



#=============================================================FOR DISPLAY FUNCTIONS============================================================

#Returns a tuple (All titles of stories user contributed to, 
#                 all stories contents of the contributed to stories,
#                 all contributors of the respective stories)
#
# Tuple represented in components : ([], [][], [][])
# For my account/my stories page
def myStoryList(username):
	db = sql.connect(STORIES)
	c = db.cursor()
	myStories = returnContributed(username)
	allStories = []
	allContributors = []
	allTitles = []
	
	for storyid in myStories:
		allStories.append(returnStory(storyid))
		allContributors.append(returnContributors(storyid))
		
		data = c.execute("SELECT * FROM stories WHERE stories.storyid == ?" , (storyid,))
		entry = data.fetchone()
		if entry:
			allTitles.append(entry[1]) #First (and only) entry fetch. fetch[1] = title
			
	return (allTitles, allStories, allContributors,)

def myStoryListID(username):
	db = sql.connect(STORIES)
	c = db.cursor()
	allIDs = []
	allTitles = []
	myStories = returnContributed(username)

	for storyid in myStories:
		allIDs.append(storyid);
		data = c.execute("SELECT * FROM stories WHERE stories.storyid == ?" , (storyid,))
		allTitles.append(data.fetchone()[1]) #First (and only) entry fetch. fetch[1] = title

	return (allIDs, allTitles,)

def myStoryListDict(username):
	db = sql.connect(STORIES)
	c = db.cursor()
	storyDict = {}
	myStories = returnContributed(username)
	for storyid in myStories:
		data = c.execute("SELECT * FROM stories WHERE stories.storyid == ?" , (storyid,))
		title = data.fetchone()
		if title:
			title = title[1] #First (and only) entry fetch. fetch[1] = title
		storyDict[storyid] = title
	return storyDict
    
    
#Returns the list of stories for the main page
def menuStories(numStories):
	db = sql.connect(STORIES)
	c = db.cursor()
	latestStories = returnLatest(numStories)
	latestEntries = []
	latestTitles = []
	for story in latestStories:
		data = c.execute("SELECT * FROM entries WHERE entries.storyid == ? ORDER BY entrynum DES" , (story,))
		entry = data.fetchone()
		if entry:
			latestEntries.append(entry[1]) #Entry[1] = content
		data = c.execute("SELECT * FROM stories WHERE stories.storyid == ?" , (story,))
		entry = data.fetchone()
		if entry:
			latestTitles.append(entry[1]) #Entry[1] = title
	return (latestTitles, latestStories, latestEntries,)


#Returns the list for all stories that were finished. To be used for the library
def libraryStories():
	db = sql.connect(STORIES)
	c = db.cursor()
	allStories = returnFinished('storyid')
	allEntries = []
	allTitles = []
	for story in allStories:
        	data = c.execute("SELECT * FROM entries WHERE story.id == ? ORDER BY entrynum DES" , (story,))
        	entry = data.fetchone()
        	if entry:
			latestEntries.append(entry[1]) #Entry[1] = content
        	data = c.execute("SELECT * FROM stories WHERE story.id == ?" , (story,))
        	entry = data.fetchone()
        	if entry:
			latestTitles.append(entry[1]) #Entry[1] = title
	return (allTitles, allStories, allEntries,)
	
def libraryStoriesDict():	
	db = sql.connect(STORIES)
	c = db.cursor()
	allStories = returnFinished('storyid')
	storyDict = {}
	for story in allStories:
		title = c.execute("SELECT * FROM stories WHERE story.id == ? ORDER BY storyid ASC", (story,))
		title = title.fetchone()
		storyDict[story] = title[1]
	return storyDict

#=============================================================================================================================================



print returnLatest(3)
print returnContributors(2)
print returnContributed('anthony')
print returnContributed('jerry')
print returnStory(3)
print returnFinished('storyid')
