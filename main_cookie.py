import time
from win32 import win32file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from get_chrome_driver import GetChromeDriver

# get_driver = GetChromeDriver()
# # get_driver.auto_download(extract=True)
# get_driver.install()
win32file._setmaxstdio(2048)
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--no-sandbox")

# Create a service object for ChromeDriver
# chromedriver_path = "C:\webdrivers\chromedriver.exe"  # causes browser mismatch
# service = Service(chromedriver_path)

# service = Service(ChromeDriverManager().install())
service = webdriver.ChromeService(port=1234)
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.current_window_handle
driver.implicitly_wait(2)


cookie = driver.find_element(By.ID, value="cookie")
# cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cookie")))
# buyGrandma = driver.find_element(By.ID, value="buyGrandma")
# buyFactory = driver.find_element(By.ID, value="buyFactory")
# buyMine = driver.find_element(By.ID, value="buyMine")
# buyShipment = driver.find_element(By.ID, value="buyShipment")
# buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
# buyPortal = driver.find_element(By.ID, value="buyPortal")
# buyTime_machine = driver.find_element(By.ID, value="buyTime machine")

try:
    while True:
        # wait = WebDriverWait(driver, timeout=2)
        # wait.until(lambda d : cookie.is_displayed())
        # time.sleep(0.01)
        cookie.click()
          # Add a short delay to prevent overwhelming the browser
except KeyboardInterrupt:
    print("Script stopped by user.")
    driver.quit()
 
driver.quit()
