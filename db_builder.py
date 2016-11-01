import sqlite3 
import csv    

#========================================================
f="data/stories.db"
db = sqlite3.connect(f)
c = db.cursor()    

f1 = open("data/accounts.csv")
d1 = csv.DictReader(f1)

q = "CREATE TABLE accounts (user TEXT, pass VARCHAR(60), myStories BLOB, settings BLOB)"

c.execute(q)    

f2 = open("data/stories.csv")
d2 = csv.DictReader(f2)

q = "CREATE TABLE courses (title TEXT, id INTEGER PRIMARY KEY, entryCount INTEGER, content BLOB, timestamp TEXT, contributors BLOB, currentEdit BOOLEAN)"

c.execute(q)
#==========================================================
db.commit() #save changes
db.close()  #close database


