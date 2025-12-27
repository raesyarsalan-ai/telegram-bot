from datetime import datetime
from db import cursor, conn

def add_user(user):
    cursor.execute("""
    INSERT OR IGNORE INTO users (user_id, username, first_name, joined_at)
    VALUES (?, ?, ?, ?)
    """, (
        user.id,
        user.username,
        user.first_name,
        datetime.utcnow().isoformat()
    ))
    conn.commit()

def save_message(user_id, text):
    cursor.execute("""
    INSERT INTO messages (user_id, text, created_at)
    VALUES (?, ?, ?)
    """, (
        user_id,
        text,
        datetime.utcnow().isoformat()
    ))
    conn.commit()

def get_stats():
    users = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    messages = cursor.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    return users, messages
