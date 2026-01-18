import pandas as pd
import streamlit as st
import mysql.connector
from numpy.random import default_rng as rng

@st.cache_data

def load_vehicle_data():
    # MySQL 연결
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'ohgiraffers',
        password = 'ohgiraffers',
        database = 'vehicledb'
    )
    if connection.is_connected():
        print('MySQL 서버 연결 성공!')
    
    # MySQL DB 삽입
    query = '''
        SELECT vc.company_name, vs.sales_model, vs.sales_date, vs.sales_count
        FROM vehicle_sales as vs
        INNER JOIN vehicle_company vc on vs.company_id = vc.company_id;
    '''
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# MySQL 연결
sales_df = load_vehicle_data()

# 페이지 구성
st.header('📊 2025 자동차 판매량 조회')
st.info(f'2025년에 판매된 {int(len(sales_df) / 12)}개의 차량의 판매량 정보를 제공합니다.')
st.subheader('✔️ 원하는 제조사명을 선택하세요!')
# 제조사명
cpy_list = sorted(sales_df['company_name'].dropna().unique())
# 컬럼 구성
col1, col2 = st.columns(2)
with col1:
        cpy_range = st.selectbox(                                                  # 제조사 선택
            "**제조사 선택**",
            cpy_list,
            placeholder='선택하기...'
        )
        model_cpy, select_cpy = [], None
        if cpy_range and cpy_range != '':
             model_df = sales_df[sales_df['company_name'] == cpy_range]
             model_list = sorted(model_df['sales_model'].dropna().unique())        # 제조사/모델 선택 연동
             if model_list:
                  select_cpy = st.selectbox('**모델 선택**', model_list, placeholder='선택하기...')

# 전월 실적 비교
with col2:
    selected_model_df = model_df[model_df['sales_model'] == select_cpy].sort_values(by='sales_date', ascending = False)
    if not selected_model_df.empty:
         latest_row = selected_model_df.iloc[0]
         latest_sales = latest_row['sales_count']
         latest_date = latest_row['sales_date'].strftime('%y-%m')
        
         delta_val = None
         if len(selected_model_df) >= 2:
              prev_sales = selected_model_df.iloc[1]['sales_count']
              delta_val = int(latest_sales - prev_sales)
         st.space(size='small')
         st.metric(
              label=f'{select_cpy} 판매량 ({latest_date})',
              value=f'{int(latest_sales):,} 대',
              delta=f'{delta_val:,} 대' if delta_val is not None else "과거 데이터가 없음", border=True)

    else:
         st.write('해당 모델의 판매 데이터 부족')

# 상세 차트
st.subheader('✔️ 자세한 차트 보기')

sales_data = selected_model_df.head(12).sort_values(by='sales_date')
if not sales_data.empty:
     st.markdown(f'##### - {select_cpy} 최근 1년 판매량')
     
     chart_df = sales_data[['sales_date', 'sales_count']].set_index('sales_date')
     st.line_chart(chart_df)
else:
     st.info('차트 표시 데이터 부족')