import sqlite3 as sql
import hashlib

STORIES = 'data/stories.db'
    
def register(username, password):
    db = sql.connect(STORIES)
    c = db.cursor()
    users = c.execute("SELECT username FROM accounts WHERE username = ?", (username, )).fetchone()
    print users
    hashpass = hashlib.sha224(password).hexdigest()
    if not users:
        c.execute("INSERT INTO accounts (username,password) VALUES (%s,%s)" % (username,password))
        return True
    else:
        return False
    db.commmit()
    db.close()

def login(username,password):
    db = sql.connect(STORIES)
    c = db.cursor()
    hashpass = hashlib.sha224(password).hexdigest()
    users = c.execute("SELECT password FROM accounts WHERE username == %s" % (username))
    if users and users[2] == hashpass:
        return True
    else: 
        return False
    db.commit()
    db.close()

