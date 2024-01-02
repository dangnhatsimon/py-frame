import requests
from bs4 import BeautifulSoup
import pandas
import time
from selenium import webdriver
#dynamic scraping using selenium and beautiful soup
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C:/SeleniumDrivers/chromedriver.exe", chrome_options=options)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.realestate.com.au/sold/in-pyrmont,+nsw+2009/list-1?activeSort=solddate&source=refinement")
src = driver.page_source
soup = BeautifulSoup(src, 'lxml')
print(soup.prettify())