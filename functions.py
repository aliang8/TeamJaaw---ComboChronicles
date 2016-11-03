import sqlite3 
import csv

USERS = 'data/users.csv'
ENTRIES = 'data/entries.csv'

f= "data/stories.db"
db = sqlite3.connect(f)
c = db.cursor()    
c.execute("CREATE TABLE IF NOT EXISTS users (user TEXT, pass VARCHAR(60))")
c.execute("CREATE TABLE IF NOT EXISTS entries (title TEXT, content TEXT)")

with open('data/users.csv','rb') as u: 
    file = csv.DictReader(u) 
    to_db = [(i['user'], i['pass']) for i in file]

with open('data/entries.csv','rb') as e:
    file = csv.DictReader(e)
    to_db2 = [(i['title'], i['content']) for i in file]

c.executemany("INSERT INTO users (user, pass) VALUES (?, ?);", to_db)
c.executemany("INSERT INTO entries (title, content) VALUES (?, ?);", to_db2)
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





