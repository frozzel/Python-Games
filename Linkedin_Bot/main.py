from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/frozzel/Library/Application Support/Google/Chrome/Profile 1")  # Run in headless mode
options.add_argument("--profile-directory=Profile 1")  # Replace with your profile name

options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/in/dennis-hickox-1b0a10227/")

print(driver.title)