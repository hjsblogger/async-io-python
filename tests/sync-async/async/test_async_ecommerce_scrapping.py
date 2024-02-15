import asyncio
import aiohttp
import sys
import ssl
import certifi
from pprint import pprint
from bs4 import BeautifulSoup

sys.path.append(sys.path[0] + "/../../..")

from pageobject.locators import locators
from pageobject.helpers import helpers

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def scrap_ecommerce(url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl_context=ssl_context)) as session:
        html = await fetch(url, session)
        soup = BeautifulSoup(html, 'html.parser')

        rows = soup.select('.product-layout.product-grid.no-desc.col-xl-4.col-lg-4.col-md-4.col-sm-6.col-6')
        meta_data_arr = []

        for row in rows:
            link = row.find("a", class_='carousel d-block slide')
            name = row.find("h4", class_='title')
            price = row.find("span", class_='price-new')

            meta_data_dict = {
                'product link': link.get('href'),
                'product name': name.get_text(),
                'product price': price.get_text()
            }
            
            meta_data_arr.append(meta_data_dict)

        return meta_data_arr

async def main():
    base_url = locators.test_bs4_url
    tasks = [scrap_ecommerce(f"{base_url}&page={i}") for i in range(1, 6)]
    results = await asyncio.gather(*tasks)

    for i, result in enumerate(results, 1):
        print(f"Product Page = {base_url}&page={i}")
        print("*********************************************************************************************************")
        helpers.print_scrapped_content(result)
        print()

if __name__ == '__main__':
    output = asyncio.run(main())
    print(output)