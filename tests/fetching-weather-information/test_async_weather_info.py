
import sys

sys.path.append(sys.path[0] + "/../../")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPEN_WEATHER_API')

start_page = 1
last_page = 5
weather_data_arr = []

async def fetch_data(url, session):
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Unable to fetch the page. Status code: {response.status}")
            return None
        else:
            return await response.text()

async def scrap_weather_site(url, session):
    html_content = await fetch_data(url, session)
    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        rows = soup.find_all('tr')[1:]

        for row in rows:
            td_tags = row.find_all('td')
            td_values = [td.get_text(strip=True) for td in td_tags]
            weather_data_dict = {
                'location': td_values[0],
                'latitude': td_values[1],
                'longitude': td_values[2]
            }
            weather_data_arr.append(weather_data_dict)

async def get_weather_info(session, latitude, longitude):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error fetching weather information for latitude {latitude} and longitude {longitude}.")
            return None
        else:
            weather_info = await response.json()
            return weather_info

async def main():
    # Encountered the below error
    # aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to 
    # host ecommerce-playground.lambdatest.io:443 ssl:True 
    # [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: 
    # unable to get local issuer certificate (_ssl.c:1000)')]

    # Solution: https://stackoverflow.com/a/66842057/126105
    # async with aiohttp.ClientSession() as session:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = []
        for iteration in range(start_page, last_page):
            test_url = locators.test_weather_url + "-" + str(iteration) + ".html"
            tasks.append(scrap_weather_site(test_url, session))
        await asyncio.gather(*tasks)

        tasks = []
        for value in weather_data_arr:
            latitude = value['latitude']
            longitude = value['longitude']
            tasks.append(get_weather_info(session, latitude, longitude))
        weather_infos = await asyncio.gather(*tasks)

        for weather_info in weather_infos:
            if weather_info:
                temperature = weather_info["main"]["temp"]
                city_name = weather_info["name"]
                print(f"Temperature in {city_name} is: {temperature}")

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")