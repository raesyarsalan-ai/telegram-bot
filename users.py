from db import pool

async def save_user(user):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO users (user_id, username, first_name)
        VALUES ($1, $2, $3)
        ON CONFLICT (user_id) DO NOTHING
        """,
        user.id,
        user.username,
        user.first_name
        )
