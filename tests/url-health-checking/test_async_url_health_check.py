import sys
from pageobject.locators import locators
from pageobject.locators import *
from pageobject.helpers import helpers
from pageobject.helpers import *

sys.path.append(sys.path[0] + "/../../")

async def check_status(session, url):
    async with session.get(url) as response:
        status_code = response.status
        print(url + " status = " + str(status_code) + " ")
        return status_code

class TestAsyncHealthCheckOps:
    @pytest.mark.asyncio
    @pytest.mark.run(order=1)
    async def test_async_url_access(self, driver) -> list:
        start_time = time.time()
        meta_data_arr = []
        driver.get(locators.test_playground_url)

        driver.maximize_window()

        meta_data_arr = helpers.scrap_playground_url(driver)

        async with aiohttp.ClientSession() as session:
            tasks = [check_status(session, url) for url in meta_data_arr]
            status_codes = await asyncio.gather(*tasks)

        for status_code, url in zip(status_codes, meta_data_arr):
            assert status_code == 200, f"Failed for URL: {url}, Status Code: {status_code}"

        print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")