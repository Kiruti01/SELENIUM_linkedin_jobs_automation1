from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

ACCOUNT_EMAIL = "mYEMAIL@gmail.com"
ACCOUNT_PASSWORD = "******"

chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.get(url.encode("ascii", "ignore").decode("unicode_escape"))

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

username_email = driver.find_element(By.ID, "username")
username_email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

