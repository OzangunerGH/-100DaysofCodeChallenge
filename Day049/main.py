# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.common.exceptions import NoSuchElementException

# Environment variables to automatically sign-in to Linkedin.
email = os.environ.get("Linkedin_email")
password = os.environ.get("Linkedin_password")

#Creating the webdriver ( Service class is not needed as the driver is in the same directory.)
driver = webdriver.Chrome()
driver.maximize_window()
# You can put any Linkedin URL here. Go to jobs sections, apply easy apply filter. After that apply any additional filter you would like (optional), 
# type in your keyword, press search, then copy the url. 
driver.get(
    "https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States") 

#Signing in
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(email)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
sign_button = driver.find_element(By.CLASS_NAME, "login__form_action_container")
sign_button.click()
time.sleep(2)

#Finding all job listings.
all_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")


for listing in all_listings:
    listing.click()
    time.sleep(2)
    # Trying to press submit button. If there is a different button than submit,(ex: "Next" button), it discards the application pop-up window and goes to the next listing.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button')
            close.click()
            time.sleep(2)
            discard = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[1]')
            discard.click()
        else:
            submit_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button')
            submit_button.click()
            print("Successfully applied to the listing.")
    # If the apply button is not there for exception cases ( E.G : Already applied before.)
    except NoSuchElementException:
        print("Already applied before or submit button does not exist.")
        continue

driver.close()
driver.quit()
