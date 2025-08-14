import streamlit as st

# --------------------------
# MBTI 궁합 데이터 (예시)
# --------------------------
mbti_match_data = {
    "INTJ": {
        "best_match": "ENFP",
        "description": "INTJ는 계획적이고 전략적인 성향을 가지며, ENFP는 자유롭고 창의적인 성향을 가져 서로를 보완합니다."
    },
    "ENTP": {
        "best_match": "INFJ",
        "description": "ENTP의 에너지는 INFJ의 깊이 있는 사고와 잘 어울리며, 서로 새로운 관점을 제공합니다."
    },
    "INFJ": {
        "best_match": "ENFP",
        "description": "INFJ의 내향적이면서도 따뜻한 성향은 ENFP의 외향적이고 활발한 에너지와 균형을 이룹니다."
    },
    "ENFP": {
        "best_match": "INTJ",
        "description": "ENFP의 창의적이고 사교적인 성격은 INTJ의 계획성과 결단력을 북돋습니다."
    },
    "ISTJ": {
        "best_match": "ESFP",
        "description": "ISTJ의 성실함과 책임감은 ESFP의 활발하고 긍정적인 에너지와 좋은 조화를 이룹니다."
    },
    "ESFP": {
        "best_match": "ISTJ",
        "description": "ESFP의 활동적인 성향은 ISTJ의 안정감과 현실적인 태도에 매력을 느낍니다."
    },
    # 필요 시 더 추가 가능
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
st.caption("📌 이 앱은 간단한 예시 데이터를 기반으로 만들어졌으며, 실제 궁합과는 다를 수 있습니다.")
