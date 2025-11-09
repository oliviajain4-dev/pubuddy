# logic.py
from 1_data.python_data import python_knowledge

# 🔍 설명형 검색 강화 버전
def find_concept(query: str):
    query = query.lower().strip()
    results = []

    for name, data in python_knowledge.items():
        # ① 함수명 일치
        if query == name.lower():
            return name, data

        # ② 설명문/키워드 포함
        if query in data["desc"].lower() or any(query in kw.lower() for kw in data.get("keywords", [])):
            results.append((name, data))

    # ③ 여러 결과 중 가장 중요도 높은 것
    if results:
        results.sort(key=lambda x: x[1]["importance"], reverse=True)
        return results[0]

    return None, None


# 🧩 카드 표시 함수
def show_card(query: str):
    name, data = find_concept(query)
    if not data:
        st.warning("해당 설명이나 개념을 찾지 못했어요 😅")
        return

    st.markdown(f"### 📘 {name}()")
    st.markdown(f"**📂 분류:** {data['type']}")
    st.markdown(f"**⭐ 중요도:** {'★' * data['importance']}")
    st.markdown(f"**📖 설명:** {data['desc']}")
    st.code(data['example'], language="python")
    st.markdown(f"**🪄 사용방법:** {data['usage']}")
    st.markdown(f"**🔗 관련 개념:** {', '.join(data['related'])}")