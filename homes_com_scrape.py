import time
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

options = Options()
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'--user-agent={user_agent}')
# options.add_argument('--headless')
base_url = 'https://www.homes.com/indianapolis-in/homes-for-rent/'         #https://www.homes.com/indianapolis-in/homes-for-rent/p2/
driver = webdriver.Chrome(options=options)


driver.get(base_url)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.paging')))
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
pager = soup.find('ol')
pages = pager.find_all('li')
page_numbers = []
for page in pages:
    link = page.find('a')
    if link:
        page_numbers.append(link.get('data-page'))

last_page = page_numbers[len(page_numbers) - 1]
print(last_page)


rental_links = []
for i in range(int(last_page)):
    paged_url = base_url + "p" + str(i) + "/"
    driver.get(paged_url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.for-rent-content-container')))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.find_all(class_='for-rent-content-container')
    for link in links:
        anchors = link.find_all('a')
        for anchor in anchors:
            rental_links.append(anchor.get('href'))
            # print(anchor.get('href'))


print(rental_links)

for rental_link in rental_links:
    print(rental_link)

driver.quit()

