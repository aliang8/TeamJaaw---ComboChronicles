import sqlite3 
import csv    

def initializeDatabase():
    f= "data/stories.db"
    db = sqlite3.connect(f)
    c = db.cursor()    
    q = "CREATE TABLE accounts (user TEXT, pass VARCHAR(60), myStories BLOB, settings BLOB)"
    c.execute(q)    
    q = "CREATE TABLE stories (title TEXT, id INTEGER PRIMARY KEY, content BLOB, timestamp TEXT, contributors BLOB)"
    c.execute(q)
    db.commit() 
    db.close()  

def newEntry(title, entry, username):
    q = "INSERT TABLE stories %s, %i, %s, %s, %s" %(title, id, entry, date('now'), username)
    c.execute(q)

initializeDatabase()


