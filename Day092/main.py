from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
from datetime import datetime


# Getting user inputs, checking if they are in correct format.
try:
    zip_codes_to_search = input(
        "Enter the zip code you want to search for craigslist rentals. If you would like to enter multiple zipcodes, separate them by a comma ',' \n"
        "e.g : 14226,14225,14233\n")
    zip_code_list = zip_codes_to_search.split(",")
    for zip_code in zip_code_list:
        int(zip_code)
except ValueError:
    message_string = ("The value you entered is in invalid format. Please try again.\nEnter the zip code you want to search for craigslist rentals.\n "
                      "If you would like to enter multiple zipcodes, separate them by a comma.\n"
                      "e.g : 14226,14225,14233\n")
    zip_codes_to_search = input(message_string)

try:
    price = input("Please enter the maximum price you want to filter by in just numbers. e.g : 2500\n")
    int(price)
except ValueError:
    price = input("The value you entered is in invalid format. Please try again.\n Please enter the maximum price you want to filter by in just numbers. e.g : 2500\n")

# Starting a separate Selenium Webdriver for every zip code entered.

for zip_codes in zip_code_list:
    all_rentals = []
    driver = webdriver.Chrome()
    driver.get('https://buffalo.craigslist.org/search/hhh?')
    driver.maximize_window()
    time.sleep(2)
    drp_bedrooms = Select(driver.find_element(By.XPATH, '/html/body/section/form/div[2]/div[2]/div[5]/select[2]'))
    drp_bedrooms.select_by_value("6")
    time.sleep(0.5)
    max_price = driver.find_element(By.XPATH, '/html/body/section/form/div[2]/div[2]/div[4]/input[2]')
    max_price.send_keys(price)
    time.sleep(0.5)
    zip_code = driver.find_element(By.XPATH, '/html/body/section/form/div[2]/div[2]/div[3]/input[2]')
    zip_code.send_keys(zip_codes + Keys.ENTER)

    all_results = driver.find_elements(By.CLASS_NAME, 'result-row')

# Scraping the necessary data for the table together from child objects.

    for result in all_results:
        try:
            price = result.find_element(By.CSS_SELECTOR, "span[class='result-price']").text.replace(",", ".")
            price = price.replace("$", "")
            parent = result.find_element(By.CLASS_NAME, 'result-heading')
            link = parent.find_element(By.TAG_NAME, 'a').get_attribute('href')
            parent = result.find_element(By.CLASS_NAME, 'result-meta')
            bedrooms = parent.find_element(By.CLASS_NAME, 'housing').text
            neighborhood = parent.find_element(By.CLASS_NAME, 'result-hood').text
        except NoSuchElementException:
            continue
        else:
            new_rental = [price, bedrooms, neighborhood, link]
            all_rentals.append(new_rental)

    driver.close()
    today = str(datetime.today())
    today = today.replace("-", "_")
    today = today.replace(":", "_")
    today = today.replace(".", "_")
    today = today.replace(" ", "_")
    df = pd.DataFrame(all_rentals, columns=['Price', 'Bedrooms', 'Neighborhood', 'Link'])
    df.to_csv(f"{today}.csv", index=False, sep=',')

driver.quit()
