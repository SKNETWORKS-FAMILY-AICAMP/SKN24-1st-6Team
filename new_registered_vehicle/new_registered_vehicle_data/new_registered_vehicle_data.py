from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from urllib.parse import quote
import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',                # MySQL 서버 주소 (ip)
    user = 'root',              # 사용자 이름
    password = 'admin1234',          # 비밀번호
    database = 'db_new_registered_vehicle'  # 사용할 DB 스키마
)

cursor = connection.cursor()                # 커서 호출

# path = 'chromedriver.exe'
# service = webdriver.chrome.service.Service(path)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver_url = 'https://www.data.go.kr/data/15059401/openapi.do#/'
driver.get(driver_url)
time.sleep(0.2)

get_new_regist_btn = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[1]/button')
get_new_regist_btn.click()   # 신규등록 통계조회 버튼 클릭
time.sleep(0.2)

ready_to_run_btn = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[1]/div[2]/button')
ready_to_run_btn.click()     # OpenAPI 실행 준비 버튼 클릭
time.sleep(0.2)

input_key_box = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/input')
input_key_box.send_keys("9a51dbf6d06f8e6124a73e1fa6722367c46d8c2a9d726cb2c9ff3b68eba94069")      # 인증키 입력
time.sleep(0.2)

input_registYy_box = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/input')
input_registYy_box.send_keys("2025")      # 등록 연도 입력
time.sleep(0.2)

for var_rM in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
    input_registMt_box = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/input')
    input_registMt_box.clear()         # 기존 입력되있던 값 삭제
    input_registMt_box.send_keys(var_rM)      # 등록 월 입력
    time.sleep(0.5)

    for var_a in ['1', '2', '3', '4', '5', '6', '7', '8']:
        input_agrde_box = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[10]/td[2]/input')
        input_agrde_box.clear()         # 기존 입력되있던 값 삭제
        input_agrde_box.send_keys(var_a)          # 연령대 입력
        time.sleep(0.5)

        for var_s in ['남자', '여자']:
            input_sexdstn_box = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/input')
            input_sexdstn_box.clear()         # 기존 입력되있던 값 삭제
            input_sexdstn_box.send_keys(var_s)      # 성별 입력
            time.sleep(0.5)

            for var_uFC in ['2', '3', '5', '7', '8']:
                input_useFuelCode_box = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/input')
                input_useFuelCode_box.clear()         # 기존 입력되있던 값 삭제
                input_useFuelCode_box.send_keys(var_uFC)    # 사용연료 입력
                time.sleep(0.5)

                call_openapi_btn = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[3]/button')
                call_openapi_btn.click()     # OpenAPI 호출 버튼 클릭
                time.sleep(1)



                request_url = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[4]/div[2]/div/div/div[2]/div/pre').text

                # API 요청 -> 응답
                request = urllib.request.Request(request_url) # 요청할 객체 생성
                response = urllib.request.urlopen(request)

                # 응답받은 데이터 확인
                # print(response)                      # <http.client.HTTPResponse object at 0x00000197A28FA710>
                # print(response.getcode())            # 200 -> 요청 성공해서 응답받음

                response_body = response.read()      # 응답 내용(response body) 반환
                if response_body.decode('utf-8').split('<resultMsg>')[1].split('</resultMsg>')[0] == 'NODATA_ERROR':
                    new_reg_count = 0                   # 에러 코드가 NODATA_ERROR이면 결과 값에 0 저장
                else:
                    new_reg_count = int(response_body.decode('utf-8').split('<dtaCo>')[1].split('</dtaCo>')[0])
                                # str 형인 응답 내용에서 결과값만 int로 변환해 저장
                # print(new_reg_count)
                # print('------')

                sql = 'INSERT INTO new_registered_vehicle (new_reg_date, age_range, gender, fuel_type, new_reg_count) VALUES (%s, %s, %s, %s, %s);'

                if var_rM == '01':
                    new_reg_date = '25_01'
                elif var_rM == '02':
                    new_reg_date = '25_02'
                elif var_rM == '03':
                    new_reg_date = '25_03'
                elif var_rM == '04':
                    new_reg_date = '25_04'
                elif var_rM == '05':
                    new_reg_date = '25_05'
                elif var_rM == '06':
                    new_reg_date = '25_06'
                elif var_rM == '07':
                    new_reg_date = '25_07'
                elif var_rM == '08':
                    new_reg_date = '25_08'
                elif var_rM == '09':
                    new_reg_date = '25_09'
                elif var_rM == '10':
                    new_reg_date = '25_10'
                elif var_rM == '11':
                    new_reg_date = '25_11'
                elif var_rM == '12':
                    new_reg_date = '25_12'

                if var_a == '1':
                    age_range = 10
                elif var_a == '2':
                    age_range = 20
                elif var_a == '3':
                    age_range = 30
                elif var_a == '4':
                    age_range = 40
                elif var_a == '5':
                    age_range = 50
                elif var_a == '6':
                    age_range = 60
                elif var_a == '7':
                    age_range = 70
                elif var_a == '8':
                    age_range = 80
                
                if var_s == '남자':
                    gender = 'M'
                elif var_s == '여자':
                    gender = 'F'

                if var_uFC == '2':
                    fuel_type = '경유'
                elif var_uFC == '3':
                    fuel_type = '수소'
                elif var_uFC == '5':
                    fuel_type = '전기'
                elif var_uFC == '7':
                    fuel_type = '하이브리드'
                elif var_uFC == '8':
                    fuel_type = '휘발유'
                
                values = (new_reg_date, age_range, gender, fuel_type, new_reg_count)

                cursor.execute(sql, values)          # 커서가 쿼리문 수행
                connection.commit()                  # 커밋 수행

                call_openapi_btn = driver.find_element(By.XPATH, '//*[@id="operations-API_목록-getnewRegistlnfoService02"]/div[2]/div/div[3]/button[2]')
                call_openapi_btn.click()     # 취소 버튼 클릭
                time.sleep(0.5)

driver.quit()

cursor.close()
connection.close()
