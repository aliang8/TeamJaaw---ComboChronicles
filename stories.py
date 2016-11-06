import sqlite3 as sql

STORIES = 'data/stories.db'

def newStory(title,content):
    params = (title,content,)
    db = sql.connect(STORIES)
    db.execute("INSERT INTO stories (title,content) VALUES (?,?)", params)
    db.commit()
    db.close()
