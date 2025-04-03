from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# eng_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount > ul > li:nth-child(2) > a:nth-child(1)")

# eng_articles.click()

# click_link = driver.find_element(By.LINK_TEXT, "Content portals")
# click_link.click()

search_box = driver.find_element(By.NAME, "search")
# search_box.send_keys("Python (programming language)")
search_box.send_keys("Python", Keys.RETURN)
# search_box.submit()
# driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT, "Python (programming language)").click()
# driver.implicitly_wait(10)

# driver.quit()