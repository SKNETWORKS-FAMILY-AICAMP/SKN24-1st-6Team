import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text

st.set_page_config(page_title="자동차 등록현황", layout="wide")
st.title("자동차 등록현황 (월별 합계)")

# DB 연결
host = os.getenv("DB_HOST", "127.0.0.1")
port = os.getenv("DB_PORT", "3306")
user = os.getenv("DB_USER", "project1")
pwd  = os.getenv("DB_PASS", "qwe123")
db   = os.getenv("DB_NAME", "vehicledb")

engine = create_engine(
    f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}?charset=utf8mb4"
)

# 날짜 범위

minmax = pd.read_sql(
    "SELECT MIN(reg_date) AS min_d, MAX(reg_date) AS max_d FROM total_registered_vehicle",
    engine
)


min_d = pd.to_datetime(minmax.loc[0, "min_d"]).date()
max_d = pd.to_datetime(minmax.loc[0, "max_d"]).date()

# 필터 옵션 로딩

cities = ["(전체)"] + pd.read_sql(
    "SELECT DISTINCT city FROM total_registered_vehicle ORDER BY city",
    engine
)["city"].tolist()

vehicle_types = ["(전체)"] + pd.read_sql(
    "SELECT DISTINCT vehicle_type FROM total_registered_vehicle ORDER BY vehicle_type",
    engine
)["vehicle_type"].tolist()

reg_types = ["(전체)"] + pd.read_sql(
    "SELECT DISTINCT reg_type FROM total_registered_vehicle ORDER BY reg_type",
    engine
)["reg_type"].tolist()

# --------------------
# UI
# --------------------
left, right = st.columns([2, 1])

with right:
    grain = st.selectbox("집계 단위", ["월", "년"])
    city = st.selectbox("시도", cities)

    if city == "(전체)":
        districts = ["(전체)"]
    else:
        districts = ["(전체)"] + pd.read_sql(
            f"""
            SELECT DISTINCT district
            FROM total_registered_vehicle
            WHERE city = '{city}'
            ORDER BY district
            """,
            engine
        )["district"].tolist()

    district = st.selectbox("시군구", districts)
    vehicle_type = st.selectbox("차종", vehicle_types)
    reg_type = st.selectbox("구분", reg_types)

with left:
    c1, c2 = st.columns(2)
    with c1:
        start = st.date_input("시작일", min_d, min_value=min_d, max_value=max_d)
    with c2:
        end = st.date_input("종료일", max_d, min_value=min_d, max_value=max_d)

if start > end:
    st.error("시작일이 종료일보다 클 수 없습니다.")
    st.stop()


 ## %Y-%M 쓰면 자꾸 에러남

if grain == "년":
    period_expr = "LEFT(reg_date, 4)"      # 'YYYY'
else:
    period_expr = "LEFT(reg_date, 7)"      # 'YYYY-MM'

where = [
    f"reg_date BETWEEN '{start}' AND '{end}'"
]

if city != "(전체)":
    where.append(f"city = '{city}'")
if district != "(전체)":
    where.append(f"district = '{district}'")
if vehicle_type != "(전체)":
    where.append(f"vehicle_type = '{vehicle_type}'")
if reg_type != "(전체)":
    where.append(f"reg_type = '{reg_type}'")

query = f"""
SELECT {period_expr} AS period, SUM(reg_count) AS total
FROM total_registered_vehicle
WHERE {" AND ".join(where)}
GROUP BY period
ORDER BY period
"""

df = pd.read_sql(query, engine)

# --------------------
# 날짜 변환 (pandas에서 처리)
# --------------------
if df.empty:
    st.info("조건에 해당하는 데이터가 없어.")
    st.stop()

if grain == "년":
    df["period"] = pd.to_datetime(df["period"] + "-01-01")
else:
    df["period"] = pd.to_datetime(df["period"] + "-01")

# --------------------
# KPI
# --------------------
st.divider()

k1, k2, k3 = st.columns(3)

df = df.sort_values("period")  # 안전하게 정렬

first_val = int(df.iloc[0]["total"])
last_val  = int(df.iloc[-1]["total"])
change    = last_val - first_val
pct       = (last_val / first_val - 1) * 100 if first_val != 0 else 0

k1.metric("마지막 기간 등록대수", f"{last_val:,}")
k2.metric("기간 변화량", f"{change:+,}")
k3.metric("기간 변화율", f"{pct:.2f}%")

# --------------------
# 차트 + 테이블
# --------------------
st.subheader("기간별 추이")

y_min = df["total"].min()
y_max = df["total"].max()
margin = (y_max - y_min) * 0.05
y_min -= margin
y_max += margin

import altair as alt

chart = (
    alt.Chart(df)
    .mark_line()
    .encode(
        x=alt.X("period:T", title="기간"),
        y=alt.Y(
            "total:Q",
            title="등록대수",
            scale=alt.Scale(domain=[y_min, y_max])
        )
    )
)

st.altair_chart(chart, use_container_width=True)


if st.checkbox("집계표 보기"):
    st.dataframe(df, use_container_width=True, hide_index=True)