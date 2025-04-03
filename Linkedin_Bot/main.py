from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()
    

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/frozzel/Library/Application Support/Google/Chrome/Profile 1")  # Run in headless mode
options.add_argument("--profile-directory=Profile 1")  # Replace with your profile name

options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4179363167&f_AL=true&f_E=2%2C3&f_JT=F%2CC&f_WT=2&keywords=full%20stack%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

time.sleep(3)

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try: 
        # Click Apply Button
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(3)

        next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        next_button.click()
        time.sleep(3)

        next_button2 = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        next_button2.click()
        time.sleep(3)

        review_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")

        review_button.click()
        time.sleep(3)

        submit_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()
            
        time.sleep(3)
        # Click Done Button
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()   
        
    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue 
            
time.sleep(5)
driver.quit()