import sqlite3 as sql

STORIES = 'data/stories.db'

def newEntry(title,content):
    params = (title,content,)
    db = sql.connect(STORIES)
    db.execute("INSERT INTO entries (title,content) VALUES (?,?)", params)
    db.commit()
    db.close()
