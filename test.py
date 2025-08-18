import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------- 기본 설정 ----------------------
st.set_page_config(page_title="건강 관리 대시보드", page_icon="🏃", layout="wide")

st.title("🏃 건강 관리 대시보드")
st.markdown("""
이 앱은 **BMI 계산기**, **권장 칼로리 추천**, **운동 기록 시각화** 기능을 제공합니다.  
건강한 생활 습관을 만드는 데 도움을 줍니다!
""")

# ---------------------- 사용자 입력 ----------------------
st.sidebar.header("개인 정보 입력")
name = st.sidebar.text_input("이름을 입력하세요", "홍길동")
age = st.sidebar.number_input("나이", 10, 100, 20)
gender = st.sidebar.selectbox("성별", ["남성", "여성"])
height = st.sidebar.number_input("키(cm)", 100, 220, 170)
weight = st.sidebar.number_input("몸무게(kg)", 30, 150, 65)
activity_level = st.sidebar.selectbox(
    "활동 수준",
    ["거의 운동 안 함", "가벼운 활동", "보통 활동", "적극적인 활동", "운동선수 수준"]
)

# ---------------------- BMI 계산 ----------------------
height_m = height / 100
bmi = round(weight / (height_m ** 2), 2)

if bmi < 18.5:
    bmi_status = "저체중"
elif 18.5 <= bmi < 25:
    bmi_status = "정상"
elif 25 <= bmi < 30:
    bmi_status = "과체중"
else:
    bmi_status = "비만"

# ---------------------- 권장 칼로리 계산 ----------------------
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

calorie_needs = round(bmr * activity_multipliers[activity_level])

# ---------------------- 운동 기록 ----------------------
st.sidebar.subheader("📅 운동 기록 입력")
exercise_data = {}
for day in ["월", "화", "수", "목", "금", "토", "일"]:
    exercise_data[day] = st.sidebar.number_input(f"{day}요일 운동 시간(분)", 0, 300, 0)

exercise_df = pd.DataFrame(list(exercise_data.items()), columns=["요일", "운동 시간(분)"])

# ---------------------- 메인 화면 ----------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"💡 {name}님의 건강 지표")
    st.metric("BMI", f"{bmi}", bmi_status)
    st.metric("권장 칼로리", f"{calorie_needs} kcal")

with col2:
    st.subheader("📊 주간 운동 기록")
    fig, ax = plt.subplots(figsize=(5,3))
    ax.bar(exercise_df["요일"], exercise_df["운동 시간(분)"], color="skyblue")
    ax.set_ylabel("운동 시간(분)")
    ax.set_title("주간 운동량")
    st.pyplot(fig)

# ---------------------- 요약 ----------------------
st.markdown("""
### ✅ 종합 요약
- **BMI 상태**: {}  
- **권장 칼로리**: {} kcal  
- **총 운동 시간(주간)**: {} 분  

👉 꾸준한 운동과 올바른 식습관이 건강을 지켜줍니다!
""".format(bmi_status, calorie_needs, sum(exercise_data.values())))

