import os
import ssl
import certifi
import aiohttp
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv('LT_USERNAME')
api_key = os.getenv('LT_ACCESS_KEY')


app = FastAPI()

async def get_lambdatest_all_builds(session):
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/builds?limit=50"
    headers = {"accept": "application/json"}
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            builds_data = await response.json()
            print(builds_data)
            return builds_data
        else:
            raise HTTPException(status_code=response.status, detail=await response.text())

async def get_lambdatest_all_sessions(session):
    url = f"https://{user_name}:{api_key}@api.lambdatest.com/automation/api/v1/sessions"
    headers = {"accept": "application/json"}
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            sessions_data = await response.json()
            print(sessions_data)
            return sessions_data
        else:
            raise HTTPException(status_code=response.status, detail=await response.text())

@app.get("/builds/")
async def fetch_builds():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl.create_default_context(cafile=certifi.where()))) as session:
        builds_data = await get_lambdatest_all_builds(session)
        dashboard_urls = [build['dashboard_url'] for build in builds_data.get('data', [])]
        return {"dashboard_urls": dashboard_urls}

@app.get("/sessions/")
async def fetch_sessions():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl.create_default_context(cafile=certifi.where()))) as session:
        sessions_data = await get_lambdatest_all_sessions(session)
        session_names = [session['build_name'] for session in sessions_data.get('data', [])]
        return {"session_names": session_names}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
