from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os


def get_follower_count():
    """Gets the number of instagram followers of the account and returns it in an integer format."""
    follower_count = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/div/span').text
    if "k" in follower_count:
        follower_count = follower_count.replace('k', '000')
        follower_count = int(follower_count)
    elif "m" in follower_count:
        follower_count = follower_count.replace('.', '')
        follower_count = follower_count.replace('m', '000000')
        follower_count = int(follower_count)
    else:
        follower_count = int(follower_count)

    return follower_count

# Set environment variables for instagram account e-mail and password.
EMAIL = os.environ.get('Instagram_email')
PASSWORD = os.environ.get('Instagram_password')

follow_auto = input(
    "Whose instagram followers you want to follow automatically ? "
    "Put in the correct instagram account name.\n").lower()

# Getting Selenium to open instagram to login. Put the chromedriver.exe inside same directory as Python for this to work.
driver = webdriver.Chrome()
driver.get('https://instagram.com')
driver.maximize_window()
time.sleep(2)
email_input = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
email_input.send_keys(EMAIL)
time.sleep(1)
password_input = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
password_input.send_keys(PASSWORD)
time.sleep(1)
login_b = driver.find_element(By.XPATH,
                              '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login_b.click()
time.sleep(3)


# Clicking necessary buttons on pop-ups to disappear once logged in. (Such as , no notifications etc.)
not_now_b = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/main/div/div/div/div/button')
not_now_b.click()
time.sleep(2)
try:
    no_notifications_b = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
    no_notifications_b.click()
except NoSuchElementException:
    no_notifications_b = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
    no_notifications_b.click()
time.sleep(2)

# Searching for the instagram account that user inputted, and selecting the first account from the search results.

search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys(follow_auto)
time.sleep(3)
insta_account = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
insta_account.click()
time.sleep(5)


# Getting the number of followers and passing it to the function to get it in the integer form. Then clicking on followers button to start following the followers.
followers = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]')
followers.click()
time.sleep(3)

people_to_follow = get_follower_count()

# Following the followers from 1 to number of followers in a for loop. Exceptions are handled below.
for i in range(1, people_to_follow):
    time.sleep(2)
    try:
        button = driver.find_element(By.XPATH, f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button')
        if button.text == "Follow":
            button.click()
    except NoSuchElementException:
        try:
            button = driver.find_element(By.XPATH,
                                         f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button')
            if button.text == "Follow":
                button.click()
        except ElementClickInterceptedException:
            ok_button = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[2]/button[2]')
            ok_button.click()
            time.sleep(3)
            continue

driver.close()
driver.quit()
