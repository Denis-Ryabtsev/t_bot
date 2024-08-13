import asyncpg
import asyncio
from dotenv import load_dotenv
import os
from PIL import Image
import io


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
    return await asyncpg.connect(**param)

async def close_conn(object):
    await object.close()

# def image_to_bytes(image_path):
#     with Image.open(image_path, 'r') as img:
#         byte_arr = io.BytesIO()
#         img.save(byte_arr, format='PNG')
#         byte_data = byte_arr.getvalue()
#     return byte_data

# async def insert_data():
#     conn = await connection()
#     a = image_to_bytes('2108.jpg')
#     b = image_to_bytes('412.jpg')
#     query = """INSERT INTO foreign_cars(vol, hp, photo, description)
#             VALUES
#             (1.5, 78, $1, 'not bad'),
#             (1.3, 50, $2, 'terrible');"""
#     await conn.execute(query, a, b)
#     await close_conn(conn)

def byte_to_image(data):
    byte_arr = io.BytesIO(data)
    img = Image.open(byte_arr)
    img.save('ex.png')  
##################
# ПОСЛЕ СОЗДАНИЯ ФОТО ИЗ БАЙТОВ, ПОСЛЕ ОТПРАВКИ ПОЛЬЗОВАТЕЛЮ УДАЛИТЬ ИЗ ДИРЕКТОРИИ ФОТО