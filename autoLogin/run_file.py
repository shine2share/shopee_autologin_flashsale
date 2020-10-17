import selenium
import pickle
import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
from string import Template
from selenium.webdriver.common.keys import Keys

from autoShopee import driver, link


class Shopee(object):
    pathChromeDriver = '.\chromedriver'
    # Lấy config account
    accountFile = open("shopeeAccount.txt", "r")
    link = accountFile.readline()
    username = accountFile.readline()
    password = accountFile.readline()
    homePage = accountFile.readline()
    driver = selenium.webdriver.Chrome(executable_path=pathChromeDriver)
    # cookies
    # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    def login(self):
        driver.get(link)

    def google(self):
        driver.get("google.com")


shopee = Shopee()
shopee.login()
