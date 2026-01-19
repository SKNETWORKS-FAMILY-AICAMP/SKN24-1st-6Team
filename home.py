import streamlit as st

def homepage():
    # ========================
    # 스타일 정의
    # ========================
    st.markdown("""
    <style>
    /* 중앙 정렬용 컨테이너 */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* 메인 타이틀 */
    .main-title {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin-bottom: 40px;
    }

    /* CARPORT 글자만 그라데이션 */
    .gradient-text {
        font-size: 64px;
        font-weight: bold;
        background: linear-gradient(to right, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 이모지는 일반 컬러 */
    .emoji {
        font-size: 48px;
    }

    /* 프로젝트 개요 박스 */
    .project-box {
        background-color: #1e1e1e;
        border-radius: 16px;
        padding: 40px;
        margin-top: 30px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.6);
        color: #eee;
        font-size: 20px;
        line-height: 1.8;
        max-width: 800px;
        min-height: 200px;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        white-space: pre-wrap;
    }

    .project-box h4 {
        font-size: 26px;
        margin-bottom: 20px;
        color: #4facfe;
    }
    </style>
    """, unsafe_allow_html=True)

    # ========================
    # 메인 타이틀 (CARPORT 그라데이션, 양옆 이모지 일반 컬러)
    # ========================
    st.markdown("""
    <div class="center-container">
        <div class="main-title">
            <span class="emoji">📊</span>
            <span class="gradient-text">CARPORT</span>
            <span class="emoji">🚗</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========================
    # 프로젝트 개요
    # ========================
    st.markdown("""
    <div class="center-container">
        <div class="project-box">
            <h4>📋 프로젝트 개요</h4>
            🚘 자동차 등록 현황을 한눈에 확인<br>
            🏆 작년에 제일 많이 팔린 차종 확인 가능<br>
            🌐 여러 사이트 정보를 통합하여 편리하게 조회
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========================
    # 현재 페이지 표시
    # ========================
page = st.session_state.get('page', 'home')

# 페이지 정의
home = st.Page(homepage, title="Home", icon="🏠")  # 홈 아이콘
total_registered_vehicle_page = st.Page(
    "total_registered_vehicle/total_registered_page.py", 
    title="🚘 국내 자동차 등록 현황", 
)
popular_vehicle_page = st.Page(
    "vehicle_sales/vehicle_sales_page.py", 
    title="🏆 최신 자동차 판매량 조회", 
)
new_registered_vehicle_page = st.Page(
    "new_registered_vehicle/new_registered_page.py", 
    title="👥 자동차 신규등록 트렌드 조회", 
)
faq_page = st.Page(
    "faq/faq_page.py", 
    title="❓ FAQ", 
)
# 내비게이션 생성
pg = st.navigation([home, total_registered_vehicle_page, popular_vehicle_page, new_registered_vehicle_page, faq_page])
pg.run()
