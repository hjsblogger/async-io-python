# Asyncio in Python

<img width="1000" height="400" alt="Bulb" src="https://github.com/hjsblogger/async-io-python/assets/1688653/01bb4b8d-9243-4de3-9f02-bf4d19d99ac2">

<div align="center"><a href="https://trunin.com/en/2021/07/python-call-async-from-sync/images/asyncio.jpeg">Image Credit</a></div>
<br/>

In this 'Asyncio with Python' repo, we have covered the following usecases:

* Fetching Pokemon names using [Pokemon APIs](https://pokeapi.co/api/v2/pokemon/)
* Fetching Weather information for certain cities in the US using [Openweather APIs](https://openweathermap.org/api)
* Reading Automation Builds & Session information using [LambdaTest APIs](https://www.lambdatest.com/support/api-doc/)
* Checking URL Health of links present on [LambdaTest Selenium Playground](https://lambdatest.com/selenium-playground)
* Web Scraping of content on [LambdaTest E-Commerce Playground](https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57)

The scenarios mentioned above are executed using Synchronous & Asynchronous (or Async) modes in Python. The Async Programming is realized by leveraging the [asyncio](https://docs.python.org/3/library/asyncio.html) library in Python.  

## Pre-requisites for test execution

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/89beb6af-549f-42ac-a063-e5f715018ef8">

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

Follow steps(3) and (4) for using the LambdaTest Cloud Grid (particularly used for Web Scraping & URL Health Checking Scenarios):

**Step 3**

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests (or scraping) on the cloud Grid.

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/9b40c9cb-93a1-4239-9fe5-99f33766a23a">

**Step 4**

Add the LambdaTest User Name and Access Key in the *.env* (or *Makefile*)that is located in the parent directory. Once done, save the Makefile.

<img width="600" height="300" alt="LambdaTestEnv-Change" src="https://github.com/hjsblogger/async-io-python/assets/1688653/ffe23c56-5b53-4d6f-8cfa-85c82d725f99">

<img width="600" height="300" alt="LambdaTestAccount" src="https://github.com/hjsblogger/async-io-python/assets/1688653/a3105b0c-4515-448b-ace3-77b25a9bf2c1">

**Step 5**

For realizing the *Weather Information* scenario, you need to register on [OpenWeather](https://openweathermap.org/). Once done, set the environment variable *OPEN_WEATHER_API* in .env. The API keys can be located from [OpenWeather API Page](https://home.openweathermap.org/api_keys)

<img width="1000" alt="OpenWeather-API-2" src="https://github.com/hjsblogger/async-io-python/assets/1688653/7d2ebb75-2d72-4dc6-9fb5-bf9cf2a7c96f">

<img width="600" height="300" alt="OpenWeather-API-1" src="https://github.com/hjsblogger/async-io-python/assets/1688653/e240c220-bb62-491b-a423-f61e34183ec1">

## Dependency/Package Installation

Run the *make install* command on the terminal to install the desired packages (or dependencies) - Pytest, Selenium, Beautiful Soup, etc.

```bash
make install
```
<img width="1295" alt="Makefile-1" src="https://github.com/hjsblogger/async-io-python/assets/1688653/9dd1d433-8994-47ec-b504-fe8c8810979f">

<img width="1412" alt="Makefile-2" src="https://github.com/hjsblogger/async-io-python/assets/1688653/062f66c6-2bbd-44dc-bfad-807c7e006d55">

For benchmarking (over a certain number of runs), we have used [hyperfine](https://github.com/sharkdp/hyperfine), a command-line benchmarking tool. Installation of hyperfine on macOS is done by triggering ```brew install hyperfine``` on the terminal.

<img width="1405" alt="Hyperfine-1" src="https://github.com/hjsblogger/async-io-python/assets/1688653/053b9437-5065-4176-8e91-08e81a2d5b96">

With this, all the dependencies and environment variables are set. It's time for some action !!

## Execution

Follow the below mentioned steps to benchmark the performance of sync and async code (via the hyperfine tool):

**Step 1**

For the URL health checking scenario, the Chrome browser is invoked in the non-headless mode. It is recommended to install Chrome on your machine before you proceed to Step(4)

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files. It also cleans .DS_Store folder from the project.

<img width="506" alt="MakeClean" src="https://github.com/hjsblogger/async-io-python/assets/1688653/5b1bbb77-1a79-4586-940f-c07f9a0cbb69">

**Step 3**

Trigger the *make* command on the terminal to realize the usecases in the sync & async mode.

### Fetching Pokemon names using Pokemon APIs

Trigger the command *make fetch-pokemon-names* to fetch the Pokemon names using [Pokemon APIs](https://pokeapi.co/api/v2/pokemon/) and running code in sync & async mode (using Asyncio in Python).

<img width="1106" alt="1_Pokemon_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/98c543cc-1474-4c4d-a7ba-88079730d168">

### <b>Result: Asyncio - 5.77+ seconds faster than sync execution</b>

### Fetching Weather information for certain cities in the US using Openweather APIs

In this scenario, the city names from [Page-1](https://www.latlong.net/category/cities-236-15-1.html) thru' [Page-15](https://www.latlong.net/category/cities-236-15-13.html) are first scraped using BeautifulSoup.

<img width="1422" alt="WeatherScenario" src="https://github.com/hjsblogger/async-io-python/assets/1688653/683963c7-7dbf-4b07-b20f-c3dabb3427cf">

Now that we have the city names, let's fetch the weather of those cities by providing Latitude & Longitude to the [OpenWeather API](https://api.openweathermap.org/data/2.5/weather?lat=<LATITUDE>&lon=<LONGITUDE>&appid=<OPEN_WEATHER_API>)

Trigger the command *make fetch-sync-weather-info* to fetch the Pokemon names using [Pokemon APIs](https://pokeapi.co/api/v2/pokemon/) and running code in sync mode.

<img width="1099" alt="2 1_Weather_Info_Sync_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/7f6f1545-8d45-4837-98f4-cdd5b1670250">

<img width="1099" alt="2 2_Weather_Info_Sync_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/99275e78-9fc7-4619-b7c5-25fea0911da1">

<img width="1099" alt="2 3_Weather_Info_Sync_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/9603f535-45fe-4a2f-8f6f-e02f6a32c0ea">

Trigger the command *make fetch-async-weather-info* to fetch the Pokemon names using [Pokemon APIs](https://pokeapi.co/api/v2/pokemon/) and running code in sync & async mode (using Asyncio in Python).

<img width="1097" alt="2 4_Weather_Info_ASync_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/a78b8bd6-dd40-4bc3-a4c4-0a19014201ed">

<img width="1097" alt="2 5_Weather_Info_ASync_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/5a765c29-839c-4551-ac8b-26ec90b64ce1">

<img width="1097" alt="2 6_Weather_Info_ASync_Execution" src="https://github.com/hjsblogger/async-io-python/assets/1688653/b2dbfdac-78c7-4af7-ae41-53e046876640">

### <b>Result: Asyncio - 318.53+ seconds faster than sync execution</b>


## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)