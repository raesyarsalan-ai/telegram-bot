import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        is_premium INTEGER DEFAULT 0,
        messages_today INTEGER DEFAULT 0
    )
    """)
    conn.commit()
