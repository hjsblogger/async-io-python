import pytest
import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from selenium import webdriver
import os
import logging
from os import environ
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from unittest.mock import patch

sys.path.append(sys.path[0] + "/../..")

exec_async = os.getenv('EXEC_ASYNC')

if exec_async == 'true':
    # logs via pytest-xdist
    # https://github.com/pytest-dev/pytest-xdist/issues/354#issuecomment-430502446
    # sys.stdout = sys.stderr

    options = ChromeOptions()

    # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
    # to trigger browser in headless mode
    options.add_argument("--headless=new")

    @pytest.fixture(scope='function')
    async def driver():
        driver = await asyncio.to_thread(webdriver.Chrome, options=options)
        yield driver
        await asyncio.to_thread(driver.quit)
else:
    @pytest.fixture(scope='function')
    def driver():
        driver = webdriver.Chrome(options=options)
        yield driver
        def fin():
            driver.quit()

# logs via pytest-xdist
# https://github.com/pytest-dev/pytest-xdist/issues/354#issuecomment-1274564868
@pytest.fixture(scope="session", autouse=True)
def fix_print():
    """
    pytest-xdist disables stdout capturing by default, which means that print() statements
    are not captured and displayed in the terminal.
    That's because xdist cannot support -s for technical reasons wrt the process execution mechanism
    https://github.com/pytest-dev/pytest-xdist/issues/354
    """
    original_print = print
    with patch("builtins.print") as mock_print:
        mock_print.side_effect = lambda *args, **kwargs: original_print(*args, **{"file": sys.stderr, **kwargs})
        yield mock_print