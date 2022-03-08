from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

#URL of Google Form to store the results of Zillow search. 
GOOGLE_FORM_URL = 'https://forms.gle/MpCQrefNJ5CNKkht9'

#Headers to pass for Zillow
headers = {"accept-Language": "en-US,en;q=0.9",
           "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27"
           }
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66639245996975%2C%22north%22%3A37.88403027709227%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

#Getting the zillow results with BeautifulSoup.
response = requests.get(url=ZILLOW_URL, headers=headers)
result = response.text
soup = BeautifulSoup(result, 'html.parser')

listings = soup.find('ul', class_='photo-cards photo-cards_wow photo-cards_short')

prices = listings.find_all('div', class_='list-card-price')
price_list = []

addresses = listings.find_all("address")
address_list = []

links = listings.find_all("a")
link_list = []

# Structuring the data from the results into a desirable format.
for price in prices:
    if "+" in price.text:
        new_price = price.text.split("+")[0]
        price_list.append(new_price)
    else:
        price_list.append(price.text.split("/")[0])

for address in addresses:
    address_list.append(address.text)

for link in links:
    if 'https://' not in link['href']:
        new_link = 'https://www.zillow.com' + link['href']
        if new_link not in link_list:
            link_list.append(new_link)
    elif link['href'] not in link_list:
        link_list.append(link['href'])

        
# Opening Google Form with Selenium to fill the data from the results automatically in to Form.
driver = webdriver.Chrome()
driver.get(GOOGLE_FORM_URL)
driver.maximize_window()
for i in range(len(link_list)):
    time.sleep(2)
    address_field = driver.find_element(By.XPATH,
                                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(address_list[i])
    price_field = driver.find_element(By.XPATH,
                                      '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price_list[i])
    link_field = driver.find_element(By.XPATH,
                                     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(link_list[i])
    submit_button = driver.find_element(By.XPATH,
                                        '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    go_next = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    go_next.click()

driver.close()
driver.quit()
