import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


#https://www.trulia.com/for_rent/Indianapolis,IN/25_p/

rental_links = []
last_page = 0
base_url = 'https://www.trulia.com/for_rent/Indianapolis,IN/'
ua = UserAgent()
user_agent = ua.random
print(user_agent)
headers = {'User-Agent': f'{user_agent}'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166'}
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    html_content = response.text
    with open('dump.html', 'w') as f:
        json.dump(html_content, f, indent=4)
    soup = BeautifulSoup(html_content, 'html.parser')
    pages = soup.find_all(attrs={'data-testid': 'pagination-page-link'})
    page_numbers = []
    for page in pages:
        link = page.find('a')
        if link:
            page_numbers.append(link.text)
    last_page = page_numbers[len(page_numbers) - 1]
    last_page = 25

print(last_page)

for i in range(int(last_page)):
    i += 1
    updated_url = base_url + '/' +  str(i) + '_p'
    response = requests.get(updated_url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # elements = soup.find_all(attrs={'data-testid': 'property-card-link'})   
        script = soup.find('script', id='__NEXT_DATA__', type='application/json') 
        if script:
            json_data_str = script.string
            json_data = json.loads(json_data_str)
            homes = json_data['props']['searchData']['homes']
            for home in homes:
                rental_links.append(home['url'])
            # with open('parsed_data.json', 'w') as f:
            #     json.dump(homes, f, indent=4)
    else:
        print("Could not find data")

print(rental_links)




# if response.status_code == 200:
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')
#     # elements = soup.find_all(attrs={'data-testid': 'property-card-link'})   
#     script = soup.find('script', id='__NEXT_DATA__', type='application/json') 
#     if script:
#         json_data_str = script.string
#         json_data = json.loads(json_data_str)
#         homes = json_data['props']['searchData']['homes']
#         for home in homes:
#             rental_links.append(home['url'])
#         # with open('parsed_data.json', 'w') as f:
#         #     json.dump(homes, f, indent=4)
#         print(rental_links)
#     else:
#         print("Could not find data")