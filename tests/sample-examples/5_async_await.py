# Demonstration of asyncio with Python (Pytest is the automation framework)

# Includes the following:

# Usage of aiohttp
# Usage of asyncio.gather
# Marking tests as async using the @pytest.mark.asyncio marker

import pytest
import aiohttp
import asyncio
import json
import ssl
import os
import sys
from dotenv import load_dotenv
import certifi

load_dotenv()

user_name = os.getenv('LT_USERNAME')
api_key = os.getenv('LT_ACCESS_KEY')

# Inspiration - https://stackoverflow.com/questions/53199248/get-json-using-python-and-asyncio
async def get_top_reddit_threads(subreddit, session):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=20"

    # Reference JSON - https://www.reddit.com/r/Playwright/top.json?sort=top&t=day&limit=20
    data = await get_json(session, url)

    if data:
        data_decoded = json.loads(data.decode('utf-8'))
        print(f'\nReddit details for {subreddit}')
        print(f'____________________________\n')
        for post in data_decoded['data']['children']:
            score = post['data']['score']
            title = post['data']['title']
            link = post['data']['url']
            if score and title and link:
                print(f'Score: {score}  |  Title: {title}  |  Link: ({link})')

# Fetch JSON data from a URL

async def get_json(session, url):
    headers = {"accept": "application/json"}
    try:
        async with session.get(url, headers=headers) as response:
            # Response 200 - We have the data!
            assert response.status == 200
            return await response.read()
    except aiohttp.client_exceptions.ClientConnectorCertificateError as e:
        print(f"SSL Certificate Error: {e}")
        return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Refer LambdaTest API documentation - https://www.lambdatest.com/support/api-doc/

async def get_lambdatest_sessions(session):
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/sessions?limit=40"
    data = await get_json(session, url)

    if data:
        data_decoded = json.loads(data.decode('utf-8'))
        for test in data_decoded['data']:
            test_id = test['test_id']
            build_name = test['build_name']
            status_ind = test['status_ind']
            print(f"Build: {build_name}  |  ID: {test_id}  |  Status: {status_ind}")          

@pytest.mark.asyncio
async def test_fetch_lambdatest_platforms():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        await get_lambdatest_sessions(session)

@pytest.mark.asyncio
async def test_fetch_reddit_threads():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        subreddits = ['Selenium', 'Playwright', 'Python', 'asyncio']
        tasks = [get_top_reddit_threads(subreddit, session) for subreddit in subreddits]
        # Gather the tasks using gather() method of asyncio
        await asyncio.gather(*tasks)