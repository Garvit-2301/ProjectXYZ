import sqlite3

DB_NAME = "data/LifeBot.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS conversations (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   question TEXT,
                   response TEXT
                   )
                   """)
    
    conn.commit()

    conn.close()