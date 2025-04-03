from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element
cookie = driver.find_element(By.ID, "cookie")

for i in range(15):
    # Click the cookie
    cookie.click()
    
# Buy upgrades

cursor = driver.find_element(By.ID, "buyCursor")
cursor.click()

for i in range(85):
    # Click the cookie
    cookie.click()
    
# Buy upgrades
grandma = driver.find_element(By.ID, "buyGrandma")
grandma.click()

for i in range(400):
    # Click the cookie
    cookie.click()
    
factory = driver.find_element(By.ID, "buyFactory")
factory.click()

for i in range(1500):
    # Click the cookie
    cookie.click()
    
mine = driver.find_element(By.ID, "buyMine")
mine.click()

for i in range(5000):
    # Click the cookie
    cookie.click()
    
shipment = driver.find_element(By.ID, "buyShipment")
shipment.click()

for i in range(43000):
    # Click the cookie
    cookie.click()
    
lab = driver.find_element(By.ID, "buyAlchemy lab")
lab.click()

for i in range(950000):
    # Click the cookie
    cookie.click()
    
portal = driver.find_element(By.ID, "buyPortal")
portal.click()

for i in range(122456789):
    # Click the cookie
    cookie.click()
    
time_machine = driver.find_element(By.ID, "buyTime machine")
time_machine.click()


    
    
    
    



# t_end = time.time() + 5
# while time.time() < t_end:
#     cookie.click()