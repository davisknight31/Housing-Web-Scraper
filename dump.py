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
from selenium.webdriver.common.proxy import Proxy, ProxyType



# options = Options()
# ua = UserAgent()
# user_agent = ua.random
# options.add_argument(f'--user-agent={user_agent}')
# options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# proxy = "172.183.241.1:8080"
# options.add_argument(f"--proxy-server={proxy}")
# url = 'https://www.homes.com/indianapolis-in/homes-for-rent/'

# url = 'https://www.trulia.com/for_rent/Indianapolis,IN/'
# driver = webdriver.Chrome(options=options)
# driver.get(url)

# options = webdriver.ChromeOptions()
# options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
# driver = webdriver.Chrome(options=options)



# for i in range(10):
#     driver.implicitly_wait(2)
#     driver.execute_script("window.scrollTo(0, 500);")


# WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.PropertyCard__StyledLink-sc-2abac362-3')))
# locators = [(By.CSS_SELECTOR, '.for-rent-content-container'), By.CSS_SELECTOR, '.for-rent-content-container']



# responses = []
# headers = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166'}
# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
#     soup = BeautifulSoup(html_content, 'lxml')
#     apartment_links = soup.find_all(class_='PropertyCard__StyledLink-sc-2abac362-3')
#     print(apartment_links)
#     for link in apartment_links:
#         print('t')
#         print(link.get('href'))
# else:
#     print("Failed to retrieve the webpage. Status code: {response.status_code}")


options = Options()
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'--user-agent={user_agent}')
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

# pages_list = []

# for page in pages:
#     pages_list.append(page)
# last_page = pages_list[len(pages_list) - 2]
# print(last_page.find)


# WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.for-rent-content-container')))


# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')

# links = soup.find_all(class_='for-rent-content-container')

# for link in links:
#     print(link.find('a'))
#     anchors = link.find_all('a')
#     print(anchors)
#     for anchor in anchors:
#         print(anchor.get('href'))



# root = tk.Tk()
# root.title("Web Scraper")

# frame = ttk.Frame(root, padding="10")
# frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# ttk.Label(frame, text="URL:").grid(column=1, row=1, sticky=tk.W)
# entry = ttk.Entry(frame, width=50)
# entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

# scrape_button = ttk.Button(frame, text="Scrape", command=scrape)
# scrape_button.grid(column=3, row=1, sticky=tk.E)

# result_label = ttk.Label(frame, text="")
# result_label.grid(column=1, row=2, columnspan=3, sticky=(tk.W, tk.E))

# root.mainloop()