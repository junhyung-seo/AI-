import streamlit as st
from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🏗️ 친환경 건축 아이디어 생성기")

st.write("건물 문제를 입력하면 AI가 해결 아이디어를 제안합니다")

user_input = st.text_area("예: 여름에 너무 더운 아파트 옥상")

if st.button("아이디어 생성"):
    if user_input:

        if "더운" in user_input or "여름" in user_input:
            result = """
• 옥상 녹화 시스템을 도입하여 열 흡수를 줄인다
• 태양광 패널을 설치해 직사열을 차단하고 에너지를 생산한다
• 고성능 단열재를 적용하여 실내 온도 상승을 막는다
"""

        elif "에너지" in user_input:
            result = """
• 건물 외벽에 고효율 단열재를 적용한다
• 태양광 패널 및 신재생 에너지 시스템을 도입한다
• 스마트 에너지 관리 시스템을 통해 전력 사용을 최적화한다
"""

        elif "햇빛" in user_input or "어두운" in user_input:
            result = """
• 채광을 고려한 창문 배치를 재설계한다
• 반사율이 높은 외부 마감재를 활용한다
• 중정을 설계하여 자연광 유입을 증가시킨다
"""

        elif "소음" in user_input:
            result = """
• 이중창 구조를 적용하여 외부 소음을 차단한다
• 방음 벽체 및 흡음재를 활용한다
• 건물 주변에 식재를 배치하여 소음을 완화한다
"""

        else:
            result = """
• 건물 환경을 고려한 친환경 설계를 적용한다
• 자연 에너지를 활용하는 시스템을 도입한다
• 지속 가능한 건축 자재를 사용한다
"""

        st.write("### 💡 추천 아이디어")
        st.write(result)

    else:
        st.warning("내용을 입력하세요!")
