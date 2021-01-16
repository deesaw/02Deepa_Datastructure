# -*- coding: utf-8 -*-
"""
@author: Megaport
"""

from selenium import webdriver

url = "https://www.google.com"

browser = webdriver.Chrome(executable_path = "C:/Users/Megaport/Desktop/chromedriver/chromedriver")

browser.get(url)

inputElement = browser.find_element_by_id("lst-ib")
inputElement.send_keys("Yahoo Finance")
inputElement.submit()

browser.quit()