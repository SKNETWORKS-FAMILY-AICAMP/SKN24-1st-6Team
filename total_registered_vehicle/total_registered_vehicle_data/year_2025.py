from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlretrieve
import time
from datetime import datetime

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=1244&hDivEng=&month_yn="
driver.get(url)
time.sleep(1)


### ['승용', '승합', '화물']
car_class_row = driver.find_element(By.XPATH, "//*[@id='sheet01-table']/tbody/tr[1]/td[2]/div/table/tbody/tr[2]")
car_class_list = str(car_class_row.text.split())
# print(type(car_class_list))
# print((car_class_list))

### ['관용', '자가용', '영업용', '계', '관용', '자가용', '영업용', '계', '관용', '자가용', '영업용']
car_label_row = driver.find_element(By.XPATH, "//*[@id='sheet01-table']/tbody/tr[1]/td[2]/div/table/tbody/tr[3]")
car_label_list = str(car_label_row.text.split())
# print(type(car_class_list))
print((car_label_list))


### ['37,360', '20,632,170', '1,369,073', '22,038,603', '24,299', '495,490', '114,035', '633,824', '35,925', '3,187,069', '472,238']
rowTds = driver.find_elements(By.CSS_SELECTOR, ".GMDataRow.GMClassFocused")
result_year = rowTds[0].text
# print(result_year)
values_list = str(rowTds[1].text).split()
# print(values_list)
# print(type(values_list))


# time.sleep(4)



driver.quit()
