#Beautiful Soup Official Documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Import the locators file
import sys
from pprint import pprint
import ssl
import os
import certifi
sys.path.append(sys.path[0] + "/../../")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPEN_WEATHER_API')

###### Page 1: https://www.latlong.net/category/cities-236-15-1.html ######
start_page = 1
###### Page 13: https://www.latlong.net/category/cities-236-15-13.html ######
last_page = 5

weather_data_arr = []

def scrap_weather_site(url) -> list:
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Unable to fetch the page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')[1:]

    for row in rows:
        # Tried using lambda for fun sake :D
        # https://stackoverflow.com/a/23212106/126105
        # Find all <a> tags that have a title attribute using lambda function
        # a_tags = row.find_all(lambda tag: tag.name == 'a' and tag.has_attr('title'))
        # if a_tags:
        #     title = a_tags[0]['title']
        #     print(title)
        # else:
        #     print("No <a> tags with title found.")

        td_tags = row.find_all('td')
        # The rudimentary approach, but there was a shortcut since all the values
        # were inside <td>
        # for td_tag in td_tags:
        #     a_tag = td_tag.find('a')
        #     if a_tag:
        #         title = a_tag.text.strip()
        #         print(title)

        # Extract values/text from all <td> tags
        td_values = [td.get_text(strip=True) for td in td_tags]
        # print(td_values)
        weather_data_dict = {
            'location': td_values[0],
            'latitude': td_values[1],
            'longitude': td_values[2]
        }
            
        weather_data_arr.append(weather_data_dict)

    return weather_data_arr

def get_weather_info(latitude, longitude):
    # url = f"https://api.openweathermap.org/data/2.5/weather?lat=19.076090&lon=72.877426&appid=ad16be8d5e1200e94e2af3a5f0a321b2"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) \
            + "&appid=" + api_key

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather information:", e)
        return None

# Pagination - 1:13
###### Page 1: https://www.latlong.net/category/cities-236-15-1.html ######
###### Page 13: https://www.latlong.net/category/cities-236-15-13.html ######
if __name__ == '__main__':
    start_time = time.time()
    for iteration in range(start_page, last_page):
        # test_weather_url = "https://www.latlong.net/category/cities-236-15
        test_url = locators.test_weather_url + "-" + str(iteration) + ".html"
        meta_data_arr = scrap_weather_site(test_url)
        # print("*****************************************************\n")
        # helpers.print_scrapped_content(meta_data_arr)
        
    for value in meta_data_arr:
        # Extract latitude and longitude
        # Example - {'location': 'Durango, CO, USA', 'latitude': '37.270500', 'longitude': '-107.878700'}
        latitude = value['latitude']
        longitude = value['longitude']
        weather_info = get_weather_info(latitude, longitude)
        if weather_info:
            temperature = weather_info["main"]["temp"]
            city_name = weather_info["name"]
            print(f"Temperature in " + city_name + " is: " + str(temperature))
    
    print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")