from selenium import webdriver
from os import environ
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Not a recommended practice - need to be replaced with Explicit Waits
import time
import pytest

# Imports for Beautiful Soup
import requests
from bs4 import BeautifulSoup

class locators(object):
    ########## Locators for e-commerce playground ##########

    test_ecomm_url = "https://ecommerce-playground.lambdatest.io/"
    shopcategory = "//a[contains(.,'Shop by Category')]"
    phonecategory = "//span[contains(.,'Phone, Tablets & Ipod')]"

    ########## Locators for YouTube ##########

    # test_yt_url = "https://www.youtube.com/@hjsblogger/videos"
    test_playground_url = "https://lambdatest.com/selenium-playground"

    # loc_upgrade = ".py-14"
    loc_title = ".text-size-50"

    ########## Definitions for scraping using Beautiful Soup ###########

    test_bs4_url = "https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57"

    ########## Scraping Weather website ###########
    ###### Format (Page 1): https://www.latlong.net/category/cities-236-15.html ######
    ###### Format (Page 1): https://www.latlong.net/category/cities-236-15-1.html ######
    ###### Format (Page 13): https://www.latlong.net/category/cities-236-15-13.html ######

    test_weather_url = "https://www.latlong.net/category/cities-236-15"

    ########## Definitions for scraping using Beautiful Soup ###########

    test_bs4_infinite_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"