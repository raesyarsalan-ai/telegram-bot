# db.py
import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")

pool = None

async def connect_db():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(DATABASE_URL)
        await create_tables()

async def create_tables():
    async with pool.acquire() as conn:
        # users table
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE,
            username TEXT,
            first_name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # messages table
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            user_id BIGINT,
            text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

async def save_user(user_id: int, username: str, first_name: str):
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO users (user_id, username, first_name)
            VALUES ($1, $2, $3)
            ON CONFLICT (user_id) DO NOTHING
            """,
            user_id,
            username,
            first_name
        )

async def save_message(user_id: int, text: str):
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO messages (user_id, text)
            VALUES ($1, $2)
            """,
            user_id,
            text
        )
