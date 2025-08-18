import streamlit as st
import pandas as pd

# ---------------------- 기본 설정 ----------------------
st.set_page_config(page_title="건강 관리 대시보드", page_icon="🏃", layout="wide")

st.title("🏃 건강 관리 대시보드")
st.markdown("""
이 앱은 **BMI 계산기**, **권장 칼로리 추천**, **운동 기록 시각화** 기능을 제공합니다.  

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
        advice = "체중을 조금 늘리는 것이 필요합니다. 단백질과 영양소를 충분히 섭취하세요."
        card_color = "#cce5ff"
    elif 18.5 <= bmi < 25:
        bmi_status = "정상"
        bmi_color = "🟢"
        advice = "매우 건강한 상태입니다! 지금과 같은 생활 습관을 유지하세요."
        card_color = "#d4edda"
    elif 25 <= bmi < 30:
        bmi_status = "과체중"
        bmi_color = "🟠"
        advice = "체중 관리가 필요합니다. 꾸준한 운동과 균형 잡힌 식단을 권장합니다."
        card_color = "#fff3cd"
    else:
        bmi_status = "비만"
        bmi_color = "🔴"
        advice = "비만 상태입니다. 식습관 개선과 규칙적인 운동이 꼭 필요합니다. 전문가 상담도 고려해보세요."
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

    # 운동 기록
    st.sidebar.subheader("📅 운동 기록 입력")
    exercise_data = {}
    for day in ["월", "화", "수", "목", "금", "토", "일"]:
        exercise_data[day] = st.sidebar.number_input(f"{day}요일 운동 시간(분)", min_value=0, max_value=300, value=0, key=day)

    exercise_df = pd.DataFrame(list(exercise_data.items()), columns=["요일", "운동 시간(분)"])

    # 메인 화면 출력
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="background-color:{card_color}; padding:20px; border-radius:10px;">
        <h3>💡 {name}님의 건강 지표</h3>
        <p><b>BMI:</b> {bmi} {bmi_color} ({bmi_status})</p>
        <p><b>권장 칼로리:</b> {calorie_needs} kcal</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("📊 주간 운동 기록")
        st.bar_chart(exercise_df.set_index("요일"))

    # 요약 + 조언 (카드 스타일)
    st.markdown(f"""
    <div style="background-color:#f1f1f1; padding:20px; border-radius:10px; margin-top:20px;">
    <h3>✅ 종합 요약</h3>
    <ul>
        <li><b>BMI 상태:</b> {bmi_color} {bmi_status}</li>
        <li><b>권장 칼로리:</b> {calorie_needs} kcal</li>
        <li><b>총 운동 시간(주간):</b> {sum(exercise_data.values())} 분</li>
    </ul>
    <p>👉 꾸준한 운동과 올바른 식습관이 건강을 지켜줍니다!</p>

    <h3>💬 맞춤 조언</h3>
    <p>{advice}</p>
    </div>
    """, unsafe_allow_html=True)
