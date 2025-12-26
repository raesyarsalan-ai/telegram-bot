import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

pool = None


async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)


async def create_tables():
    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE,
            username TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        );
        """)


async def add_user(telegram_id: int, username: str | None):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO users (telegram_id, username)
        VALUES ($1, $2)
        ON CONFLICT (telegram_id) DO NOTHING
        """, telegram_id, username)
