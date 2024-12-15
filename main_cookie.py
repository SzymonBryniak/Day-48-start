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


# get_driver = GetChromeDriver()
# # get_driver.auto_download(extract=True)
# get_driver.install()
win32file._setmaxstdio(2048)
chrome_options = webdriver.EdgeOptions()
chrome_options.page_load_strategy = 'eager'
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--no-sandbox")
# Create a service object for ChromeDriver
chromedriver_path = "C:\webdrivers\msedgedriver.exe"  # causes browser mismatch
service = Service(chromedriver_path)
# service = Service(ChromeDriverManager().install())
# service = webdriver.ChromeService(port=1234)
driver = webdriver.Edge(options=chrome_options, service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.current_window_handle
driver.implicitly_wait(2)
start_time = time.time()
   
    # cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cookie")))

def get_menu():
    buyCursor = driver.find_element(By.ID, value="buyCursor")
    buyGrandma = driver.find_element(By.ID, value="buyGrandma")
    buyFactory = driver.find_element(By.ID, value="buyFactory")
    buyMine = driver.find_element(By.ID, value="buyMine")
    buyShipment = driver.find_element(By.ID, value="buyShipment")
    buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
    buyPortal = driver.find_element(By.ID, value="buyPortal")
    buyTime_machine = driver.find_element(By.ID, value="buyTime machine")
    buyCursor = driver.find_element(By.ID, value="buyCursor")
    buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
    return [buyCursor, buyGrandma, buyFactory, buyMine, buyShipment, buyAlchemy, buyPortal, buyTime_machine]

# buyGrandma = driver.find_element(By.ID, value="buyGrandma")
# buyFactory = driver.find_element(By.ID, value="buyFactory")
# buyMine = driver.find_element(By.ID, value="buyMine")
# buyShipment = driver.find_element(By.ID, value="buyShipment")
# buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
# buyPortal = driver.find_element(By.ID, value="buyPortal")
# buyTime_machine = driver.find_element(By.ID, value="buyTime machine")

    # return [buyCursor, buyGrandma, buyFactory, buyMine, buyShipment, buyAlchemy, buyPortal, buyTime_machine]


# def is_available(*args):
#     greyed = "grayed" in buyGrandma.get_attribute("class")
#     print(greyed)
#     print(buyGrandma.text)
#     find_digits = re.findall("\d", buyFactory.text)
#     concatenate_no_spaces = functools.reduce(operator.add, find_digits)
#     print(concatenate_no_spaces)
#     if greyed == False:
#         buyGrandma.click()

def click_decorator():
    def inner(*args):
        return
 
def to_click():
    menu = [
    driver.find_element(By.ID, value="buyCursor"),
    driver.find_element(By.ID, value="buyGrandma"),
    driver.find_element(By.ID, value="buyFactory"),
    driver.find_element(By.ID, value="buyMine"),
    driver.find_element(By.ID, value="buyShipment"),
    driver.find_element(By.ID, value="buyAlchemy lab"),
    driver.find_element(By.ID, value="buyPortal"),
    driver.find_element(By.ID, value="buyTime machine")
    ]
    # print(menu[4][0].get_attribute("class"))
    not_grayed = [False if "grayed" in menu[i].get_attribute("class") else True for i in range(len(menu))]
    is_available = {menu[x]:not_grayed[x] for x in range(len(menu))}
    selection = [k for k, v in is_available.items() if v == True]
    return selection[-1]
    

modulo = 5
def elapsed_time_check(elapsed):
    global modulo
    if elapsed % modulo == 0 and elapsed != 0 and modulo < 300:
            print(f'elapsed: {elapsed}')
            modulo += 10
            print(modulo)
            x = to_click()
            x.click()
    elif modulo > 300:
        print(f'cookies/second : {driver.find_element(By.ID, value='cps').text}')
        return True



def click_menu_item(item):
    if item != None:
        to_click = driver.find_element(By.ID, value=item[-1])
        to_click.click()
    return
try:
    while True:
        # get_menu()
        current_time = time.time()
        elapsed_time = current_time - start_time
        cookie = driver.find_element(By.ID, value="cookie")
        cookie.click()
        # click_menu_item(elapsed_time_check(round(elapsed_time)))
        x = elapsed_time_check(round(elapsed_time))
        if x:
            break
 
except KeyboardInterrupt:
    print("Script stopped by user.")
    driver.quit()
 
driver.quit()
