import sqlite3

DB = "topics.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS topics (name TEXT UNIQUE)")
    conn.commit()
    conn.close()

def add_topic(topic):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO topics VALUES (?)", (topic,))
    conn.commit()
    conn.close()

def remove_topic(topic):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM topics WHERE name=?", (topic,))
    conn.commit()
    conn.close()

def get_topics():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT name FROM topics")
    topics = [r[0] for r in c.fetchall()]
    conn.close()
    return topics
