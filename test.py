import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(page_title="건강 관리 대시보드", page_icon="🏃", layout="wide")

st.title("🏃 건강 관리 대시보드")
st.markdown("""
이 앱은 **BMI 계산기**, **권장 칼로리 추천**, **식단 및 운동 조언** 기능을 제공합니다.  

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
        diet = {
            "아침": "계란, 두유, 통곡물 빵",
            "점심": "닭가슴살, 현미밥, 채소 볶음",
            "저녁": "연어, 고구마, 샐러드",
            "간식": "견과류, 요거트"
        }
    elif 18.5 <= bmi < 25:
        bmi_status = "정상"
        bmi_color = "🟢"
        advice = "매우 건강한 상태입니다! 지금과 같은 생활 습관을 유지하세요."
        card_color = "#d4edda"
        diet = {
            "아침": "오트밀, 과일, 우유",
            "점심": "잡곡밥, 생선구이, 나물",
            "저녁": "두부 스테이크, 샐러드, 현미밥",
            "간식": "과일, 삶은 달걀"
        }
    elif 25 <= bmi < 30:
        bmi_status = "과체중"
        bmi_color = "🟠"
        advice = "체중 관리가 필요합니다. 꾸준한 운동과 균형 잡힌 식단을 권장합니다."
        card_color = "#fff3cd"
        diet = {
            "아침": "삶은 달걀, 블랙커피, 채소",
            "점심": "현미밥 소량, 닭가슴살, 샐러드",
            "저녁": "채소 스프, 고구마, 두부",
            "간식": "방울토마토, 오이"
        }
    else:
        bmi_status = "비만"
        bmi_color = "🔴"
        advice = "비만 상태입니다. 식습관 개선과 규칙적인 운동이 꼭 필요합니다. 전문가 상담도 고려해보세요."
        card_color = "#f8d7da"
        diet = {
            "아침": "귀리죽, 삶은 달걀",
            "점심": "잡곡밥 소량, 삶은 채소, 닭가슴살",
            "저녁": "두부 샐러드, 채소 수프",
            "간식": "무가당 요거트, 오이"
        }

    # 권장 칼로리 계산 (BMR 공식)
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

    # 정상 BMI 범위 몸무게 계산
    min_weight = round(18.5 * (height_m ** 2), 1)
    max_weight = round(24.9 * (height_m ** 2), 1)

    if bmi < 18.5:
        normal_range_msg = f"👉 건강한 범위에 들어가려면 최소 {min_weight}kg 이상이 필요합니다."
    elif bmi >= 25:
        normal_range_msg = f"👉 건강한 범위에 들어가려면 최대 {max_weight}kg 이하로 줄여야 합니다."
    else:
        normal_range_msg = "👉 현재 정상 범위에 속해 있어 체중 조절이 필요하지 않습니다."

    # 메인 화면 출력
    st.markdown(f"""
    <div style="background-color:{card_color}; padding:20px; border-radius:10px;">
    <h3>💡 {name}님의 건강 지표</h3>
    <p><b>BMI:</b> {bmi} {bmi_color} ({bmi_status})</p>
    <p><b>권장 칼로리:</b> {calorie_needs} kcal</p>
    <p>{normal_range_msg}</p>
    </div>
    """, unsafe_allow_html=True)

    # 요약 + 조언 (카드 스타일)
    st.markdown(f"""
    <div style="background-color:#f1f1f1; padding:20px; border-radius:10px; margin-top:20px;">
    <h3>✅ 종합 요약</h3>
    <ul>
        <li><b>BMI 상태:</b> {bmi_color} {bmi_status}</li>
        <li><b>권장 칼로리:</b> {calorie_needs} kcal</li>
        <li>{normal_range_msg}</li>
    </ul>

    <h3>💬 맞춤 조언</h3>
    <p>{advice}</p>

    <h3>🍽️ 식단 예시</h3>
    <ul>
        <li><b>아침:</b> {diet['아침']}</li>
        <li><b>점심:</b> {diet['점심']}</li>
        <li><b>저녁:</b> {diet['저녁']}</li>
        <li><b>간식:</b> {diet['간식']}</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
