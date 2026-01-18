import mysql.connector
import pandas as pd
import csv

file_path = 'final_vehicle_sales_data.csv'

# MySQL 연결
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'ohgiraffers',
    password = 'ohgiraffers',
    database = 'vehicledb'
)
cursor = connection.cursor()

if connection.is_connected():
    print('MySQL 서버 연결 성공!')

d = pd.read_csv(file_path)

# 별도 SQL 구문으로 처리하고자 주석 처리
# unique_cpy = d['제조사'].unique()
# sql_cpy = 'INSERT INTO vehicle_company(company_name) VALUES (%s)'# 
# for brd_name in unique_cpy:
#     try:
#          cursor.execute(sql_cpy, (brd_name,))
#          print(f'등록 완료: {brd_name}')
#     except mysql.connector.Error as err:
#          print(f'제조사 건너뛰기: {brd_name} | 이유: {err}')
# sql_cpy = 'INSERT INTO vehicle_sales(sales_date, company_id, sales_count, sales_model) VALUES (%s, %s, %s, %s)'

cursor.execute("SELECT company_id, company_name FROM vehicle_company")
cpy_map = {cpy_name: cpy_id for (cpy_id, cpy_name) in cursor.fetchall()}

sql_sales = 'INSERT INTO vehicle_sales(sales_date, company_id, sales_count, sales_model) VALUES (%s, %s, %s, %s)'

for index, row in d.iterrows():
    try:
        c_id = cpy_map[row['제조사']]
        
        val = (row['연월'], c_id, row['판매량'], row['모델명'])
        cursor.execute(sql_sales, val)
    except Exception as e:
        print(f'{index}행 입력 중 오류 발생: {e}')

connection.commit()
print("모든 데이터 저장")

cursor.close()
connection.close()