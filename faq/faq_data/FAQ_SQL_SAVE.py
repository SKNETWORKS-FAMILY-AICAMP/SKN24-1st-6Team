import mysql.connector
import pandas as pd

hyundai_faq = pd.read_csv('hd_faq.csv',encoding='utf-8')
kia_faq = pd.read_csv('kia_faq.csv', encoding='utf-8')

### crawling 불가 데이터 따로 기입 (3개 row)
hyundai_faq.loc[70,'answer']='변경을 원하시면 기존 가입하신 상품 취소 후 변경 상품으로 재 가입하시면 됩니다.(단, 출고일 포함 30일 이내에만 재가입 가능합니다.)'
hyundai_faq.loc[81,'answer']='모젠고객센터(080-600-6000)로 문의 주시거나 1:1상담 문의에 올려주시면 신속하게 지원해 드리겠습니다.'
hyundai_faq.loc[157,'answer']='블루링크를 가입하시면 차량 원격제어, 안전보안, 차량관리, 길 안내 서비스를 제공받으실 수 있습니다. 블루링크 자세한 서비스 안내는 아래 페이지를 참고해주세요. 블루링크 서비스 안내 ▶바로가기'
print('na값이 있나 확인해보자 :    ',hyundai_faq[hyundai_faq['answer'].isnull()].index)

# 크롤링 시 특수 문자 제거 된 것을 저장 ("[현대]" --> "현대")
hyundai_faq['category'] = hyundai_faq['category'].str.replace('[', '').str.replace(']', '')
hyundai_faq.to_csv('hd_faq.csv', index=False, encoding='utf-8') 


faq_name_hd = '현대'
faq_name_kia = '기아'

print(hyundai_faq[hyundai_faq.isna().any(axis=1)])
print(kia_faq[kia_faq.isna().any(axis=1)])

# -------------SQL 연결-----------------#
connection = mysql.connector.connect(
    host = 'localhost', # MySQL 서버 주소(iP)
    user = 'ohgiraffers', # 사용자 이름
    password = 'ohgiraffers', # 비밀번호
    database = 'vehicledb' #사용할 DB 스키마
)
cursor = connection.cursor()
# -------------------------------------#

# -------------MYSQL에 저장된 company_id(FK) 가져오기---------------#
cursor.execute("SELECT company_id FROM vehicle_company WHERE company_name=%s", (faq_name_hd,))
company_id_hd = cursor.fetchone()[0] # 현대 id반환
print(company_id_hd)

cursor.execute("SELECT company_id FROM vehicle_company WHERE company_name=%s", (faq_name_kia,))
company_id_kia = cursor.fetchone()[0] # 기아 id반환
print(company_id_kia)
# ----------------------------------------------#

# -------------category 키를 만들기 위한 (중복제거)---------------#
hyd_faq_category_id = pd.DataFrame(hyundai_faq['category'].drop_duplicates().reset_index(drop=True))
print(hyd_faq_category_id)

kia_faq_category_id = pd.DataFrame(kia_faq['category'].drop_duplicates().reset_index(drop=True))
print(kia_faq_category_id)
# -------------------------------------------------------------#

# ------------faq_category table --> insert company_id, faq_category_name-------------------------#

for idx in hyd_faq_category_id.index:  #sql query & values
    category_value = hyd_faq_category_id.iloc[idx,0]
    cursor.execute(
        'INSERT INTO faq_category(faq_cat_name, company_id) values(%s,%s)'
    , (category_value, company_id_hd))

for idx in kia_faq_category_id.index:  #sql query & values
    category_value = kia_faq_category_id.iloc[idx,0]
    cursor.execute(
        'INSERT INTO faq_category(faq_cat_name, company_id) values(%s,%s)'
    , (category_value, company_id_kia))
# ------------------------------------------------------------------------#


# ------------faq table --> insert category_id, question, answer INSERT-------------------------#

# 현대 카테고리 ID 가져오기
cursor.execute(
    "SELECT faq_cat_id, faq_cat_name FROM faq_category WHERE company_id=%s",
    (company_id_hd,)
)
hd_cat_map = {name: cid for cid, name in cursor.fetchall()}  # {'차량구매': 1, '서비스': 2, ...}
print(hd_cat_map)
# 기아 카테고리 ID 가져오기
cursor.execute(
    "SELECT faq_cat_id, faq_cat_name FROM faq_category WHERE company_id=%s",
    (company_id_kia,)
)
kia_cat_map = {name: cid for cid, name in cursor.fetchall()}


# 카테고리 이름으로 이미 DB에 있는 ID를 가져옴
for idx in hyundai_faq.index:
    faq_cat_id = hd_cat_map[hyundai_faq['category'][idx]]
    cursor.execute(
        "INSERT INTO faq(faq_cat_id, question, answer) VALUES (%s, %s, %s)",
        (faq_cat_id, hyundai_faq['question'][idx], hyundai_faq['answer'][idx])
    )

# 기아 FAQ insert
for idx in kia_faq.index:
    faq_cat_id = kia_cat_map[kia_faq['category'][idx]]
    cursor.execute(
        "INSERT INTO faq(faq_cat_id, question, answer) VALUES (%s, %s, %s)",
        (faq_cat_id, kia_faq['question'][idx], kia_faq['answer'][idx])
    )
# ----------------------------------------------------------------------------------------#

    
connection.commit()
cursor.close()

