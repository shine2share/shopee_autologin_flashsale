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

# Function definition
def getinfologin():
    global link, username, password
    accountFile = open("shopeeAccount.txt", "r")
    link = accountFile.readline()
    username = accountFile.readline()
    password = accountFile.readline()


def addcookie():
    global cookies
    # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)


def buyproduct():
    global e
    # get all element with 1k class
    item1k = driver.find_elements_by_class_name("SlvYAy")
    for idxItem1k, valItem1k in enumerate(item1k):
        if "1.000" == valItem1k.text:
            print("Bắt đầu mua item thứ " + str((idxItem1k + 1)) + " có giá: " + valItem1k.text)
            # click on item to view item detail
            valItem1k.click()
            # class of button Mua Ngay: btn btn-solid-primary btn--l YtgjXY
            WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.CLASS_NAME, "btn.btn-solid-primary.btn--l.YtgjXY")))
            muaNgay = driver.find_element_by_class_name("btn.btn-solid-primary.btn--l.YtgjXY")
            muaNgay.click()
            try:
                if "Vui lòng chọn Phân loại hàng" == driver.find_element_by_class_name("QiI0pP").text:
                    colorAndSize = driver.find_elements_by_class_name("product-variation")
                    for idxColor, valColor in enumerate(colorAndSize):
                        if valColor.is_enabled():
                            valColor.click()
                            if "m" == valColor.text or "L" == valColor.text:
                                break
                    muaNgay.click()
                    print("Mua xong item thứ " + str(idxItem1k + 1))
            except Exception as e:
                print("end of flow")
        break

def login():
    time.sleep(1)
    # click login link
    loginLink = driver.find_element_by_link_text("Đăng Nhập")
    loginLink.click()
    # enter userName and password
    time.sleep(1)
    userE = driver.find_element(By.NAME, "loginKey").send_keys(username)
    passE = driver.find_element(By.NAME, "password").send_keys(password)
    # click button login
    btnLogin = driver.find_element_by_css_selector('button._35rr5y._32qX4k._1ShBrl._3z3XZ9._2iOIqx._2h_2_Y')
    WebDriverWait(driver, 2).until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "button._35rr5y._32qX4k._1ShBrl._3z3XZ9._2iOIqx._2h_2_Y")))
    close = driver.find_element_by_css_selector("button._35rr5y._32qX4k._1ShBrl._3z3XZ9._2iOIqx._2h_2_Y")
    actionChains = ActionChains(driver)
    actionChains.double_click(close).perform()


def closepopup():
    global close, actionChains
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "shopee-popup__close-btn")))
    close = driver.find_element_by_class_name("shopee-popup__close-btn")
    actionChains = ActionChains(driver)
    actionChains.double_click(close).perform()


# Function definition

# Lấy config account
getinfologin()
# Set up cho chrome
# you are using firefox or chrome?
options = Options()
# options.add_argument("user-data-dir=C:\\Users\\ducky\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("user-data-dir=C:\\Users\\ducky\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\Default User")
driver = selenium.webdriver.Firefox(executable_path=pathFirefoxDriver)
# driver = selenium.webdriver.Chrome(executable_path=pathChromeDriver)
driver.get(link)
addcookie()
try:
    if "https://shopee.vn" == link.strip():
        # close popup when open shopee website
        closepopup()
        login()
        # close popup windows after login successful (a popup of shopee home page)
        closepopup()
        # get list of shop name with 1k sale from file (before run tool, please fill in the listShop.txt file
        with open("listShop.txt", "r") as f:
            lines = f.readlines()
            for idxLine, valLine in enumerate(lines):
                print("shop " + str(idxLine+1) + ": " + valLine)
                driver.get("https://shopee.vn/" + valLine)
                # class name of 1k item: SlvYAy
                WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.CLASS_NAME, "SlvYAy")))
                # scroll window to show element
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                buyproduct()
                print("done buy product")
except Exception as e:
    print("in exception: " + e)
    # driver.quit()
