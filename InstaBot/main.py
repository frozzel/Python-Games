from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class InstaFollower:

    def __init__(self):
        # Keep browser open so you can manually log out
        options = webdriver.ChromeOptions()
        options.add_argument(r"--user-data-dir=/Users/frozzel/Library/Application Support/Google/Chrome/Profile 1")  # Run in headless mode
        options.add_argument("--profile-directory=Profile 1")  # Replace with your profile name
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/_designhomedecor/followers/")
        time.sleep(5)
        followers_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
        followers_link.click()
        time.sleep(5)
        
    def follow(self):
        # Click on the follow button
        all_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow')]")
        time.sleep(5)
        for button in all_buttons:
            try:
                # Check if the button text is "Follow"
                button.click()
                time.sleep(2)  # Wait for the follow action to complete
            except NoSuchElementException:
                print("No such element found.")
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
            
        # Close the browser
        # self.driver.quit()
        # print("Driver closed.")
        # print("All followers followed.")

        
bot = InstaFollower()
bot.find_followers()
bot.follow()
