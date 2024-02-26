# Example Inspiration - https://www.twilio.com/en-us/blog/
# asynchronous-http-requests-in-python-with-aiohttp#Utilizing-asyncio-for-improved-performance

import sys

sys.path.append(sys.path[0] + "/../../")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *
from dotenv import load_dotenv

load_dotenv()

start_page = 1
last_page = 151

start_time = time.time()

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['game_indices']


async def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = []
        for number in range(start_page, last_page):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        # print(original_pokemon)

        # Iterate over the nested list and print the 'name' entry
        for sublist in original_pokemon:
            for item in sublist:
                print("Name:", item['version']['name'])

asyncio.run(main())
print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")