import asyncpg
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
USER = os.getenv('DB_USER')
PSWD = os.getenv('DB_PSWD')
HOST = os.getenv('DB_HOST')
NAME = os.getenv('DB_NAME')

async def connection():
    param = {
        "host": HOST,
        "database": NAME,
        "user": USER,
        "password": PSWD
    }
    
    conn = await asyncpg.connect(**param)
    await conn.close()

asyncio.run(connection())