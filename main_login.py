from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

# all_portals.click()

First_Name = driver.find_element(By.NAME, value="fName")
Last_Name = driver.find_element(By.NAME, value="lName")
Email_address = driver.find_element(By.NAME, value="email")

First_Name.send_keys("Szymon")
Last_Name.send_keys("Bryniak")
Email_address.send_keys("Szymonbryniak@gmail.com")
Sign_Up = driver.find_element(By.CLASS_NAME, value="btn-block")
Sign_Up.click()


# driver.quit()
