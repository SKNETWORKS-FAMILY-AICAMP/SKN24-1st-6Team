from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

### 0. 다운로드 파일 경로 설정
base_dir = os.getcwd() # 현재 디렉토리 가져오기
data_dir = os.path.join(base_dir, "월별 등록 현황") # 현재 폴더/"새로운 폴더 이름"

if not os.path.exists(data_dir): # 폴더가 없으면 새로 만들기
    os.makedirs(data_dir)

# 크롬 설정하기
prefs = {
    "download.default_directory": data_dir, # data_dir 경로
    "download.prompt_for_download": False,  # 물어보지 말고 바로 저장
    "directory_upgrade": True, #경로 설정 최신화 
}

# 옵션 활성화
chrome_options = Options()
chrome_options.add_experimental_option("prefs", prefs)

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

### 1. 사이트 접근 
url = "https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=5498&hDivEng=&month_yn="
driver.get(url)
time.sleep(5)

year = input("연도를 입력하세요") # 연도 추가 수집 가능
target_start_month =year + "01" # 날짜 변경가능하게
target_end_month = year + "12"


### 2. 날짜 시작 선택 버튼
start_btn = driver.find_element(By.XPATH, "//*[@id='sStart']")
start_btn.click()
time.sleep(2)

start_options = driver.find_elements(By.XPATH, "//*[@id='sStart']/option")
for option in start_options:
    if option.text == target_start_month:
        option.click()
        break


### 2. 날짜 끝 선택 버튼
end_btn = driver.find_element(By.XPATH, "//*[@id='sEnd']")
end_btn.click()
time.sleep(1)

end_options = driver.find_elements(By.XPATH, "//*[@id='sEnd']/option")


for option in end_options:
    if option.text == target_end_month:
        option.click()
        break

### 3. 조회하기
search_btn = driver.find_element(By.CSS_SELECTOR, ".mu-btn.mu-btn-secondary")
if search_btn.text == "조회":
    search_btn.click()
time.sleep(3)

### 4. 엑셀 파일 다운로드
wait = WebDriverWait(driver, 30)
file_dl_btn=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fileDownBtn"]'))) # 엑셀 다운로드 버튼이 클릭 가능할 때까지 대기
file_dl_btn.click()
time.sleep(1)

xlsx_dl_btn = driver.find_element(By.XPATH, '//*[@id="file-download-modal"]/div[2]/div[3]/button')
xlsx_dl_btn.click()
time.sleep(5) #다운로드 시작하는데 시간 좀 걸림

driver.quit()