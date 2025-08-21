import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(page_title="건강 관리 대시보드", page_icon="🏃", layout="wide")

st.title("🏃 건강 관리 대시보드")
st.markdown("""
이 앱은 **BMI 계산기**, **권장 칼로리 추천**, 그리고 **식습관·운동 조언 + 아침/점심/저녁 식단 예시**를 제공합니다.  

### 📌 BMI란?
BMI(체질량지수, Body Mass Index)는 **몸무게(kg) ÷ [키(m)]²** 로 계산됩니다.  
- **18.5 미만**: 저체중  
- **18.5 ~ 24.9**: 정상  
- **25 ~ 29.9**: 과체중  
- **30 이상**: 비만  

BMI는 건강 상태를 가늠하는 지표로 활용됩니다.
""")

# ---------------------- 유틸 함수 ----------------------
def make_meal_plan(category: str, calorie_needs: int):
    """BMI 카테고리에 따라 기본 식단 예시를 반환합니다.
    calorie_needs에 맞춰 탄단지 균형(대략)을 고려해 분량을 안내합니다.
    """
    # 분량 가이드 (대략) — 칼로리에 따라 그램/컵 수를 조정
    if calorie_needs < 1700:
        portion = {
            "탄수화물": "밥 1공기(150g) 또는 현미·잡곡밥 120g",
            "단백질": "닭가슴살/두부/달걀 1~2단위(예: 닭가슴살 100g)",
            "채소": "채소 1~2컵",
            "지방": "견과류 한 줌(15g) 또는 올리브유 1작은술"
        }
    elif calorie_needs < 2100:
        portion = {
            "탄수화물": "밥 1.3공기(180g) 또는 고구마 200g",
            "단백질": "살코기/두부 150g 또는 달걀 2개",
            "채소": "채소 2컵 이상",
            "지방": "견과류 20g 또는 올리브유 1~2작은술"
        }
    else:
        portion = {
            "탄수화물": "밥 1.5공기(220g) 또는 통곡물빵 3장",
            "단백질": "살코기/생선 180~200g 또는 달걀 2~3개",
            "채소": "채소 2~3컵",
            "지방": "견과류 25~30g 또는 올리브유 2작은술"
        }

    base = {
        "저체중": {
            "advice": "에너지 섭취를 늘리고 규칙적으로 간식(우유·바나나·견과류)을 추가하세요. 근력운동 병행으로 건강하게 체중을 늘리세요.",
            "breakfast": [
                "그릭요거트 + 그래놀라 + 바나나",
                "스크램블 에그 + 통곡물빵 2장",
                "우유 한 컵(또는 두유)"
            ],
            "lunch": [
                "현미밥 + 닭가슴살 120g + 아보카도 샐러드",
                "두부김치(기름 적당히) + 나물 2종"
            ],
            "dinner": [
                "연어구이 150g + 통곡물밥 + 구운야채",
                "파스타(올리브오일 베이스) + 닭가슴살 100g"
            ],
            "snack": ["견과류 한 줌", "바나나/사과", "우유/두유"]
        },
        "정상": {
            "advice": "현재 식습관을 유지하되 가공식품·당류를 줄이고, 주 3~4회 30분 내외 유산소+스트레칭을 추천합니다.",
            "breakfast": [
                "오트밀 + 우유 + 블루베리",
                "달걀 2개 + 토마토 + 통곡물빵"
            ],
            "lunch": [
                "현미밥 + 제철채소 비빔 + 삶은계란",
                "메밀소바 + 닭가슴살 샐러드"
            ],
            "dinner": [
                "생선구이 + 샐러드 + 고구마",
                "두부스테이크 + 채소볶음 + 현미밥"
            ],
            "snack": ["플레인 요거트", "사과/배", "아몬드 몇 알"]
        },
        "과체중": {
            "advice": "당분·튀김·야식을 줄이고, 단백질과 채소 위주의 식단으로 포만감을 높이세요. 주 4~5회 30~40분 유산소를 권장합니다.",
            "breakfast": [
                "삶은 달걀 2개 + 방울토마토 + 통곡물빵 1장",
                "저지방 요거트 + 베리류 + 견과 소량"
            ],
            "lunch": [
                "닭가슴살 샐러드(올리브유 소량) + 통곡물빵 1장",
                "곤약/두부면 샐러드 + 과일 소량"
            ],
            "dinner": [
                "현미밥 소량 + 담백한 국(맑은탕) + 채소반찬 2~3종",
                "구운 생선/살코기 120g + 샐러드 + 고구마 소량"
            ],
            "snack": ["방울토마토", "오이/당근스틱", "아몬드 소량"]
        },
        "비만": {
            "advice": "칼로리 밀도 낮은 식품(채소·해조류·버섯) 위주로 드시고, 설탕·가공음료를 피하세요. 의사·영양사 상담을 권장합니다.",
            "breakfast": [
                "채소 오믈렛 + 통곡물빵 1장",
                "그릭요거트(무가당) + 베리류"
            ],
            "lunch": [
                "현미밥 소량 + 닭가슴살 120g + 채소무침 2종",
                "연두부 + 샐러드 + 삶은계란 1개"
            ],
            "dinner": [
                "구운 생선 120g + 채소수프 + 샐러드",
                "두부·버섯 볶음 + 채소 가득 비빔"
            ],
            "snack": ["무가당 차/아메리카노", "오이/셀러리", "아몬드 10~15알"]
        }
    }

    plan = base.get(category, base["정상"])  # 기본은 정상형

    # 분량 안내 문구 생성
    portion_text = " | ".join([f"{k}: {v}" for k, v in portion.items()])

    return plan, portion_text

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
        card_color = "#cce5ff"
    elif 18.5 <= bmi < 25:
        bmi_status = "정상"
        bmi_color = "🟢"
        card_color = "#d4edda"
    elif 25 <= bmi < 30:
        bmi_status = "과체중"
        bmi_color = "🟠"
        card_color = "#fff3cd"
    else:
        bmi_status = "비만"
        bmi_color = "🔴"
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

    # 식단 계획 생성
    meal_plan, portion_text = make_meal_plan(bmi_status, calorie_needs)

    # 메인 카드: BMI & 칼로리
    st.markdown(f"""
    <div style="background-color:{card_color}; padding:20px; border-radius:10px;">
      <h3>💡 {name}님의 건강 지표</h3>
      <p><b>BMI:</b> {bmi} {bmi_color} ({bmi_status})</p>
      <p><b>권장 칼로리:</b> {calorie_needs} kcal</p>
    </div>
    """, unsafe_allow_html=True)

    # 식단 카드
    st.markdown(f"""
    <div style="background-color:#f1f1f1; padding:20px; border-radius:10px; margin-top:20px;">
      <h3>🥗 아침/점심/저녁 식단 예시</h3>
      <p style="margin-bottom:8px;"><b>분량 가이드:</b> {portion_text}</p>
      <h4>🍳 아침</h4>
      <ul>{''.join([f'<li>{item}</li>' for item in meal_plan['breakfast']])}</ul>
      <h4>🍱 점심</h4>
      <ul>{''.join([f'<li>{item}</li>' for item in meal_plan['lunch']])}</ul>
      <h4>🍽️ 저녁</h4>
      <ul>{''.join([f'<li>{item}</li>' for item in meal_plan['dinner']])}</ul>
      <h4>🍎 간식(선택)</h4>
      <ul>{''.join([f'<li>{item}</li>' for item in meal_plan['snack']])}</ul>
    </div>
    """, unsafe_allow_html=True)

    # 조언 카드
    st.markdown(f"""
    <div style="background-color:#eef6ff; padding:20px; border-radius:10px; margin-top:20px;">
      <h3>💬 맞춤 조언</h3>
      <p>{meal_plan['advice']}</p>
      <p style="font-size:13px; color:#555;">*개인별 건강 상태에 따라 차이가 있을 수 있으므로 필요 시 전문가와 상담하세요.</p>
    </div>
    """, unsafe_allow_html=True)
