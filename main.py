import streamlit as st

# MBTI 궁합 데이터 (예시)
compatibility = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["ENTJ", "ESTJ"],
    "ENTJ": ["INTP", "INFJ"],
    "ENTP": ["INFJ", "INTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ENTJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INTJ", "INFJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["ISFP", "ISTP"],
    "ESFJ": ["ISFP", "ISTP"],
    "ISTP": ["ESFJ", "ENFJ"],
    "ISFP": ["ENFJ", "ESFJ"],
    "ESTP": ["ISFJ", "INFJ"],
    "ESFP": ["ISFJ", "ISTJ"]
}

st.title("MBTI 궁합 추천 웹앱 💞")

# MBTI 입력 받기
user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)").upper()

# 결과 출력
if user_mbti:
    if user_mbti in compatibility:
        matches = compatibility[user_mbti]
        st.success(f"{user_mbti}와 잘 맞는 MBTI는: {', '.join(matches)} 입니다!")
    else:
        st.error("올바른 MBTI를 입력해주세요. (예: INFP, ENTP)")

