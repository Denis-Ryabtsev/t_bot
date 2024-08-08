import aiohttp
from dotenv import load_dotenv
import os


load_dotenv()
API = os.getenv('API_GIF')

async def get_gif(keyword):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": API,
        "q": keyword,
        "limit": 1,  # Количество GIF, которые нужно вернуть
        "offset": 0,
        "rating": "R",  # Рейтинг GIF (например, G, PG, PG-13, R)
        "lang": "en"  # Язык
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
    gif_url = data["data"][0]["images"]["original"]["url"]
    return gif_url