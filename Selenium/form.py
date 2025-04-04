from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("John")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Doe")
email = driver.find_element(By.NAME, "email")
email.send_keys("frozzel@me.com")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
# Close the browser after a delay
# driver.implicitly_wait(5)
# driver.quit()