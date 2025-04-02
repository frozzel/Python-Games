from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://python.org")

# Up Coming Events
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')    
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
    
print(events)


# for name in event_names:
#     print(name.text)

# for time in event_times:
#     print(time.text)

driver.quit()