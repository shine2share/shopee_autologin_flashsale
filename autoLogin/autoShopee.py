import selenium
import pickle
import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from string import Template

# you are using chrome or firefox?

#pathFirefoxDriver = '.\geckodriver'
pathChormDriver = '.\chromedriver'

# Lấy config account
acountFile = open("shopeeAccount.txt", "r")
link = acountFile.readline()
username = acountFile.readline()
password = acountFile.readline()

# Set up cho chorme


######################### you are using firefox or chrome? #########################
options = Options()
options.add_argument("user-data-dir=C:\\Users\\ducky\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

#driver = selenium.webdriver.Firefox(executable_path=pathFirefoxDriver)
driver = selenium.webdriver.Chrome(executable_path=pathChormDriver)
driver.get(link)
#pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
try:
	# chờ load xong trang bao giờ hiện ra cái này thì là xong rồi

	#loginbox =  WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.NAME, 'loginKey')))

	# thực hiện login
	try:
        
		usserE = driver.find_element(By.NAME, "loginKey").send_keys(username)
		passE = driver.find_element(By.NAME, "password").send_keys(password)
		btnLogin = driver.find_element_by_css_selector("button._35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y").click()
		
	except Exception as e:
		print(e)
		#pass
except Exception as e:
	print(e)
	driver.quit()