# db.py
import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")

pool = None

async def connect_db():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(DATABASE_URL)

async def save_message(
    user_id: int,
    username: str,
    text: str
):
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO messages (user_id, username, text)
            VALUES ($1, $2, $3)
            """,
            user_id,
            username,
            text
        )
