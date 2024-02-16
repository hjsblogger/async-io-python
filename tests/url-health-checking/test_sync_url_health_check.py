# Import the locators file
import sys
sys.path.append(sys.path[0] + "/../../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

class TestSyncOps:
    @pytest.mark.run(order=1)
    def test_sync_url_access(self, driver) -> list:
        meta_data_arr=[]
        driver.get(locators.test_playground_url)

        driver.maximize_window()

        meta_data_arr = helpers.scrap_playground_url(driver)

        for url in meta_data_arr:
            status_code = requests.get(url).status_code
            print(url + " status = " + str(status_code) + " ")
            assert status_code == 200, f"Failed for URL: {url}, Status Code: {status_code}"