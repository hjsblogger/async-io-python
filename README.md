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

![LambdaTestEnv-Change](https://github.com/hjsblogger/async-io-python/assets/1688653/ffe23c56-5b53-4d6f-8cfa-85c82d725f99)

![LambdaTestMakefile-Change-2](https://github.com/hjsblogger/async-io-python/assets/1688653/a3105b0c-4515-448b-ace3-77b25a9bf2c1)

**Step 5**

For realizing the *Weather Information* scenario, you need to register on [OpenWeather](https://openweathermap.org/). Once done, set the environment variable *OPEN_WEATHER_API* in .env. The API keys can be located from [OpenWeather API Page](https://home.openweathermap.org/api_keys)

<img width="1424" alt="OpenWeather-API-2" src="https://github.com/hjsblogger/async-io-python/assets/1688653/7d2ebb75-2d72-4dc6-9fb5-bf9cf2a7c96f">

![OpenWeather-API-1](https://github.com/hjsblogger/async-io-python/assets/1688653/e240c220-bb62-491b-a423-f61e34183ec1)

## Dependency/Package Installation

Run the *make install* command on the terminal to install the desired packages (or dependencies) - Pytest, Selenium, Beautiful Soup, etc.

```bash
make install
```
<img width="1295" alt="Makefile-1" src="https://github.com/hjsblogger/async-io-python/assets/1688653/9dd1d433-8994-47ec-b504-fe8c8810979f">

<img width="1412" alt="Makefile-2" src="https://github.com/hjsblogger/async-io-python/assets/1688653/062f66c6-2bbd-44dc-bfad-807c7e006d55">

For benchmarking (over a certain number of runs), we have used [hyperfine](https://github.com/sharkdp/hyperfine), a command-line benchmarking tool. Installation of hyperfine on macOS is done by triggering ```brew install hyperfine``` on the terminal.

<img width="1405" alt="Hyperfine-1" src="https://github.com/hjsblogger/async-io-python/assets/1688653/053b9437-5065-4176-8e91-08e81a2d5b96">

With this, all the dependencies and environment variables are set.

<!--
## Web Scraping using Selenium PyUnit (Local Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on local machine:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *local*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.

<img width="1043" alt="Make-Local" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1ab63873-28e8-4ec0-bebc-ff95d30b224e">

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1baf2aeb-fab1-4207-8547-4c07a70074c2">

**Step 3**

The Chrome browser is invoked in the Headless Mode. It is recommended to install Chrome on your machine before you proceed to Step(3)

**Step 4**

Trigger the *make scrap-using-pyunit* command on the terminal to scrap content from the above mentioned websites

<img width="1404" alt="Pyunit-Scraping-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/3e3ab76f-6c92-4f49-8574-dbe7dc949220">

<img width="1404" alt="Pyunit-Scraping-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/398f147d-bfe9-45af-8fb7-7682592a4470">

As seen above, the content from LambdaTest YouTube channel and LambdaTest e-commerce playground are scrapped successfully!

## Web Scraping using Selenium Pytest (Local Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on local machine:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *local*. Trigger the command ```brew install hyperfine``` on the terminal for installing hyperfine on macOS.

<img width="1405" alt="Hyperfine-1" src="https://github.com/hjsblogger/async-io-python/assets/1688653/053b9437-5065-4176-8e91-08e81a2d5b96">

**Step 2**

The Chrome browser is invoked in the Headless Mode. It is recommended to install Chrome on your machine before you proceed to Step(4)

**Step 3**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/a5d706a8-ccc7-4ef8-aa85-1288b5bef60d">

**Step 4**

Trigger the *make scrap-using-pytest* command on the terminal to scrap content from the above mentioned websites

<img width="1405" alt="Pytest-scraping-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/b6614736-c03a-4e67-9460-32c0443b6166">

<img width="1405" alt="Pytest-scraping-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/dedbbe0c-f18a-4f7d-8ffb-f89c22bea1f3">

## Web Scraping using Beautiful Soup

Beautiful Soup is a Python library that is majorly used for screen-scraping (or web scraping). More information about the library is available on [Beautiful Soup HomePage](https://www.crummy.com/software/BeautifulSoup/)

The Beautiful Soup (bs4) library is already installed as a part of *pre-requisite steps*. Hence, it is safe to proceed with the scraping with Beautiful Soup. [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/) has infinite scrolling pages and Selenium is used to scroll to the end of the page so that all the items on the page can be scraped using the said libraries.

The following websites are used for demonstration:

* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)
* [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/)

Follow the below mentioned steps to perform web scraping using Beautiful Soup(bs4):

**Step 1**

Set *EXEC_PLATFORM* environment variable to *local*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.

<img width="1043" alt="Make-Local" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f8f3fd04-661e-4674-a7e7-48dc8d9cb49f">

**Step 2**

Trigger the *make scrap-using-beautiful-soup* command on the terminal to scrap content from the above mentioned websites

<img width="1402" alt="scraping-bs4-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/82b56e1a-0355-47bc-8527-a14ecf660b33">

<img width="1402" alt="scraping-bs4-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/63253dea-e00d-4636-9955-097952d15d85">

<img width="1402" alt="scraping-bs4-3" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/746724d6-2f1d-47a3-a640-dc40e9338625">

<img width="1413" alt="scraping-bs4-4" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1047b1bb-6495-4d4c-913e-53ea55e9fd78">

<img width="1413" alt="scraping-bs4-5" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/d2a9d796-e1ff-47c5-baa7-323b0ac5649a">

As seen from the above screenshots, content on Pages (1) thru' (5) on [LambdaTest E-Commerce Playground](https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57) are successfully displayed on the console.

<img width="1413" alt="infinite-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/22cbf56e-9420-402f-a16f-df7ea25135e5">

<img width="1097" alt="infinite-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/a691fe82-0f0e-48df-adf1-57d047a904ca">

Also, all the 60 items on [Scraping Club Infinite Scroll Website](https://scrapingclub.com/exercise/list_infinite_scroll/) are scraped without any issues.

## Web Scraping using Selenium Cloud Grid and Python

<b>Note</b>: As mentioned earlier, there could be cases where YouTube Scraping might fail on cloud grid (particularly when there are a number of attempts to scrape the content). Since cookies and other settings are cleared (or sanitized) after every test session, YouTube might take genuine web scraping as a Bot Attack! In such cases, you might across the following page where cookie consent has to be given by clicking on "Accept all" button.

<img width="1407" alt="Accept-All" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/b3a49faa-1ff0-496c-8c8d-661c694455e1">

You can find more information about this insightful [Stack Overflow thread](https://stackoverflow.com/questions/66902404/selenium-python-click-agree-to-youtube-cookie)

Since we are using LambdaTest Selenium Grid for test execution, it is recommended to create an acccount on [LambdaTest](https://www.lambdatest.com/?fp_ref=himanshu15) before proceeding with the test execution. Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security).

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/74028ca3-fe1f-4c25-8cfc-9d563b71900e">

### Web Scraping using Selenium Pyunit (Cloud Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on LambdaTest cloud grid:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *cloud*. Trigger the command *export EXEC_PLATFORM=cloud* on the terminal.

<img width="1396" alt="Terminal" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/f9d81fe0-2eab-466d-8794-aaafc49a5e02">

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/09dd65fc-653a-460f-9ef7-216bd0750d39">

**Step 3**

Trigger the *make scrap-using-pyunit* command on the terminal to scrap content from the above mentioned websites

<img width="1410" alt="Pyunit-cloud-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/dd1129bc-2f74-406c-a54d-6742d0552c66">

<img width="1410" alt="Pyunit-cloud-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/c598f5a3-402b-4117-839f-e78792d711f6">

<img width="1410" alt="Pyunit-cloud-3" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/85ffdf69-6719-47fb-b031-6c2d872a0d59">


As seen above, the content from LambdaTest YouTube channel and LambdaTest e-commerce playground are scrapped successfully! You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1422" alt="Pyunit-LambdaTest-Status-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/5d394264-af49-43d9-a4a0-43f000ec458d">

<img width="1422" alt="Pyunit-LambdaTest-Status-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/98e3cfe2-815f-4f14-a803-0ad3f7399870">

As seen above, the status of test execution is "Completed". Since the browser is instantiated in the *Headless* mode, the video recording is not available on the dashboard.

### Web Scraping using Selenium Pytest (Cloud Execution)

The following websites are used for demonstration:

* [LambdaTest YouTube Channel](https://www.youtube.com/@lambdatest/videos)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to perform scraping on LambdaTest cloud grid:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *cloud*. Trigger the command *export EXEC_PLATFORM=cloud* on the terminal.

<img width="1396" alt="Terminal" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/a89872a1-5a43-4d88-8e9e-1b3e4f170051">

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="710" alt="Make-Clean" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1c228aa5-804c-40a9-9a3b-920e3cd9e489">

**Step 3**

Trigger the *make scrap-using-pytest* command on the terminal to scrap content from the above mentioned websites

<img width="1410" alt="Pytest-cloud-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/4e22c844-0d61-4b4d-85e0-152e11c73689">

<img width="1410" alt="Pytest-cloud-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/0b043360-8f0d-45e7-8f2f-6d96bb65219e">

<img width="1410" alt="Pytest-cloud-3" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/53490f40-f21d-4ecf-90eb-cb38add032da">

As seen above, the content from LambdaTest YouTube channel and LambdaTest e-commerce playground are scrapped successfully! You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1422" alt="Pytest-LambdaTest-Status-1" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/1c090187-2785-4505-916f-34cf07d7565c">

<img width="1429" alt="Pytest-LambdaTest-Status-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/bf0d5757-cc71-4a56-b5ad-e6384018d78e">

As seen above, the status of test execution is "Completed". Since the browser is instantiated in the *Headless* mode, the video recording is not available on the dashboard. -->

## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)
