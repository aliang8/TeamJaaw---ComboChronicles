import sqlite3 as sql
import hashlib

STORIES = 'data/stories.db'
    
def register(username, password):
    hashpass = hashlib.sha224(password).hexdigest()
    creds = (username,hashpass,)
    db = sql.connect(STORIES)
    c = db.cursor()
    users = c.execute("SELECT username FROM accounts WHERE username = ?", (username,))
    if len(c.fetchall()) == 0 and len(password) >= 3:
        c.execute("INSERT INTO accounts (username,password) VALUES (?,?)", creds)
        db.commit()
        db.close()
        return True
    else:
        return False
    
def login(username,password):
    hashpass = hashlib.sha224(password).hexdigest()
    db = sql.connect(STORIES)
    c = db.cursor()
    users = c.execute("SELECT password FROM accounts WHERE username = ?", (username,))
    if c.fetchone()[0] == hashpass: 
        return True
    else:
        return False
    db.commit()
    db.close()

