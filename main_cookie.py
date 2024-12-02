from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# all_portals.click()

cookie = driver.find_element(By.ID, value="cookie")
# buyGrandma = driver.find_element(By.ID, value="buyGrandma")
# buyFactory = driver.find_element(By.ID, value="buyFactory")
# buyMine = driver.find_element(By.ID, value="buyMine")
# buyShipment = driver.find_element(By.ID, value="buyShipment")
# buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
# buyPortal = driver.find_element(By.ID, value="buyPortal")
# buyTime_machine = driver.find_element(By.ID, value="buyTime machine")

while True:
  cookie.click()

# driver.quit()
