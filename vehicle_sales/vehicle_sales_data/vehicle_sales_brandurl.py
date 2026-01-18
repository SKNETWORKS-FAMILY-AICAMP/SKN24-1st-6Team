from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

path = "chromedriver.exe"
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

url = "https://auto.danawa.com/newcar/?Work=record&Tab=Grand&Month=2025-01-00"
driver.get(url)
time.sleep(1)

def company_tag():
    company_brand_elems = driver.find_elements(By.CSS_SELECTOR, 'li[data-brand]')

    company_url = []
    for name in company_brand_elems:
        company_data = name.get_attribute('data-brand')
        company_url.append(company_data)

    print(company_url)
    print(len(company_url))

company_tag()

driver.quit()