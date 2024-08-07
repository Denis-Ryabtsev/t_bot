import aiohttp
from dotenv import load_dotenv
import os


load_dotenv()
API = os.getenv('API_WEATHER')

async def get_weather(lat, lon):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API,
        "units": "metric",
        "lang": "ru"
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(base_url, params=params)
    temp = await response.json()
    data = str(f"City: {temp['name']}\
               \nWeather: {temp['weather'][0]['description']}\
               \nTemp min: {temp['main']['temp_min']}\
               \nTemp max: {temp['main']['temp_max']}\
               \nFeels like: {temp['main']['feels_like']}\
               \nSpeed wind: {temp['wind']['speed']}")
    return data