import sqlite3 

USERS = 'data/users.csv'
ENTRIES = 'data/entries.csv'

def initializeDatabase():
    f= "data/stories.db"
    db = sqlite3.connect(f)
    c = db.cursor()    
    q = "CREATE TABLE users (user TEXT, pass VARCHAR(60))"
    c.execute(q)    
    q = "CREATE TABLE entries (title TEXT, content TEXT)"
    c.execute(q)
    db.commit() 
    db.close()  

def newAccount(username, password):
    d = open(USERS,'a')
    user = "%s,%s\n" %(username,password) 
    d.write(user)
    d.close()

def newEntry(title, content):
    d = open(ENTRIES,'a')
    entry = "%s,%s\n" %(title, content)
    d.write(entry)
    d.close()

initializeDatabase()



