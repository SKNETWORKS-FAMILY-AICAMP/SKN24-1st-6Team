from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

path = "chromedriver.exe"
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)
# 스크랩 순서
# 필요한 정보 값 : 제조사 / 모델명 / 판매년 / 월 / 판매량

brand_id = ('303', '307', '304', '312', '326', '321', '328', '338', '634', '334', '329', '333', '632', '337', '318', '633', '315', '319', '331', '362', '349', '371', '611', '546', '445', '380', '617', '612', '459', '376', '491', '486', '573', '602', '408', '614', '468', '458', '381', '569', '500', '390', '385', '404', '409', '630', '587', '367', '399', '413', '436', '440', '537', '616', '556', '615', '622', '394', '422', '618')
month = ('2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01', '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01')

# 2. 제조사, 모델명, 판매년월(month_id 이용), 판매량
# 크롤링 함수 정의

def data_scrap_brd(brd_now):
    try: 
        select_brand = f'li[data-brand="{brd_now}"] > button > span'
        brand_name_elems = driver.find_element(By.CSS_SELECTOR, select_brand)
        # print(brand_name_elems.text)
        name_brd = brand_name_elems.text.strip()
        print(f'{name_brd}를 수집하고 있습니다.')
        return name_brd
    
    except Exception as e:
        print(f'실패!:{e}')

def data_scrap_model(brand_name, csv_writer):
    rows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')

    for row in rows:
        title_x = row.find_elements(By.CSS_SELECTOR, 'td.title > a')
        if not title_x:
            continue
        try:
            car_name = title_x[0].text.strip()
            # print(car_name)
            # 그래프 클릭
            row.find_element(By.CLASS_NAME, 'viewGraph').click()
            time.sleep(1)

            # 그래프 팝업 값 찾기
            popup = driver.find_element(By.ID, 'autodanawa_popup')
            graph_popup = popup.find_elements(By.CSS_SELECTOR, 'table.recordMonth > tbody > tr > td')[2:]
            # for data_graph in graph_popup:
            #     print(data_graph.text)
            
            for monthly, data_graph in zip(month, graph_popup):
                sales_value = data_graph.text.strip().replace('-','0')
                sales_int = sales_value.replace(',','')

                result = [brand_name, car_name, monthly, sales_int]
                print(result)
                csv_writer.writerow(result)

            # 그래프 닫기
            popup.find_element(By.CSS_SELECTOR, 'div > button').click()
            time.sleep(2)
        except Exception as e: 
            print(f'실패!: {e}')


# 1. 페이지 접속(브랜드명 변수로 지정 > 수집 다 하면 바뀔 수 있도록)
# 3. 1부터 브랜드명만 바꿔서 다시 시작 총 60개
# 4. csv 저장

with open('vehicle_sales_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['제조사', '모델명', '연월', '판매량'])

    for brand in brand_id:
        url = f'https://auto.danawa.com/newcar/?Work=record&Tab=Grand&Brand={brand}&Month=2025-12-00&MonthTo='
        driver.get(url)
        time.sleep(2)
        brand_name_now = data_scrap_brd(brand)          # 제조사명 불러오기
        data_scrap_model(brand_name_now, writer)        # 전체 값 불러오기


driver.quit()