import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(page_title="건강 관리 대시보드", page_icon="🏃", layout="wide")

st.title("🏃 건강 관리 대시보드")
st.markdown("""
이 앱은 **BMI 계산기**, **권장 칼로리 추천**, 그리고 **식습관·운동 조언**을 제공합니다.  

### 📌 BMI란?
BMI(체질량지수, Body Mass Index)는 **몸무게(kg) ÷ [키(m)]²** 로 계산됩니다.  
- **18.5 미만**: 저체중  
- **18.5 ~ 24.9**: 정상  
- **25 ~ 29.9**: 과체중  
- **30 이상**: 비만  

BMI는 건강 상태를 가늠하는 지표로 활용됩니다.
""")

# ---------------------- 사용자 입력 ----------------------
st.sidebar.header("개인 정보 입력")
name = st.sidebar.text_input("이름을 입력하세요", "홍길동")
age = st.sidebar.number_input("나이", min_value=10, max_value=100, value=20)
gender = st.sidebar.selectbox("성별", ["남성", "여성"])
height = st.sidebar.number_input("키(cm)", min_value=100, max_value=220, value=170)
weight = st.sidebar.number_input("몸무게(kg)", min_value=30, max_value=150, value=65)
activity_level = st.sidebar.selectbox(
    "활동 수준",
    ["거의 운동 안 함", "가벼운 활동", "보통 활동", "적극적인 활동", "운동선수 수준"]
)

# ---------------------- 버튼 클릭 시 결과 계산 ----------------------
if st.sidebar.button("결과 확인하기"):
    # BMI 계산
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2) if height_m > 0 else 0

    if bmi < 18.5:
        bmi_status = "저체중"
        bmi_color = "🔵"
        advice = "체중을 늘리기 위해 단백질과 탄수화물이 충분한 균형 잡힌 식사를 하세요. 근력 운동을 병행하면 건강하게 체중을 늘릴 수 있습니다."
        card_color = "#cce5ff"
    elif 18.5 <= bmi < 25:
        bmi_status = "정상"
        bmi_color = "🟢"
        advice = "건강한 상태입니다! 현재 식습관을 유지하고, 주 3~4회 가벼운 유산소 운동과 스트레칭을 병행하세요."
        card_color = "#d4edda"
    elif 25 <= bmi < 30:
        bmi_status = "과체중"
        bmi_color = "🟠"
        advice = "체중 감량이 필요합니다. 야식과 당분 섭취를 줄이고, 주 3~5회 30분 이상의 유산소 운동을 권장합니다."
        card_color = "#fff3cd"
    else:
        bmi_status = "비만"
        bmi_color = "🔴"
        advice = "비만 상태입니다. 고칼로리 음식 섭취를 줄이고, 전문가와 상담하여 규칙적인 운동과 식단 관리를 시작하세요."
        card_color = "#f8d7da"

    # 권장 칼로리 계산
    if gender == "남성":
        bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

    activity_multipliers = {
        "거의 운동 안 함": 1.2,
        "가벼운 활동": 1.375,
        "보통 활동": 1.55,
        "적극적인 활동": 1.725,
        "운동선수 수준": 1.9,
    }

    calorie_needs = round(bmr * activity_multipliers.get(activity_level, 1.2))

    # 메인 화면 출력
    st.markdown(f"""
    <div style="background-color:{card_color}; padding:20px; border-radius:10px;">
    <h3>💡 {name}님의 건강 지표</h3>
    <p><b>BMI:</b> {bmi} {bmi_color} ({bmi_status})</p>
    <p><b>권장 칼로리:</b> {calorie_needs} kcal</p>
    </div>
    """, unsafe_allow_html=True)

    # 요약 + 조언 (카드 스타일)
    st.markdown(f"""
    <div style="background-color:#f1f1f1; padding:20px; border-radius:10px; margin-top:20px;">
    <h3>✅ 종합 요약</h3>
    <ul>
        <li><b>BMI 상태:</b> {bmi_color} {bmi_status}</li>
        <li><b>권장 칼로리:</b> {calorie_needs} kcal</li>
    </ul>

    <h3>🥗 맞춤 식습관 & 운동 조언</h3>
    <p>{advice}</p>
    </div>
    """, unsafe_allow_html=True)

