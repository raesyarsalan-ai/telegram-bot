from db import cur, conn

def add_user(user_id):
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()

def is_premium(user_id):
    cur.execute("SELECT is_premium FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    return row and row[0] == 1

def can_use(user_id):
    cur.execute("SELECT messages_today FROM users WHERE user_id=?", (user_id,))
    count = cur.fetchone()[0]
    return count < 5

def inc_usage(user_id):
    cur.execute(
        "UPDATE users SET messages_today = messages_today + 1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()

def activate_premium(user_id):
    cur.execute(
        "UPDATE users SET is_premium = 1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()
