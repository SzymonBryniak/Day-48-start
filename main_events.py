from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

keys = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
values = driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")
numbers = [i for i in range(len(keys))]

# itest = {i.text: ii.text for i in menu_time for ii in menu_a}
# print(itest)

myDict = {i:{"time":k.text, "name":v.text} for (k,v) in zip(keys, values) for i in numbers} 
print(myDict)
# zip_events = dict(zip(numbers, (keys, values)))
# print(zip_events)



driver.quit()
