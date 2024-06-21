# Define variables
PYTHON := python3
PYTEST := pytest
PIP := pip3
PROJECT_NAME := Asyncio in Python

.PHONY: install
install:
	$(PIP) install -r requirements.txt
	@echo "Set env vars LT_USERNAME & LT_ACCESS_KEY"
    # Procure Username and AccessKey from https://accounts.lambdatest.com/security
    export LT_USERNAME=himanshuj
    export LT_ACCESS_KEY=Ia1Miq

.PHONY: test
test:
    export NODE_ENV = test

.PHONY: test
fetch-pokemon-names:
	- hyperfine "python tests/fetching-pokemon-names/test_sync_pokeman.py" \
		"python tests/fetching-pokemon-names/test_async_pokeman.py" --warmup=3

# Can't do this since the OpenWeather API account might get blocked
# fetch-weather-info:
# 	- hyperfine "python tests/fetching-weather-information/test_sync_weather_info.py" \
# 		"python tests/fetching-weather-information/test_async_weather_info.py" --warmup=3

fetch-sync-weather-info:
	- python tests/fetching-weather-information/test_sync_weather_info.py

fetch-async-weather-info:
	- python tests/fetching-weather-information/test_async_weather_info.py

get-automation-builds:
	- hyperfine "python tests/get-automation-builds/test_sync_automation_builds.py" \
		"python tests/get-automation-builds/test_async_automation_builds.py" --warmup=3

check-url-health:
	- hyperfine "pytest --verbose --capture=no tests/url-health-checking/test_sync_url_health_check.py" \
		"pytest --verbose --capture=no tests/url-health-checking/test_async_url_health_check.py" --warmup=3

perform-web-scraping:
	- hyperfine "python tests/web-scraping/test_sync_ecommerce_scrapping.py" \
		"python tests/web-scraping/test_async_ecommerce_scrapping.py" --warmup=3

.PHONY: clean
clean:
    # This helped: https://gist.github.com/hbsdev/a17deea814bc10197285
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Clean Succeded"

	find . | grep -E "(.DS_Store)" | xargs rm -rf
	@echo "Clean of DS_Store Succeded"

	find . | grep -E "(.cache)" | xargs rm -rf
	@echo "Pytest Cache clean Succeded"

.PHONY: distclean
distclean: clean
	rm -rf venv

.PHONY: help
help:
	@echo ""
	@echo "install : Install project dependencies"
	@echo "clean : Clean up temp files"
	@echo "fetch-pokemon-names : Fetch Pokemon names [Sync & Async]"
	@echo "fetch-weather-info : Fetch weather information [Sync & Async]"
	@echo "get-automation-builds : Get automation build details [Sync & Async]"
	@echo "check-url-health : Check health of Selenium Playground [Sync & Async]"
	@echo "perform-web-scraping : Web scraping E-Commerce Playground [Sync & Async]"