from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 기아: 현대차와 함께 시장을 주도하는 인기 브랜드.

vehicle_FAQ_group = '기아 FAQ'

path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

url = 'https://www.kia.com/kr/customer-service/center/faq'
driver.get(url)


# FAQ 테이블

faq_PK = []
company = []
category = []
question = []
answer = []

#------------------------------ FAQ 카테고리 갯수 확인--------------------------------------#
num_categorys = len(driver.find_elements(By.XPATH,'//*[@id="tab-list"]//button/span'))

print(num_categorys)
#-----------------------------------------------------------------------------------------#

#---------------------- FAQ text 추출 (회사, 질문, 답변, 카테고리, 인덱스-----------------#
faq_number = 0
for category_idx in range(3,num_categorys+1):
    category_btn = driver.find_element(By.XPATH,f'//*[@id="tab-list"]/li[{category_idx}]/button')
    driver.execute_script("arguments[0].click();", category_btn)
    time.sleep(10)
    # print(category_idx)

    category_title = driver.find_element(By.XPATH, f'//*[@id="tab-list"]/li[{category_idx}]/button/span')
    title = category_title.get_attribute("innerText").strip()
    print(f'category : {title}')

    page = 1


    while True:
        print(f'FAQ {page} 페이지')
    # FAQ content  
        content_elems = driver.find_elements(By.XPATH,'//button[contains(@class,"accordion")]')
        print(len(content_elems), '질문 갯수 \n ')

        for idx in range(len(content_elems)+1):
            # question : 질문 추출
            try:
                question_elem = driver.find_element(By.XPATH, f'//*[@id="accordion-item-{idx}-button"]')
                spans = question_elem.find_elements(By.TAG_NAME, 'span')
                question_text = ""
                for s in spans:
                    if s.text.strip():  # 텍스트가 있으면 그 span 사용
                        question_text = s.text.strip()
                        break
                if not question_text:  # 질문 없으면 skip
                    print("질문 없음, 건너뜀")
                    continue
            except:
                print("질문 요소 없음, 건너뜀")
                continue


            # question_answer : 대답
            question_click = driver.find_element(By.XPATH, f'//*[@id="accordion-item-{idx}-button"]')
            driver.execute_script("arguments[0].click();", question_click)
            time.sleep(3)  # 클릭 후 잠깐 기다리기

            # 답변 가져오기
            elems = driver.find_element(By.XPATH, f'//*[@id="accordion-item-{idx}-panel"]/div')
            elems = elems.get_attribute("innerText").strip()

            category.append(title)
            print('카테고리 이름 : ', title,'\n')
            print('인덱스', idx ,'\n')

            # mysql column name : FAQ code (PK)
            faq_number +=1
            print(f'FAQ code : {faq_number}\n')
            faq_PK.append(faq_number)
            
            # comapany : 기아
            print('브랜드 명 : 기아','\n')
            company.append(f'기아')

            print(f'질문 : {question_text}\n')
            question.append(question_text)

            print('대답 : ',elems)
            answer.append(elems)

        try:
            next_btn = driver.find_element(
                By.XPATH,
                     f'//*[@id="contents"]/div/div[3]/div/div/div[4]/div/ul/li[{page+1}]/a'
            )
            driver.execute_script("arguments[0].click();", next_btn)
            page += 1
            time.sleep(2)

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
df.to_csv('kia_faq.csv', index=False, encoding='utf-8') 
#----------------------------------------------------------------------#
    
