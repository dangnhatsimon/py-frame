# import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from datetime import datetime
from google.cloud import bigquery
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os




# define website and read its content with html parser
chrome_driver='C:/SeleniumDrivers/chromedriver.exe'
url='https://www.realestate.com.au/sold/in-pyrmont,+nsw+2009/list-1?activeSort=solddate&source=refinement'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'} # headers from 'network tab' when inspect website
with open('valid_proxy.txt','r') as f:
    proxies=f.readlines()
os.environ['PATH'] += r'C:/SeleniumDrivers'

def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    driver = webdriver.Chrome(executable_path=chrome_driver, options = chrome_options)
    return driver
driver = configure_driver()
driver.get(url)
driver.implicitly_wait(5) #time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source,features='html.parser')
# soup = BeautifulSoup(page_source,features='html.parser')
# print(soup.prettify())

# # Check status and try to access website
# def request_get(url, headers, retry):
#     for proxy in proxies:
#         try:
#             response = requests.get(url=url,headers=headers,proxies={'http': proxy,'https': proxy})
#             for _ in range(retry):
#                 if response.status_code == 200:
#                     return response
#                 elif response.status_code == 429:
#                     # If rate-limited, wait and then retry
#                     time.sleep(3)  # Adjust the delay as needed
#                 else:
#                     print(f'Failed with status code: {response.status_code}')
#                     # return None
#         except requests.exceptions.ProxyError as e:
#             print(f'Proxy error: {e}')
#     print("All proxies failed. Unable to make the request.")
#     return None
# response = request_get(url=url, headers=headers,retry=3)
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# function scraper
def web_scraper(url):
    date_pattern = r'\d{1,2} [A-Z][a-z]{2} \d{4}'
    format_date='%d %b %Y'
    residential_data = []
    residential_list = soup.find_all('div', class_='residential-card__content')
    for residential_item in residential_list:
        address = residential_item.find('a',{'class':'details-link residential-card__details-link'}).find('span').text.strip()
        sold_date = residential_item.find('div', {'class':'PropertyCardLayout__StyledPipedContent-sc-1qkhjdh-0 dgCHTg'}).find('span').text.strip()
        sold_date_formatted=datetime.strptime(re.search(date_pattern,sold_date).group(),format_date)
        price = residential_item.find('span', {'class':'property-price'}).text.strip()
        if 'Contact Agent' in price:
            price = None
        else:
            price=int(price)
        num_bedrooms = int(residential_item.find_all('div', {'class':'View__PropertyDetail-sc-11ysrk6-0 eSRWKr'})[0].find('p').text.strip())
        num_bathrooms = int(residential_item.find_all('div', {'class':'View__PropertyDetail-sc-11ysrk6-0 eSRWKr'})[1].find('p').text.strip())
        type = residential_item.find('span', {'class':'residential-card__property-type'}).text.strip()
        
        residential_data.append({
            'Address': address,
            'Sold on': sold_date_formatted,
            'Price': price,
            'Number of Bedrooms': num_bedrooms,
            'Number of Bathrooms': num_bathrooms,
            'Type': type
        })
    
    return residential_data

# Scrape data from the URL
residential_data = web_scraper(url)

# Create a DataFrame from the scraped data
df = pd.DataFrame(residential_data)

# Display the DataFrame
print(df)

# Set BigQuery project, dataset, and table details
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'
table_id = 'your-table-id'

# Function to push the DataFrame to BigQuery
def push_to_bigquery(df, project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Append the DataFrame to the BigQuery table
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    client.load_table_from_dataframe(df, table_ref, job_config=job_config).result()
    
# Push DataFrame to BigQuery
push_to_bigquery(df, project_id, dataset_id, table_id)