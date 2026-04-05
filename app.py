import streamlit as st
from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🏗️ 친환경 건축 아이디어 생성기")

st.write("건물 문제를 입력하면 AI가 해결 아이디어를 제안합니다")

user_input = st.text_area("예: 여름에 너무 더운 아파트 옥상")

if st.button("아이디어 생성"):
    if user_input:
response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"너는 친환경 건축 전문가야. 현실적이고 구체적인 해결 방법을 3가지 bullet point로 제시해.\n\n문제: {user_input}"
)

result = response.output_text

        st.write("### 💡 추천 아이디어")
        st.write(result)
    else:
        st.warning("내용을 입력하세요!")
