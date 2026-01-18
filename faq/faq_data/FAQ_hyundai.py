from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 현대자동차: 대중적인 승용차 및 SUV 라인업.

vehicle_FAQ_group = '현대자동차 FAQ'

path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)


url = 'https://www.hyundai.com/kr/ko/e/customer/center/faq'
driver.get(url)
time.sleep(5)

faq_PK = []
company = []
category = []
question = []
answer = []

#------------------------------ FAQ 카테고리 갯수 확인--------------------------------------#
num_categorys = len(driver.find_elements(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li'))
print(num_categorys)
#-----------------------------------------------------------------------------------------#

#---------------------- FAQ text 추출 (회사, 질문, 답변, 카테고리, 인덱스-----------------#
faq_number = 0

for category_idx in range(1,num_categorys+1):
    category_btn = driver.find_element(By.XPATH,f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[{category_idx}]/button')
    driver.execute_script("arguments[0].click();", category_btn)
    time.sleep(4)
    print(category_idx)

    page = 1

    while True:
        print(f'FAQ {page} 질문')
        faq_elem = driver.find_elements(By.XPATH,'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div')
    # FAQ content 

        for idx in range(1,len(faq_elem)+1):
            # mysql column name : FAQ code (PK)
            faq_number +=1
            print(f'FAQ code : {faq_number}\n')
            faq_PK.append(faq_number)
            
            # comapany : 현대
            print('브랜드 명 : 현대','\n')
            company.append(f'현대')

            # category : 카테고리명
            category_title = driver.find_element(By.XPATH, f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{idx}]/button/div/span[1]')
            print(f'카테고리 : {category_title.text}\n')
            category_title = category_title.text
            category.append(category_title)
            
            # question_title : 자주 묻는 질문
            question_title = driver.find_element(By.XPATH, f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{idx}]/button/div/span[2]')
            print(f'질문 : {question_title.text}\n')
            question_title = question_title.text
            question.append(question_title)

            # question_answer : 대답
            question_click = driver.find_element(By.XPATH, f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{idx}]/button')
            driver.execute_script("arguments[0].click();", question_click)
            time.sleep(0.5)  # 클릭 후 잠깐 기다리기

            # 답변 가져오기
            xpaths = [
                f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{idx}]/div/div',
                f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{idx}]/div/div/div',
                f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[1]/div/div']

            answer_text = ''  # 기본값
            for xp in xpaths:
                elems = driver.find_elements(By.XPATH, xp)
                if elems:
                    answer_text = elems[0].text
                    break  # 텍스트를 찾으면 반복 종료

            print(f'대답 : {answer_text}\n')
            time.sleep(2)
            answer.append(answer_text)

        try:
            next_btn = driver.find_element(
                By.XPATH,
                     f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/div/ul//button[not(@disabled) and text()={page+1}]'
            )
            driver.execute_script("arguments[0].click();", next_btn)
            page += 1
            time.sleep(2)
            
            next_btn2 = driver.find_element(By.CLASS_NAME,'list-category').text
            if next_btn2=='차량정비':
                next_btn = driver.find_element(
                    By.XPATH,
                        f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/div/ul//button[not(@disabled) and text()={page+1}]'
                )
                driver.execute_script("arguments[0].click();", next_btn)
                page += 1

        except:
            print("✅ 마지막 페이지")
            break
#----------------------------------------------------------------------#

#-----------------------크롤링 추출 결과 저장------------------------------#

data = {'faq_PK': faq_PK,   
        'company': company,   
        'category': category,
        'question':question,
        'answer': answer}   
df = pd.DataFrame(data)   


# FAQ 현대 저장  
df.to_csv('hd_faq.csv', index=False, encoding='utf-8') 
#----------------------------------------------------------------------#
   
