import json
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



def setup_scrape_url(location, rent_or_sale):
    rent_or_sale_specification = ''
    base_url = 'https://www.homes.com/'

    if rent_or_sale == 'rent':
        rent_or_sale_specification = 'homes-for-rent/'
    else:
        rent_or_sale_specification = ''

    built_url = base_url + location + '/' + rent_or_sale_specification
    print(built_url)
    return built_url


def scrape(url):
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

        # base_url = 'https://www.homes.com/indianapolis-in/homes-for-rent/'         #https://www.homes.com/indianapolis-in/homes-for-rent/p2/
    driver = webdriver.Chrome(options=options)
    # driver.set_window_size(1200, 600)


    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.paging')))
    page_source = driver.page_source
    print(page_source)
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
        time.sleep(0.5)
        i += 1
        paged_url = url + "p" + str(i) + "/"
        driver.get(paged_url)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'script[type="application/ld+json"]')))
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        scripts = soup.find_all('script', type='application/ld+json') 
        if len(scripts) > 1:
            correct_script = scripts[len(scripts) - 1]
            correct_script_str = correct_script.string
            housing_data = json.loads(correct_script_str)
            with open('parsed_data.json', 'w') as f:                    
                json.dump(housing_data, f, indent=4)
            units = housing_data['mainEntity']['itemListElement']
            for unit in units:
                rental_links.append(unit['url'])
    return rental_links

#     return rental_links
    #     links = soup.find_all(class_='for-rent-content-container')
    #     for link in links:
    #         anchors = link.find_all('a')
    #         for anchor in anchors:
    #             rental_links.append(anchor.get('href'))
    #             print(anchor.get('href'))


   # with open('dump.html', 'w', encoding='utf-8') as f:
        #     f.write(str(page_source))        


def begin_scrape(location, rent_or_sale):
    url = setup_scrape_url(location, rent_or_sale)
    links = scrape(url)
    return links

# begin_scrape('indianapolis-in', 'rent')






# print(rental_links)

# for rental_link in rental_links:
#     print(rental_link)

# driver.quit()


# with open('dump.html', 'w', encoding='utf-8') as f:
#         f.write(str(html_content))


# base_url = 'https://www.homes.com/indianapolis-in/homes-for-rent/'













# location_specification = ''
# rent_or_sale_specification = ''
# base_url = 'https://www.homes.com/'


# def setup_scrape_url(location, rent_or_sale):
#     #location would be something like indianapolis-in
#     #rent_or_sale would equal either 'rent' or 'sale'
#     global rent_or_sale_specification
#     global base_url

#     if rent_or_sale == 'rent':
#         rent_or_sale_specification = 'homes-for-rent/'
#     else:
#         rent_or_sale_specification = ''

#     built_url = base_url + location + '/' + rent_or_sale_specification
#     print(built_url)
#     return built_url




# def scrape(url):
#     ua = UserAgent()
#     user_agent = ua.random
#     print(user_agent)


#     #find number of pages
#     number_of_pages = 1
#     page_numbers = []
#     session = requests.Session()
#     session.headers.update({'User-Agent': f'{user_agent}',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.google.com/',
#     'Connection': 'keep-alive'
#     })
#     # headers = {'User-Agent': f'{user_agent}'}
#     # headers = {
#     # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
#     # }
#     # response = requests.get(url, headers=headers)
#     print(url)
#     response = session.get(url)
#     if response.status_code == 200:
#         html_content = response.text
#         soup = BeautifulSoup(html_content, 'html.parser')
#         pager = soup.find(class_="paging")
#         if pager:
#             page_list = pager.find('ol')
#             page_list_items = page_list.find_all('li')
#             for item in page_list_items:
#                 page = item.find('a')
#                 if page:
#                     page_numbers.append(page.get('data-page'))
            
#             number_of_pages = page_numbers[len(page_numbers) - 1]
#     else:
#         print(response.text)

#     print(number_of_pages)


#     rental_links = []
#     for i in range(int(number_of_pages)):
#         time.sleep(2)
#         i += 1
#         paged_url = url + "p" + str(i) + "/"
#         response = session.get(paged_url)
#         if response.status_code == 200:
#             html_content = response.text
#             soup = BeautifulSoup(html_content, 'html.parser')
#             scripts = soup.find_all('script', type='application/ld+json') 
#             if len(scripts) > 1:
#                 second_script = scripts[1]
#                 second_script_str = second_script.string
#                 housing_data = json.loads(second_script_str)
#                 with open('parsed_data.json', 'w') as f:
#                     json.dump(housing_data, f, indent=4)
#                 units = housing_data['mainEntity']['itemListElement']
#                 for unit in units:
#                     rental_links.append(unit['url'])

#     return rental_links

# def begin_scrape(location, rent_or_sale):
#     url = setup_scrape_url(location, rent_or_sale)
#     links = scrape(url)
#     print(links)



# begin_scrape('indianapolis-in', 'sale')