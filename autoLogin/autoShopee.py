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

# you are using chrome or firefox?

pathFirefoxDriver = '.\geckodriver'
# pathChromeDriver = '.\chromedriver'

# Lấy config account
accountFile = open("shopeeAccount.txt", "r")
link = accountFile.readline()
username = accountFile.readline()
password = accountFile.readline()
homePage = accountFile.readline()
# Set up cho chrome


# you are using firefox or chrome?
options = Options()
#options.add_argument("user-data-dir=C:\\Users\\ducky\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("user-data-dir=C:\\Users\\ducky\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\Default User")

driver = selenium.webdriver.Firefox(executable_path=pathFirefoxDriver)
# driver = selenium.webdriver.Chrome(executable_path=pathChromeDriver)
driver.get(link)
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
try:
    try:
        if "https://shopee.vn" == link.strip():
            # close popup when open shopee website
            WebDriverWait(driver, 2).until(ec.visibility_of_element_located((By.CLASS_NAME, "shopee-popup__close-btn")))
            close = driver.find_element_by_class_name("shopee-popup__close-btn")
            actionChains = ActionChains(driver)
            actionChains.double_click(close).perform()
            time.sleep(1)

            # click login link
            loginLink = driver.find_element_by_link_text("Đăng Nhập")
            loginLink.click()
            # enter userName and password
            userE = driver.find_element(By.NAME, "loginKey").send_keys(username)
            passE = driver.find_element(By.NAME, "password").send_keys(password)
            # click button login
            btnLogin = driver.find_element_by_css_selector('button._35rr5y._32qX4k._1ShBrl._3z3XZ9._2iOIqx._2h_2_Y')
            WebDriverWait(driver, 2).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button._35rr5y._32qX4k._1ShBrl._3z3XZ9._2iOIqx._2h_2_Y")))
            close = driver.find_element_by_css_selector("button._35rr5y._32qX4k._1ShBrl._3z3XZ9._2iOIqx._2h_2_Y")
            actionChains = ActionChains(driver)
            actionChains.double_click(close).perform()

            # close popup windows after login successful (a popup of shopee home page)
            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "shopee-popup__close-btn")))
            close = driver.find_element_by_class_name("shopee-popup__close-btn")
            actionChains = ActionChains(driver)
            actionChains.double_click(close).perform()

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "shopee-skinny-banner__full-height.V1Fpl5")))
            deal0Vnd = driver.find_element_by_class_name("shopee-skinny-banner__full-height.V1Fpl5")
            actionChains = ActionChains(driver)
            actionChains.double_click(deal0Vnd).perform()


            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "_3IGAiu._1aqQcY")))
            layMa = driver.find_element_by_class_name("_3IGAiu._1aqQcY")
            actionChains = ActionChains(driver)
            for ma in layMa:
                actionChains.double_click(ma).perform()



    except Exception as e:
        print(e)
except Exception as e:
    print(e)
    driver.quit()
