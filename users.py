users = {}

def save_user(user_id: int, username: str | None):
    if user_id not in users:
        users[user_id] = {
            "username": username,
            "messages": 0
        }

def increase_message_count(user_id: int):
    if user_id in users:
        users[user_id]["messages"] += 1

def get_message_count(user_id: int) -> int:
    return users.get(user_id, {}).get("messages", 0)
