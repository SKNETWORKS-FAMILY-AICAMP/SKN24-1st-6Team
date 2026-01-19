import streamlit as st
import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'ohgiraffers',
    password = 'ohgiraffers',
    database = 'vehicledb'
)

st.title("FAQ ⁉️ ")

############ 1. company name 필터링 ##################
# 1. 자동차 제조사 목록
cursor = connection.cursor() 
company_list_sql = "SELECT DISTINCT f.company_id, v.company_name FROM faq_category AS f INNER JOIN vehicle_company AS v ON f.company_id = v.company_id;" 
cursor.execute(company_list_sql)

vehicle_company_res = cursor.fetchall()

company_id_map = {i: i + 1 for i in range(27)}

company_list = {}
for i, row in enumerate(vehicle_company_res):
    company_id = row[0]
    name = row[1]
    company_list[i] = name


selection = st.pills(
    "자동차 제조사 선택",
    options=company_list.keys(),
    format_func=lambda option: company_list[option],
    selection_mode="single",
)
if selection is not None:
    company_id = company_id_map[selection]
    
    # 2. SQL: category list
    faq_cat_list_sql = "SELECT faq_cat_id, faq_cat_name, company_id FROM faq_category WHERE company_id = %s" 
    companyArgValue = company_id,
    cursor.execute(faq_cat_list_sql, companyArgValue)

faq_cat_res = cursor.fetchall()

############ 2. category 필터링 ##################
category_id_map = {i: i + 1 for i in range(27)}

category_list = {}
for i, row in enumerate(faq_cat_res):
    cat_id = row[0]
    name = row[1]
    category_list[i] = name
print("category_list!",category_list)


selection = st.pills(
    "",
    options=category_list.keys(),
    format_func=lambda option: category_list[option],
    selection_mode="single",
)
if selection is not None:
    print(selection)
    cat_id = faq_cat_res[selection][0] #cat id

    ############ 3. FAQ 목록 ##################
    faq_list_sql = "SELECT faq_id, faq_cat_id, question, answer FROM faq WHERE faq_cat_id = %s" 
    faqArgValue = cat_id,
    cursor.execute(faq_list_sql, faqArgValue)

    faq_list = cursor.fetchall()
    if not faq_list:
        st.write("해당 들록된 질문이 없습니다.")  
    else: 
        for _, _, question, answer in faq_list:
            with st.expander(f"{question}"):
                st.write(answer)



cursor.close()
connection.close()