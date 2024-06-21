import time
import json
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager





# https://www.zillow.com/indianapolis-in/rentals/
#https://www.zillow.com/indianapolis-in/rentals/1_p/
#https://www.zillow.com/indianapolis-in/rentals/7_p/
#ZILLOW HAS 20 PAGES
#data-test="property-card-price" IS PRICE
#data-test="property-card-link" IS LINK TO HOME
#data-test="property-card-addr" IS ADDRESS

# https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-86.45366862402344%2C%22east%22%3A-85.83431437597656%2C%22south%22%3A39.52703792041692%2C%22north%22%3A40.032038482462816%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A32149%7D%5D%7D
# headers = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166'}



options = Options()
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'--user-agent={user_agent}')
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1080")
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
options.add_argument('disable-infobars')
options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(options=options)

url = "https://www.zillow.com/indianapolis-in/rentals/"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.search-page-container')))
page_source = driver.page_source
print(page_source)


# rental_links = []
# url = 'https://www.zillow.com/homes/new_homes/'
# ua = UserAgent()
# user_agent = ua.random
# print(user_agent)
# # headers = {'User-Agent': f'{user_agent}'}
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')
#     print(html_content)
#     with open('dump.html', 'w') as f:
#         json.dump(html_content, f, indent=4)
# else:
#     print(response.text)
    # elements = soup.find_all(attrs={'data-testid': 'property-card-link'})   
    # script = soup.find('script', id='__NEXT_DATA__', type='application/json') 
    # if script:
    #     json_data_str = script.string
    #     json_data = json.loads(json_data_str)
    #     homes = json_data['props']['searchData']['homes']
    #     for home in homes:
    #         rental_links.append(home['url'])
        # with open('parsed_data.json', 'w') as f:
        #     json.dump(homes, f, indent=4)
        # print(rental_links)
    # else:
    #     print("Could not find data")


    # with open('dump.html', 'w', encoding='utf-8') as f:
    #     f.write(str(elements))
    # for element in elements:
    #     print(element.text.strip())