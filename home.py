import streamlit as st

def homepage():
    st.title("CARPORT")

    # 필터링 
    col1, col2, col3 = st.columns(3)

    with col1:
        age_range = st.selectbox(
            "연령대 선택해주세요.",
            ("10대", "20대", "30대"),
        )
        st.write("선택한 연령대:", age_range)

    with col2:
        genre = st.radio(
            "사용연료",
            ["경유", "수소"],
            index=None,
        )
        st.write("You selected:", genre)

    with col3:
        gender_options = {
        0: "여자",
        1: "남자"
        }
        selection = st.pills(
            "성별",
            options=gender_options.keys(),
            format_func=lambda option: gender_options[option],
            selection_mode="single",
        )
        st.write(
            "성별 선택: "
            f"{None if selection is None else gender_options[selection]}"
        )



# 페이지 타이틀, 페이지 경로 설정
home = st.Page(homepage, title="Home", icon=":material/home:")
total_registered_vehicle_page = st.Page("total_registered_vehicle/total_registered_page.py", title="국내 자옫차등록현황은 어떨까?", icon=":material/description:")
popular_vehicle_page = st.Page("vehicle_sales/vehicle_sales_page.py", title="핫한 모델 및 브랜드 보기!", icon=":material/description:")
new_registered_vehicle_page = st.Page("new_registered_vehicle/new_registered_page.py", title="20, 30, 40대는 차를 몇대샀을까유?", icon=":material/description:")
faq_page = st.Page("faq/faq_page.py", title="모든답을 여기 FAQ에서 찾기!", icon=":material/description:")

# 사이드바 내비게이션
pg = st.navigation([home, total_registered_vehicle_page, popular_vehicle_page, new_registered_vehicle_page, faq_page])

pg.run()




