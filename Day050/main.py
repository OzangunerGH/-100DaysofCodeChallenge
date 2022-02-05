# Importing necessary libraries to use.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from selenium.webdriver.common.keys import Keys

# Enter your tinder e-mail address and password ( Save it as an environment variable)
email = os.environ.get("Tinder_email")
password = os.environ.get("Tinder_password")

#Getting chrome web driver initiated (Chromweb driver is in the same directory so Service is not needed.)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tinder.onelink.me/9K8a/3d4abb81")

time.sleep(3)
#Accepting Cookies pop-up and logging in.
cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/button')
cookies.click()
facebook_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()
time.sleep(1)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(window_name=fb_login_window)
time.sleep(2)
# Sending email and password to login with facebook pop-up.  
email_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_input.send_keys(email)
password_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(3)
driver.switch_to.window(base_window)
time.sleep(3)
# Allowing tinder to use location data.
allow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_button.click()
time.sleep(3)
# Clicking on "Not interested" on notification pop-up.
no_notifications = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]')
no_notifications.click()
time.sleep(5)

# Clicking like 100 times (Because tinder has a 100 like limit for free tier.)
for n in range(100):
    time.sleep(3)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          '//*[@id="q1413092675"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
    except NoSuchElementException:
        try:
            like_button = driver.find_element(By.XPATH,
                                          '//*[@id="q1413092675"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
            like_button.click()
       
        except ElementClickInterceptedException:
            try:
                time.sleep(2)
                match_popup = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button')
                match_popup.click()
            except NoSuchElementException:
                not_interested = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[2]')
                not_interested.click()
driver.close()
driver.quit()




