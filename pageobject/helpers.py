# Import the locators file
import sys
import time
import requests
import pytest
import asyncio
import httpx
import asyncio
import aiohttp
import ssl
import os
from selenium import webdriver
import certifi

from bs4 import BeautifulSoup
from pprint import pprint

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.locators import locators
from pageobject.locators import *

from array import array

# def create_actions(driver):
#     actions = ActionChains(driver)
#     return actions

# def create_waits(driver, duration):
#     # Explicit wait of 10 seconds
#     wait = WebDriverWait(driver, duration)
#     return wait

class helpers(object):
    # def scrap_playground_url(driver)->list:
    def scrap_playground_url(driver)->array:    
        meta_data_arr=[]
        # Explicit wait of 10 seconds
        # wait = create_waits(driver, 10)

        # actions = create_actions(driver)

        # element_cat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
        #         locators.loc_title)))
        
        # Now the page is loaded, let's fetch the links from the page
        loc_parent_elem = driver.find_element(By.XPATH,
                "//*[@id='__next']/div/section[2]/div/ul")
        
        loc_list_elems = loc_parent_elem.find_elements(By.CLASS_NAME,
                            "pt-10")
        
        # Get the length of the list of elements
        num_elements = len(loc_list_elems)

        # Output the number of elements located
        print("Number of elements located:", num_elements)

        for loc_link_info in loc_list_elems:
            link_info = loc_link_info.find_element(By.CSS_SELECTOR,
                ".text-black.text-size-14.hover\:text-lambda-900.leading-relaxed")

            final_link = link_info.get_attribute('href')

            meta_data_arr.append(final_link)

        return meta_data_arr

    def print_scrapped_content(meta_data):
        for elem_info in meta_data:
            print(elem_info)