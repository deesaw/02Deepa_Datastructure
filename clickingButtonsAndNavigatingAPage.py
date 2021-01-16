# -*- coding: utf-8 -*-
"""
@author: Megaport
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.google.com"

browser = webdriver.Chrome(executable_path = "C:/Users/Megaport/Desktop/chromedriver/chromedriver")

browser.get(url)

inputElement = browser.find_element_by_id("lst-ib")
inputElement.send_keys("Yahoo Finance")
inputElement.submit()

#element = browser.find_element_by_xpath('//*[@id="Rzn5id"]/div/a[2]')
#element.click()

element = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Rzn5id"]/div/a[2]'))).click()

element = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/table/tbody/tr[2]/td[2]/div/span/h3/a')
element.click()

element = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div[2]/form[1]/div/input'))).click()


#browser.quit()