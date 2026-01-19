import pandas as pd
from pathlib import Path

base_dir = Path.cwd()
xlsx_path = base_dir / "월별 등록 현황" / "자동차등록현황보고_자동차등록대수현황 시도별 (201101 ~ 202512).xlsx"


# 위에가 두줄로 되어 있는 header 이므로 5번째, 6번째 줄을 header 로 잡음
df = pd.read_excel(xlsx_path, header=[4, 5], engine="openpyxl")


# 1) id 컬럼(멀티인덱스 튜플 그대로)

id_cols = [
    ("월(Monthly)", "월(Monthly)"),
    ("시도명", "시도명"),
    ("시군구", "시군구"),
]

# 2) id를 인덱스로 두고, 나머지 멀티 컬럼을 아래로 내림
long_df = (
    df.set_index(id_cols)
      .stack(level=[0, 1])       
      .reset_index()
)

# 3) 컬럼명 정리
long_df.columns = ["reg_date", "city", "district", "vehicle_type", "reg_type", "reg_count"]

# 4) 타입 정리 -> 날짜 = 연월 ,  숫자 = , 없애기 
long_df["reg_date"] = pd.to_datetime(long_df["reg_date"], format="%Y-%m").dt.date

long_df["reg_count"] = pd.to_numeric(
    long_df["reg_count"].astype(str).str.replace(",", "", regex=False),
    errors="coerce"
)

long_df = long_df[long_df["reg_type"] != "계"] # 합계 칼럼 없애기
long_df = long_df[long_df["vehicle_type"] != "총계"] # 총계도 있었네
long_df = long_df[long_df["district"] != "계"] # 시군구에도 계가 있네

#  확인용
print(long_df.head())
print(long_df[["vehicle_type", "reg_type"]].drop_duplicates().head(20))

dup = long_df.duplicated(
    subset=["reg_date", "city", "district", "vehicle_type", "reg_type"]
).sum()
print("duplicate rows by key:", dup)



from sqlalchemy import create_engine

# 본인이 쓰는 계정 정보 (꼭 바꿔서 입력해 주세요.!!) --------------------------------------------------------------------
user = "ohgiraffers"
pw = "ohgiraffers"
host = "localhost"      
port = 3306
db = "vehicledb"
# --------------------------------------------------------------------------------------------------------------------
engine = create_engine(
    f"mysql+pymysql://{user}:{pw}@{host}:{port}/{db}?charset=utf8mb4"
)

# 데이터 넣기

to_insert = long_df[[
    "reg_date", "city", "district", "vehicle_type", "reg_type", "reg_count"
]]

to_insert.to_sql(
    name="total_registered_vehicle",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000,
    method="multi"
)

# 테이블 확인
from sqlalchemy import text

with engine.connect() as conn:
    n = conn.execute(text("SELECT COUNT(*) FROM total_registered_vehicle")).scalar()
    print("rows in table:", n)

    sample = conn.execute(text("""
        SELECT reg_date, city, district, vehicle_type, reg_type, reg_count
        FROM total_registered_vehicle
        ORDER BY reg_date DESC
        LIMIT 5
    """)).fetchall()

    print(sample)

