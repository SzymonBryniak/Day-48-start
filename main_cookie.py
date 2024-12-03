import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)

# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.implicitly_wait(1)
# all_portals.click()

cookie = driver.find_element(By.ID, value="cookie")
# buyGrandma = driver.find_element(By.ID, value="buyGrandma")
# buyFactory = driver.find_element(By.ID, value="buyFactory")
# buyMine = driver.find_element(By.ID, value="buyMine")
# buyShipment = driver.find_element(By.ID, value="buyShipment")
# buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
# buyPortal = driver.find_element(By.ID, value="buyPortal")
# buyTime_machine = driver.find_element(By.ID, value="buyTime machine")

try:
    while True:
        cookie.click()
        time.sleep(0.1)  # Add a short delay to prevent overwhelming the browser
except KeyboardInterrupt:
    print("Script stopped by user.")
    driver.quit()
 
# driver.quit()
