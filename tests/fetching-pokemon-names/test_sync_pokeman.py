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

def get_pokemon(url):
    response = requests.get(url)
    pokemon = response.json()
    return pokemon['game_indices']

def test_getname():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with requests.Session() as session:
        original_pokemon = []
        for number in range(start_page, last_page):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            original_pokemon.append(get_pokemon(url))
        
        # print(original_pokemon)

        # Iterate over the nested list and print the 'name' entry
        for sublist in original_pokemon:
            for item in sublist:
                print("Name:", item['version']['name'])

test_getname()

print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")
