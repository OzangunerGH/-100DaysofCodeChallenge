from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import os

PROMISED_DOWNLOAD = 30
PROMISED_UPLOAD = 10


def get_internet_speed():
    """This function opens Speedtest.net and measures the Download - Upload Speed, then returns them in 'speed_string' variable."""
    st_driver = webdriver.Chrome()
    st_driver.get('https://speedtest.net')
    st_driver.maximize_window()
    time.sleep(2)
    speedtest = st_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
    speedtest.click()
    time.sleep(50)
    download = st_driver.find_element(By.XPATH,
                                      '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    upload = st_driver.find_element(By.XPATH,
                                    '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
    speed_string = f"@TurkTelekom My current internet speed is:  Download: {download.text} Upload: {upload.text}" \
                   f"My promised internet speed in my contract is : Download: {PROMISED_DOWNLOAD} Upload: {PROMISED_UPLOAD}"
    return speed_string


def tweet_at_provider():
    """This function logins to Twitter automatically and Tweets the 'Tweet_message' variable."""
    email = os.environ.get("Twitter_email")
    password = os.environ.get("Twitter_password")
    tw_driver = webdriver.Chrome()
    tw_driver.get('https://twitter.com')
    tw_driver.maximize_window()
    time.sleep(2)
    sign_in = tw_driver.find_element(By.XPATH,
                                     '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
    sign_in.click()
    tw_driver.maximize_window()
    time.sleep(2)
    email_input = tw_driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
    email_input.send_keys(email)
    next_button = tw_driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
    next_button.click()
    time.sleep(2)
    try:
        password_input = tw_driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
    except NoSuchElementException:
        time.sleep(2)
        username_input = tw_driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_input.send_keys('ozanguner15')
        next_but = tw_driver.find_element(By.XPATH,
                                          '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        next_but.click()
        time.sleep(2)
        password_input = tw_driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(password)
        login_button = tw_driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        login_button.click()
        time.sleep(3)
        tweet_button = tw_driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_button.click()
        tweet_body = tw_driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet_body.send_keys(tweet_message)
        time.sleep(3)
        submit_tweet = tw_driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        submit_tweet.click()
    return tw_driver


# Getting Speedtest results and saving results to tweet_message variable.

tweet_message = get_internet_speed()

# calling tweet_at_provider method to tweet the results and the promised speeds to the provider through Twitter.

driver = tweet_at_provider()
time.sleep(15)
driver.close()
driver.quit()
