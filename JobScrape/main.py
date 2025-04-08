import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSc2Y25v8wPEvcCXg45-jiTzJvmECSMVVc6JsWbnN0SbZJ69iA/viewform?usp=header"
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
zillow = response.text
soup = BeautifulSoup(zillow, 'html.parser')

addresses = []
prices = []
links = []

for address in soup.find_all(name='address'):
    addresses.append(address.getText().strip())
    
for price in soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine'):
    prices.append(price.getText().split("+")[0].split("/")[0])
    
for link in soup.find_all(name='a', class_='property-card-link'):
    links.append(link.get('href'))


# create a list of dictionaries
properties = []
for i in range(len(addresses)):
    properties.append({
        "address": addresses[i],
        "price": prices[i],
        "link": links[i]
    })
# print(properties)

# send the data to google form
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/frozzel/Library/Application Support/Google/Chrome/Profile 1")  # Run in headless mode
options.add_argument("--profile-directory=Profile 1")  # Replace with your profile name
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(FORM)

for property in properties:
    time.sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    address.send_keys(property["address"])
    price.send_keys(property["price"])
    link.send_keys(property["link"])
    
    submit = driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span')
    submit.click()
    
    time.sleep(2)
    
    do_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    do_another.click()
    
    