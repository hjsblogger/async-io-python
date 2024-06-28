import sys

sys.path.append(sys.path[0] + "/../../")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *
from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv('LT_USERNAME')
api_key = os.getenv('LT_ACCESS_KEY')

start_time = time.time()

def get_lambdatest_all_builds():
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/builds?limit=50"
    headers = {"accept": "application/json"}

    # SSL context for HTTPS request
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    response = requests.get(url, headers=headers)

    if (response.status_code == 200):
        builds_data = response.json()
        return builds_data
    else:
        print("Failed to fetch builds. Status code:", response.status_code)
        print("Error Message:", response.text)
        return None
    
def get_lambdatest_all_sessions():
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/sessions"
    headers = {"accept": "application/json"}

    # SSL context for HTTPS request
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    response = requests.get(url, headers=headers)

    if (response.status_code == 200):
        builds_data = response.json()
        return builds_data
    else:
        print("Failed to fetch builds. Status code:", response.status_code)
        print("Error Message:", response.text)
        return None

def main():
    print("********* Getting Build Details *********\n")
    builds_data = get_lambdatest_all_builds()
    if builds_data is not None:
        # Extract dashboard URLs from each build object
        dashboard_urls = [build['dashboard_url'] for build in builds_data['data']]

        for dashboard_url in dashboard_urls:
            print("Dashboard URL:", dashboard_url)

    print("\n********* Getting Session Details *********\n")
    sessions_data = get_lambdatest_all_sessions()
    # print(sessions_data)
    if sessions_data is not None:
        # Extract dashboard URLs from each build object
        session_name_urls = [session['build_name'] for session in sessions_data['data']]

        # Print the respective build names
        for session_name_url in session_name_urls:
            print("Session Name:", str(session_name_url))

main()
print("\nTime elapsed is " + str((time.time() - start_time)) + " seconds")