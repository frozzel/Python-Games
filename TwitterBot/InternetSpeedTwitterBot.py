from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/frozzel/Library/Application Support/Google/Chrome/Profile 1")  # Run in headless mode
options.add_argument("--profile-directory=Profile 1")  # Replace with your profile name

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



class InternetSpeedTwitterBot:
    def __init__(self,):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)

        try:
            download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
            upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
            self.down = download_speed.text
            self.up = upload_speed.text
        except NoSuchElementException:
            print("No such element found.")
        finally:
            # self.driver.quit()
            print("Driver closed.")
            print(f"Download Speed: {self.down} Mbps")
            print(f"Upload Speed: {self.up} Mbps")
            return self.down, self.up
        
    def tweet_at_provider(self):
        print("Tweeting at provider...")
        self.driver.get("https://x.com/home")
        time.sleep(5)
        # tweet_button = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Tweet']")
        # tweet_button.click()
        # time.sleep(2)

        tweet_text = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for 1000 Mbps? #InternetSpeed"
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
        tweet_box.send_keys(tweet_text)
        time.sleep(5)

        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_button.click()