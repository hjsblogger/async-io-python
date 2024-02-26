import sys

sys.path.append(sys.path[0] + "/../../")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *
from dotenv import load_dotenv

load_dotenv()

# user_name = os.getenv('LT_USERNAME')
# api_key = os.getenv('LT_ACCESS_KEY')

user_name = "ankurn"
api_key = "6Skayj4MMR4483tOhhdnHsJjLvozmyBI9D2ELd0pABI6m9oZut"

async def get_lambdatest_all_builds(session):
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/builds?limit=2000"
    headers = {"accept": "application/json"}
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            builds_data = await response.json()
            return builds_data
        else:
            print("Failed to fetch builds. Status code:", response.status)
            print("Error Message:", await response.text())
            return None

async def get_lambdatest_all_sessions(session):
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/sessions"
    headers = {"accept": "application/json"}
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            sessions_data = await response.json()
            return sessions_data
        else:
            print("Failed to fetch sessions. Status code:", response.status)
            print("Error Message:", await response.text())
            return None

async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl.create_default_context(cafile=certifi.where()))) as session:
        print("********* Getting Build Details *********\n")
        builds_data = await get_lambdatest_all_builds(session)
        if builds_data:
            dashboard_urls = [build['dashboard_url'] for build in builds_data.get('data', [])]
            for dashboard_url in dashboard_urls:
                print("Dashboard URL:", dashboard_url)

        print("\n********* Getting Session Details *********\n")
        sessions_data = await get_lambdatest_all_sessions(session)
        if sessions_data:
            session_names = [session['build_name'] for session in sessions_data.get('data', [])]
            for session_name in session_names:
                print("Session Name:", session_name)

start_time = time.time()
asyncio.run(main())
print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")