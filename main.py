import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 궁합 추천 웹앱",
    page_icon="💞",
    layout="centered"
)

st.title("💞 MBTI 궁합 추천 웹앱")
st.write("당신의 MBTI를 선택하면 잘 맞는 MBTI와 설명을 보여드립니다!")

# MBTI 데이터
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

compatibility = {
    "INTJ": {
        "matches": ["ENFP", "ENTP"],
        "desc": "전략가형 INTJ는 창의적이고 활발한 ENFP, ENTP와 잘 어울립니다."
    },
    "INTP": {
        "matches": ["ENTJ", "ESTJ"],
        "desc": "사색가형 INTP는 추진력 있는 ENTJ, ESTJ와 균형을 이룹니다."
    },
    "ENTJ": {
        "matches": ["INTP", "INFJ"],
        "desc": "리더형 ENTJ는 사색적인 INTP, 따뜻한 INFJ와 조화를 이룹니다."
    },
    "ENTP": {
        "matches": ["INFJ", "INTJ"],
        "desc": "도전가형 ENTP는 깊이 있는 INFJ, 전략적인 INTJ와 좋은 궁합입니다."
    },
    "INFJ": {
        "matches": ["ENFP", "ENTP"],
        "desc": "옹호자형 INFJ는 자유로운 ENFP, 에너제틱한 ENTP와 잘 맞습니다."
    },
    "INFP": {
        "matches": ["ENFJ", "ENTJ"],
        "desc": "중재자형 INFP는 따뜻한 ENFJ, 결단력 있는 ENTJ와 잘 어울립니다."
    },
    "ENFJ": {
        "matches": ["INFP", "ISFP"],
        "desc": "정의로운 ENFJ는 감성적인 INFP, 예술적인 ISFP와 조화를 이룹니다."
    },
    "ENFP": {
        "matches": ["INTJ", "INFJ"],
        "desc": "활동가형 ENFP는 깊이 있는 INTJ, INFJ와 좋은 관계를 형성합니다."
    },
    "ISTJ": {
        "matches": ["ESFP", "ESTP"],
        "desc": "청렴결백형 ISTJ는 활발한 ESFP, ESTP와 잘 어울립니다."
    },
    "ISFJ": {
        "matches": ["ESFP", "ESTP"],
        "desc": "수호자형 ISFJ는 사교적인 ESFP, ESTP와 좋은 궁합입니다."
    },
    "ESTJ": {
        "matches": ["ISFP", "ISTP"],
        "desc": "경영자형 ESTJ는 부드러운 ISFP, 유연한 ISTP와 균형을 이룹니다."
    },
    "ESFJ": {
        "matches": ["ISFP", "ISTP"],
        "desc": "친선도모형 ESFJ는 예술적인 ISFP, 탐험가형 ISTP와 잘 맞습니다."
    },
    "ISTP": {
        "matches": ["ESFJ", "ENFJ"],
        "desc": "장인형 ISTP는 사교적인 ESFJ, ENFJ와 좋은 궁합입니다."
    },
    "ISFP": {
        "matches": ["ENFJ", "ESFJ"],
        "desc": "예술가형 ISFP는 따뜻한 ENFJ, ESFJ와 좋은 관계를 맺습니다."
    },
    "ESTP": {
        "matches": ["ISFJ", "INFJ"],
        "desc": "사업가형 ESTP는 헌신적인 ISFJ, 깊이 있는 INFJ와 조화를 이룹니다."
    },
    "ESFP": {
        "matches": ["ISFJ", "ISTJ"],
        "desc": "엔터테이너형 ESFP는 신중한 ISFJ, ISTJ와 좋은 궁합입니다."
    }
}

# MBTI 이미지 경로 (이미지 파일은 같은 폴더 내 images/ 폴더에 저장)
# 예: images/INTJ.png, images/ENTP.png ...
image_path = {mbti: f"images/{mbti}.png" for mbti in mbti_list}

# MBTI 선택 (드롭다운)
user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 결과 출력
if user_mbti:
    data = compatibility[user_mbti]
    st.subheader(f"✨ {user_mbti} 궁합 결과 ✨")
    
    # MBTI 이미지
    st.image(image_path[user_mbti], width=200, caption=f"{user_mbti} 타입")
    
    # 설명
    st.write(f"**잘 맞는 MBTI:** {', '.join(data['matches'])}")
    st.info(data['desc'])
    
    # 잘 맞는 MBTI 이미지들
    st.write("💖 잘 맞는 MBTI 이미지 보기")
    cols = st.columns(len(data['matches']))
    for i, match_mbti in enumerate(data['matches']):
        with cols[i]:
            st.image(image_path[match_mbti], width=150, caption=match_mbti)

