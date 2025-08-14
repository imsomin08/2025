import streamlit as st

# --------------------------
# MBTI 궁합 데이터 (16유형)
# --------------------------
mbti_match_data = {
    "INTJ": {
        "best_match": "ENFP",
        "description": "계획적이고 전략적인 INTJ는 자유롭고 창의적인 ENFP와 서로를 보완합니다."
    },
    "INTP": {
        "best_match": "ENTJ",
        "description": "논리적인 INTP는 결단력 있는 ENTJ와 함께 목표를 향해 나아가며 시너지를 냅니다."
    },
    "ENTJ": {
        "best_match": "INTP",
        "description": "리더십 강한 ENTJ는 분석적인 INTP와 함께 혁신적인 결과를 만들어냅니다."
    },
    "ENTP": {
        "best_match": "INFJ",
        "description": "활발한 ENTP는 깊이 있는 INFJ와 대화를 통해 서로에게 새로운 시각을 제공합니다."
    },
    "INFJ": {
        "best_match": "ENFP",
        "description": "내향적이면서도 따뜻한 INFJ는 에너제틱한 ENFP와 균형을 이룹니다."
    },
    "INFP": {
        "best_match": "ENFJ",
        "description": "이상주의적인 INFP는 이끌어주는 ENFJ와 함께 성장할 수 있습니다."
    },
    "ENFJ": {
        "best_match": "INFP",
        "description": "사교적이고 배려심 깊은 ENFJ는 INFP의 내면을 잘 이해하고 지지해줍니다."
    },
    "ENFP": {
        "best_match": "INTJ",
        "description": "창의적이고 사교적인 ENFP는 계획적인 INTJ에게 영감을 줍니다."
    },
    "ISTJ": {
        "best_match": "ESFP",
        "description": "책임감 있고 성실한 ISTJ는 긍정적이고 활동적인 ESFP와 좋은 조화를 이룹니다."
    },
    "ISFJ": {
        "best_match": "ESFP",
        "description": "배려심 깊은 ISFJ는 활발하고 친근한 ESFP와 균형 잡힌 관계를 만듭니다."
    },
    "ESTJ": {
        "best_match": "ISFP",
        "description": "체계적인 ESTJ는 온화하고 유연한 ISFP와 함께 균형을 이룹니다."
    },
    "ESFJ": {
        "best_match": "ISFP",
        "description": "사람을 좋아하는 ESFJ는 차분한 ISFP와 안정적인 관계를 형성합니다."
    },
    "ISTP": {
        "best_match": "ESTP",
        "description": "실용적인 ISTP는 모험심 있는 ESTP와 함께 새로운 경험을 즐깁니다."
    },
    "ISFP": {
        "best_match": "ESTJ",
        "description": "온화하고 예술적인 ISFP는 체계적인 ESTJ와 좋은 균형을 이룹니다."
    },
    "ESTP": {
        "best_match": "ISTP",
        "description": "모험심 많은 ESTP는 침착하고 실용적인 ISTP와 환상의 팀워크를 보여줍니다."
    },
    "ESFP": {
        "best_match": "ISTJ",
        "description": "활발하고 낙천적인 ESFP는 안정적이고 현실적인 ISTJ와 좋은 조화를 이룹니다."
    },
}

# --------------------------
# Streamlit 앱 UI
# --------------------------
st.set_page_config(page_title="MBTI 궁합 추천", page_icon="💞", layout="centered")

st.title("💞 MBTI 궁합 추천기")
st.write("당신의 MBTI를 입력하면 잘 맞는 MBTI와 이유를 알려드립니다.")

# MBTI 입력
user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: ENFP)", "").upper()

# 버튼 클릭 시 결과 표시
if st.button("궁합 보기"):
    if user_mbti in mbti_match_data:
        best_match = mbti_match_data[user_mbti]["best_match"]
        description = mbti_match_data[user_mbti]["description"]
        
        st.success(f"당신과 가장 잘 맞는 MBTI는 **{best_match}** 입니다!")
        st.write(description)
    else:
        st.error("등록되지 않은 MBTI입니다. 16가지 MBTI 유형 중 하나를 정확히 입력해주세요.")

# 푸터
st.markdown("---")
st.caption("📌 이 앱은 MBTI 궁합에 대한 일반적인 의견을 참고한 것이며, 개인차가 있을 수 있습니다.")
