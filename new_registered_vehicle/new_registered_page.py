import mysql.connector
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng

connection = mysql.connector.connect(
    host = 'localhost',                     # MySQL 서버 주소 (ip)
    user = 'root',                          # 사용자 이름
    password = 'admin1234',                 # 비밀번호
    database = 'db_new_registered_vehicle'  # 사용할 DB 스키마
)

cursor = connection.cursor()                # 커서 호출

st.title("자동차 신규등록 현황 조회")
st.write('2025년에 새로 등록된 차량의 수를 조회합니다.')
st.divider()


col1, col2, col3 = st.columns(3)

with col1:
    age_range = st.selectbox(
        "연령대를 선택하세요.",
        ("10대", "20대", "30대", "40대", "50대", "60대", "70대", "80대"),
    )
    st.write("선택한 연령대 :", age_range)

with col2:
    gender = st.selectbox(
        "성별을 선택하세요.",
        ("전체", "남자", "여자"),
    )
    st.write("선택한 성별 :", gender)

with col3:
    fuel_type = st.selectbox(
        "사용연료를 선택하세요.",
        ("전체", "경유", "수소", "전기", "하이브리드(휘발유+전기)", "휘발유"),
    )
    st.write("선택한 사용연료 :", fuel_type)
st.divider()

# ---------------------------------------------------------------------------




if st.button('조회하기', width = 1000):
    st.divider()

    age_range_where = ''
    gender_select = ''
    gender_where = ''
    fuel_type_select = ''
    fuel_type_where = ''

    if age_range == '10대':
        age_range_where = 'age_range = 10'
    elif age_range == '20대':
        age_range_where = 'age_range = 20'
    elif age_range == '30대':
        age_range_where = 'age_range = 30'
    elif age_range == '40대':
        age_range_where = 'age_range = 40'
    elif age_range == '50대':
        age_range_where = 'age_range = 50'
    elif age_range == '60대':
        age_range_where = 'age_range = 60'
    elif age_range == '70대':
        age_range_where = 'age_range = 70'
    elif age_range == '80대':
        age_range_where = 'age_range = 80'

    if gender == '전체':
        gender_select = ''
        gender_where = ''
    elif gender == '남자':
        gender_select = ', gender'
        gender_where = ' and gender = "M"'
    elif gender == '여자':
        gender_select = ', gender'
        gender_where = ' and gender = "F"'

    if fuel_type == '전체':
        fuel_type_select = ''
        fuel_type_where = ''
    elif fuel_type == '경유':
        fuel_type_select = ', fuel_type'
        fuel_type_where = ' and fuel_type = "경유"'
    elif fuel_type == '수소':
        fuel_type_select = ', fuel_type'
        fuel_type_where = ' and fuel_type = "수소"'
    elif fuel_type == '전기':
        fuel_type_select = ', fuel_type'
        fuel_type_where = ' and fuel_type = "전기"'
    elif fuel_type == '하이브리드(휘발유+전기)':
        fuel_type_select = ', fuel_type'
        fuel_type_where = ' and fuel_type = "하이브리드"'
    elif fuel_type == '휘발유':
        fuel_type_select = ', fuel_type'
        fuel_type_where = ' and fuel_type = "휘발유"'

    sql = f'SELECT new_reg_date, age_range' + gender_select + fuel_type_select + ', sum(new_reg_count) FROM new_registered_vehicle WHERE ' + age_range_where + gender_where + fuel_type_where + ' GROUP BY new_reg_date'

    cursor.execute(sql)          # 커서가 쿼리문 수행

    result_rows = cursor.fetchall()        # 커서가 수행한 내용을 가져와 변수 result_rows에 저장
    new_reg_count_list = []                # 결과 값인 new_reg_count를 담을 list 초기화
    for row in result_rows:
        new_reg_count_list.append(int(row[-1]))
        print(type(row[-1]))

    connection.commit()                  # 커밋 수행

    data = pd.DataFrame({
        '연월' : ['25_01', '25_02', '25_03', '25_04', '25_05', '25_06', '25_07', '25_08', '25_09', '25_10', '25_11', '25_12'],
        '신규등록 수 (대)' : new_reg_count_list
    })
    st.line_chart(data.set_index('연월')['신규등록 수 (대)'], x_label='연월', y_label='신규등록 수 (대)')

cursor.close()
connection.close()
