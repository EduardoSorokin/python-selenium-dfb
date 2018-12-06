#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json


# Setting the Chrome Web Driver -----------------------------------------------
"""
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
"""

# Setting the Firefox Web Driver ----------------------------------------------

driver = webdriver.Firefox()
driver.maximize_window()


# Variables -------------------------------------------------------------------

username = ''
password = ''


# Login -----------------------------------------------------------------------

driver.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_css_selector('button[type="submit"]').click()


# Changing to profile page ----------------------------------------------------

time.sleep(1)

driver.get('https://www.instagram.com/%s' % username)

time.sleep(1)


# Checking the followers ------------------------------------------------------

followers_link = driver.find_element_by_css_selector('a[href="/%s/followers/"]' % username)
followers_qty = int(followers_link.find_element_by_css_selector('span').text)
followers_link.click()

time.sleep(2)

followers_container = driver.find_element_by_css_selector('div[class="isgrP"]')
followers_list = driver.find_element_by_css_selector('div[role="dialog"] ul').get_attribute('innerHTML')

time.sleep(2)

while followers_list.count('</li>') < followers_qty:
	driver.execute_script('arguments[0].scrollTop += 250', followers_container)
	time.sleep(0.5)
	followers_list = driver.find_element_by_css_selector('div[role="dialog"] ul').get_attribute('innerHTML')

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

# Checking who I follow -------------------------------------------------------

following_link = driver.find_element_by_css_selector('a[href="/%s/following/"]' % username)
following_qty = int(following_link.find_element_by_css_selector('span').text)
following_link.click()

time.sleep(2)

following_container = driver.find_element_by_css_selector('div[class="isgrP"]')
following_list = driver.find_element_by_css_selector('div[role="dialog"] ul').get_attribute('innerHTML')

time.sleep(2)

while following_list.count('</li>') < following_qty:
	driver.execute_script('arguments[0].scrollTop += 250', following_container)
	time.sleep(0.5)
	following_list = driver.find_element_by_css_selector('div[role="dialog"] ul').get_attribute('innerHTML')

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


# Logout ----------------------------------------------------------------------

time.sleep(0.5)

driver.get('https://www.instagram.com/accounts/logout/')


# Beautiful Soup - Followers --------------------------------------------------

soup = BeautifulSoup(followers_list, 'html.parser')

formated_followers_list = []

for li in soup.find_all("li"):
    formated_followers_list.append(
        {
            'usr': li.a['href'][1:-1],
            'src': li.img['src']
        }
    )

if followers_qty != len(formated_followers_list):
    print('[ERROR] Something went wrong while formating the followers list.\nAborted!')
    driver.quit()

# Beautiful Soup - Following --------------------------------------------------

soup = BeautifulSoup(following_list, 'html.parser')

formated_following_list = []

for li in soup.find_all("li"):
    formated_following_list.append(
        {
            'usr': li.a['href'][1:-1],
            'src': li.img['src']
        }
    )

if following_qty != len(formated_following_list):
    print('[ERROR] Something went wrong while formating the list of who you are following.\nAborted!')
    driver.quit()

# DFB -------------------------------------------------------------------------

driver.get('http://rocknrollpixel.pythonanywhere.com/dont-follow-back')

driver.find_element_by_id('followers').send_keys(json.dumps(formated_followers_list))
driver.find_element_by_id('following').send_keys(json.dumps(formated_following_list))
driver.find_element_by_id('check').click()


# THE END ---------------------------------------------------------------------

print('All done!')

quit()
