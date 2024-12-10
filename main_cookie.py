import time
import re
import functools
import operator
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
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

# get_driver = GetChromeDriver()
# # get_driver.auto_download(extract=True)
# get_driver.install()
win32file._setmaxstdio(2048)
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'none'
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--no-sandbox")

# Create a service object for ChromeDriver
# chromedriver_path = "C:\webdrivers\chromedriver.exe"  # causes browser mismatch
# service = Service(chromedriver_path)

# service = Service(ChromeDriverManager().install())
# service = webdriver.ChromeService(port=1234)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


driver.current_window_handle
driver.implicitly_wait(2)


cookie = driver.find_element(By.ID, value="cookie")



# cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cookie")))
buyCursor = driver.find_element(By.ID, value="buyCursor")
buyGrandma = driver.find_element(By.ID, value="buyGrandma")
buyFactory = driver.find_element(By.ID, value="buyFactory")
buyMine = driver.find_element(By.ID, value="buyMine")
buyShipment = driver.find_element(By.ID, value="buyShipment")
buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
buyPortal = driver.find_element(By.ID, value="buyPortal")
buyTime_machine = driver.find_element(By.ID, value="buyTime machine")



def is_available(*args):
    greyed = "grayed" in buyGrandma.get_attribute("class")
    print(greyed)
    print(buyGrandma.text)
    find_digits = re.findall("\d", buyFactory.text)
    concatenate_no_spaces = functools.reduce(operator.add, find_digits)
    print(concatenate_no_spaces)
    if greyed == False:
        buyGrandma.click()

def click_decorator():
    def inner(*args):
        return

def to_click(*args):
    # not_grayed = [f"not: {i}" if "grayed" in args[i].get_attribute("class") else f'to click: {i}' for i in range(len(args))]
    not_grayed = [False if "grayed" in args[i].get_attribute("class") else True for i in range(len(args))]
    print(not_grayed)
    # is_available = {x.get_attribute("id"):not_grayed[y] for x in args for y in range(len(not_grayed))}
    is_available = {args[x].get_attribute("id"):not_grayed[y] for x in range(len(args)) for y in range(len(not_grayed))}
    print(is_available)



# is_available(buyGrandma)
start_time = round(time.time())

try:
    while True:

        # wait = WebDriverWait(driver, timeout=2)
        # wait.until(lambda d : cookie.is_displayed())
        # time.sleep(0.01)
        current_time = round(time.time())
        elapsed_time = current_time - start_time
        if round(elapsed_time) % 5 == 0:
            print(elapsed_time)
            # is_available(buyGrandma)
            to_click(buyCursor, buyGrandma, buyFactory, buyMine, buyShipment, buyShipment, buyAlchemy, buyPortal, buyTime_machine)
            
        
        cookie.click()
        # Add a short delay to prevent overwhelming the browser
 
except KeyboardInterrupt:
    print("Script stopped by user.")
    driver.quit()
 
driver.quit()
