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

### 1. 사이트 접근 
url = "https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=5498&hDivEng=&month_yn="
driver.get(url)
time.sleep(1)

### 2. 날짜 시작 선택 버튼
start_btn = driver.find_element(By.XPATH, "//*[@id='sStart']")
start_btn.click()
time.sleep(1)

start_options = driver.find_elements(By.XPATH, "//*[@id='sStart']/option")

for idx, option in enumerate(start_options):
    if option.text == "202501":
        option.click()


### 2. 날짜 끝 선택 버튼
end_btn = driver.find_element(By.XPATH, "//*[@id='sEnd']")
start_btn.click()
time.sleep(1)

end_options = driver.find_elements(By.XPATH, "//*[@id='sEnd']/option")

for idx, option in enumerate(end_options):
    if option.text == "202512":
        option.click()

### 3. 조회하기
search_btn = driver.find_element(By.CSS_SELECTOR, ".mu-btn.mu-btn-secondary")
if search_btn.text == "조회":
    search_btn.click()


### 4. 2025년 월 돌리기 하는중
time.sleep(2)
january = driver.find_element(By.XPATH, "//*[@id='sheet01-table']/tbody/tr[2]/td[1]/div/div[1]/table/tbody/tr[2]/td[2]")
time.sleep(2)
december = driver.find_element(By.XPATH, "//*[@id='sheet01-table']/tbody/tr[2]/td[1]/div/div[12]/table/tbody/tr[2]/td[2]")
print((january.text))
print((december.text))

#202501 
# <td style="background-color: rgb(255, 255, 254);" class=" GMClassReadOnly GMClassFocusedCell GMWrap0 GMText GMCell IBSheetFont0 HideCol0C1" rowspan="272" colspan="2">2025-01</td>
# //*[@id="sheet01-table"]/tbody/tr[2]/td[1]/div/div[1]/table/tbody/tr[2]/td[2]

#202502
# <td style="background-color:rgb(201,225,245);" class=" GMClassReadOnly GMWrap0 GMText GMCell IBSheetFont0 HideCol0C1" rowspan="272" colspan="2">2025-02</td>
# //*[@id="sheet01-table"]/tbody/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]

#202512
# //*[@id="sheet01-table"]/tbody/tr[2]/td[1]/div/div[12]/table/tbody/tr[2]/td[2]


time.sleep(2)

driver.quit()
