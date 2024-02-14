import time
import requests
import asyncio
from aiohttp import ClientSession



cities = ['Delhi', 'Minsk', 'Moscow']

def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '4cfca7c0d39c20a00a4dea84301d4188'}
    res = requests.get(url, params)
    j = res.json()
    print(f"{city} - {j['weather'][0]['main']}")


async def a_get_weather(city):
    async with ClientSession() as session:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '4cfca7c0d39c20a00a4dea84301d4188'}
        async with session.get(url = url, params = params) as respons:
            j = await respons.json()
            print(f"{city} - {j['weather'][0]['main']}")


async def a_main(cities):
    tasks = []
    for city in cities:
        tasks.append(asyncio.create_task(a_get_weather(city)))

    for task in tasks:
        q = await task




t = time.time()
#for city in cities*5:
    #get_weather(city)
#    asyncio.run(a_get_weather(city))
asyncio.run(a_main(cities*5))
print(time.time() - t)