import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")
pool = None

async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)
    await create_tables()

async def create_tables():
    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE,
            username TEXT,
            first_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
