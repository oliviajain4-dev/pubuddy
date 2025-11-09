# =========================================================
# 🐍 PyBuddy — 파이썬 학습 도감 (업그레이드 버전)
# =========================================================

import streamlit as st

# =========================================================
# [1️⃣ 기본 설정]
# =========================================================
st.set_page_config(
    page_title="PyBuddy - 파이썬 도감",
    page_icon="🐍",
    layout="centered"
)

# 세션 상태 초기화
if "saved_cards" not in st.session_state:
    st.session_state.saved_cards = []
if "history" not in st.session_state:
    st.session_state.history = []
if "current_index" not in st.session_state:
    st.session_state.current_index = -1

# =========================================================
# [2️⃣ 데이터: 파이썬 핵심 지식 샘플]
# =========================================================
python_knowledge = {
    "print": {
        "type": "기본 함수",
        "importance": 5,
        "desc": "콘솔(터미널)에 데이터를 출력합니다.",
        "example": "print('Hello, world!')",
        "usage": "가장 기본적인 출력 함수입니다.",
        "related": ["input", "len"]
    },
    "len": {
        "type": "기본 함수",
        "importance": 5,
        "desc": "객체(문자열, 리스트 등)의 길이를 반환합니다.",
        "example": "len('hello')  # 5",
        "usage": "문자열, 리스트, 딕셔너리 길이 계산 시 사용.",
        "related": ["count", "sum"]
    },
    "append": {
        "type": "리스트 메서드",
        "importance": 5,
        "desc": "리스트 끝에 요소를 추가합니다.",
        "example": "my_list = [1, 2]\nmy_list.append(3)",
        "usage": "리스트에 데이터 누적 시 사용.",
        "related": ["insert", "extend"]
    },
}

# =========================================================
# [3️⃣ 로직 함수]
# =========================================================
def show_card(query: str):
    """카드 표시 함수"""
    data = python_knowledge.get(query.lower())
    if not data:
        st.warning("아직 등록되지 않은 개념이에요 😅")
        return

    # 탐색 기록 업데이트
    st.session_state.history.append(query)
    st.session_state.current_index = len(st.session_state.history) - 1

    st.markdown(f"### 📘 {query}()")
    st.markdown(f"**📂 분류:** {data['type']}")
    st.markdown(f"**⭐ 중요도:** {'★' * data['importance']}")
    st.markdown(f"**📖 설명:** {data['desc']}")
    st.code(data['example'], language="python")
    st.markdown(f"**🪄 사용방법:** {data['usage']}")
    st.markdown(f"**🔗 관련 개념:** {', '.join(data['related'])}")

    if st.button("💾 이 카드 저장하기", key=f"save_{query}"):
        if query not in st.session_state.saved_cards:
            st.session_state.saved_cards.append(query)
            st.success(f"'{query}'를 내 보관함에 저장했어요! 🎉")
        else:
            st.info("이미 저장된 카드예요 😊")

# =========================================================
# [4️⃣ UI 출력]
# =========================================================
st.title("🐍 PyBuddy — 파이썬 지식 도감")
st.caption("기초부터 차근차근, 내가 직접 정리하는 파이썬 학습 챗봇 💡")

# 🔹 입력창 강화
st.markdown("### 🔍 알고 싶은 파이썬 개념을 입력하세요")
query = st.text_input(
    "예시: append, if, len ...",
    placeholder="여기에 검색어를 입력하세요 👇",
    key="search_input"
)

# 시각 강조 (눈에 잘 띄는 색상)
st.markdown(
    """
    <style>
    input[type="text"] {
        border: 2px solid #00bfff;
        border-radius: 10px;
        font-size: 18px;
        background-color: #f0faff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🔹 탐색 버튼 영역
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 홈"):
        st.session_state.history = []
        st.session_state.current_index = -1
        st.experimental_rerun()
with col2:
    if st.button("⬅️ 뒤로"):
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1
            show_card(st.session_state.history[st.session_state.current_index])
with col3:
    if st.button("➡️ 앞으로"):
        if st.session_state.current_index < len(st.session_state.history) - 1:
            st.session_state.current_index += 1
            show_card(st.session_state.history[st.session_state.current_index])
with col4:
    if st.button("🔄 새로고침"):
        st.experimental_rerun()

st.markdown("---")

if query:
    show_card(query)

# 🔹 사이드바
with st.sidebar:
    st.header("📂 내 보관함")
    if st.session_state.saved_cards:
        for saved in st.session_state.saved_cards:
            st.write(f"- {saved}")
    else:
        st.caption("아직 저장된 카드가 없어요 💡")

    st.markdown("---")
    st.info("다음 목표: 🃏 플래시카드(앞/뒤 보기) 모드 추가 예정!")
    # =========================================================
# 🐍 PyBuddy — 파이썬 학습 도감 (Flashcards + 100 Concepts)
# =========================================================

import streamlit as st
import random

# =========================================================
# [1️⃣ 기본 설정]
# =========================================================
st.set_page_config(
    page_title="PyBuddy - 파이썬 도감",
    page_icon="🐍",
    layout="centered"
)

if "saved_cards" not in st.session_state:
    st.session_state.saved_cards = []
if "history" not in st.session_state:
    st.session_state.history = []
if "current_index" not in st.session_state:
    st.session_state.current_index = -1
if "flash_index" not in st.session_state:
    st.session_state.flash_index = 0
if "flash_show_back" not in st.session_state:
    st.session_state.flash_show_back = False

# =========================================================
# [2️⃣ 파이썬 기초 100개 데이터]
# =========================================================
python_knowledge = {
    "print": {"type": "기본 함수", "importance": 5, "desc": "콘솔에 내용을 출력합니다.", "example": "print('Hello')", "usage": "출력용", "related": ["input", "len"]},
    "input": {"type": "기본 함수", "importance": 5, "desc": "사용자로부터 입력을 받습니다.", "example": "name = input('이름: ')", "usage": "콘솔 입력", "related": ["print"]},
    "len": {"type": "기본 함수", "importance": 5, "desc": "객체의 길이를 반환합니다.", "example": "len('abc')", "usage": "길이 계산", "related": ["count"]},
    "type": {"type": "기본 함수", "importance": 5, "desc": "데이터의 타입을 확인합니다.", "example": "type(3)", "usage": "타입 확인", "related": ["isinstance"]},
    "int": {"type": "자료형 변환", "importance": 5, "desc": "정수형으로 변환합니다.", "example": "int('10')", "usage": "문자열→정수", "related": ["float", "str"]},
    "float": {"type": "자료형 변환", "importance": 5, "desc": "실수형으로 변환합니다.", "example": "float('3.14')", "usage": "형변환", "related": ["int", "str"]},
    "str": {"type": "자료형 변환", "importance": 5, "desc": "문자열로 변환합니다.", "example": "str(123)", "usage": "출력 전 변환", "related": ["int"]},
    "list": {"type": "자료형", "importance": 5, "desc": "여러 값을 순서대로 저장합니다.", "example": "nums = [1, 2, 3]", "usage": "데이터 집합 저장", "related": ["tuple", "dict"]},
    "dict": {"type": "자료형", "importance": 5, "desc": "키-값 쌍으로 데이터를 저장합니다.", "example": "d = {'a':1, 'b':2}", "usage": "매핑 구조", "related": ["list", "set"]},
    "set": {"type": "자료형", "importance": 4, "desc": "중복 없는 집합형 데이터", "example": "s = {1,2,3}", "usage": "중복 제거", "related": ["list"]},
    "tuple": {"type": "자료형", "importance": 4, "desc": "변경 불가능한 리스트", "example": "t = (1,2,3)", "usage": "불변 데이터 저장", "related": ["list"]},
    "append": {"type": "리스트 메서드", "importance": 5, "desc": "리스트 끝에 요소 추가", "example": "a.append(4)", "usage": "누적 저장", "related": ["extend", "insert"]},
    "remove": {"type": "리스트 메서드", "importance": 4, "desc": "첫 번째 일치 요소 제거", "example": "a.remove(2)", "usage": "요소 삭제", "related": ["pop", "del"]},
    "pop": {"type": "리스트 메서드", "importance": 4, "desc": "인덱스로 요소 제거 후 반환", "example": "a.pop(1)", "usage": "데이터 추출", "related": ["remove"]},
    "for": {"type": "제어문", "importance": 5, "desc": "반복문 실행", "example": "for i in range(3): print(i)", "usage": "반복 처리", "related": ["while"]},
    "while": {"type": "제어문", "importance": 5, "desc": "조건이 참일 때 반복", "example": "while x < 5: x += 1", "usage": "조건 반복", "related": ["for"]},
    "if": {"type": "제어문", "importance": 5, "desc": "조건에 따라 실행 분기", "example": "if x>0: print('양수')", "usage": "조건 판단", "related": ["else", "elif"]},
    "elif": {"type": "제어문", "importance": 4, "desc": "추가 조건 분기", "example": "if x==0: pass\nelif x>0: print('양수')", "usage": "복수 조건", "related": ["if", "else"]},
    "else": {"type": "제어문", "importance": 4, "desc": "조건이 거짓일 때 실행", "example": "if x<0: print('음수')\nelse: print('양수')", "usage": "조건 분기", "related": ["if"]},
    "def": {"type": "함수 정의", "importance": 5, "desc": "사용자 정의 함수 생성", "example": "def add(a,b): return a+b", "usage": "함수 선언", "related": ["return", "lambda"]},
    "return": {"type": "함수 제어", "importance": 4, "desc": "함수 실행 결과 반환", "example": "return a+b", "usage": "값 전달", "related": ["def"]},
    "import": {"type": "모듈", "importance": 5, "desc": "외부 모듈 가져오기", "example": "import math", "usage": "라이브러리 불러오기", "related": ["from"]},
    "from": {"type": "모듈", "importance": 4, "desc": "특정 함수만 불러오기", "example": "from math import sqrt", "usage": "부분 import", "related": ["import"]},
    "class": {"type": "객체지향", "importance": 5, "desc": "새로운 클래스 정의", "example": "class Dog: pass", "usage": "객체 생성용", "related": ["object", "init"]},
    "try": {"type": "예외 처리", "importance": 4, "desc": "에러 발생 시 예외 처리", "example": "try: 1/0\nexcept: print('Error')", "usage": "오류 방지", "related": ["except", "finally"]},
    "lambda": {"type": "익명 함수", "importance": 3, "desc": "간단한 한 줄 함수", "example": "square = lambda x: x**2", "usage": "간결한 함수 정의", "related": ["def"]},
    "open": {"type": "파일 입출력", "importance": 5, "desc": "파일 열기", "example": "f=open('a.txt','r')", "usage": "파일 읽기/쓰기", "related": ["read", "write"]},
    "read": {"type": "파일 입출력", "importance": 4, "desc": "파일 읽기", "example": "f.read()", "usage": "파일 데이터 읽기", "related": ["open"]},
    "write": {"type": "파일 입출력", "importance": 4, "desc": "파일에 쓰기", "example": "f.write('text')", "usage": "파일 데이터 저장", "related": ["open"]},
    # 나머지 60개도 이런 식으로 확장 가능
}

# =========================================================
# [3️⃣ 카드 표시 함수]
# =========================================================
def show_card(query: str):
    data = python_knowledge.get(query.lower())
    if not data:
        st.warning("아직 등록되지 않은 개념이에요 😅")
        return

    st.markdown(f"### 📘 {query}()")
    st.markdown(f"**📂 분류:** {data['type']}")
    st.markdown(f"**⭐ 중요도:** {'★' * data['importance']}")
    st.markdown(f"**📖 설명:** {data['desc']}")
    st.code(data['example'], language="python")
    st.markdown(f"**🪄 사용방법:** {data['usage']}")
    st.markdown(f"**🔗 관련 개념:** {', '.join(data['related'])}")

    if st.button("💾 이 카드 저장하기", key=query):
        if query not in st.session_state.saved_cards:
            st.session_state.saved_cards.append(query)
            st.success(f"'{query}'를 내 보관함에 저장했어요! 🎉")
        else:
            st.info("이미 저장된 카드예요 😊")

# =========================================================
# [4️⃣ 플래시카드 기능]
# =========================================================
def flashcard_mode():
    st.subheader("🃏 플래시카드 암기 모드")
    if not st.session_state.saved_cards:
        st.warning("아직 저장된 카드가 없어요 💡")
        return

    cards = st.session_state.saved_cards
    if st.button("랜덤 카드 뽑기 🎲"):
        st.session_state.flash_index = random.randint(0, len(cards)-1)
        st.session_state.flash_show_back = False

    if cards:
        query = cards[st.session_state.flash_index]
        data = python_knowledge.get(query, None)
        if not data:
            st.error("등록되지 않은 카드입니다.")
            return

        st.markdown(f"### 📘 {query}()")
        if not st.session_state.flash_show_back:
            st.markdown("> 카드 앞면 👀: **개념 이름**")
            if st.button("🔁 뒤집기 (정답 보기)"):
                st.session_state.flash_show_back = True
        else:
            st.markdown(f"**📖 설명:** {data['desc']}")
            st.code(data['example'], language="python")
            st.markdown(f"**⭐ 중요도:** {'★' * data['importance']}")
            if st.button("🔙 다시 앞면으로"):
                st.session_state.flash_show_back = False

# =========================================================
# [5️⃣ UI 출력]
# =========================================================
st.title("🐍 PyBuddy — 파이썬 지식 도감")
st.caption("기초부터 차근차근, 내가 직접 정리하는 파이썬 학습 챗봇 💬")

query = st.text_input("찾고 싶은 파이썬 개념 (예: append, if, len):")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 홈"): st.experimental_rerun()
with col2:
    if st.button("⬅️ 뒤로"): st.warning("뒤로가기 기능 준비 중 🚧")
with col3:
    if st.button("➡️ 앞으로"): st.warning("앞으로가기 기능 준비 중 🚧")
with col4:
    if st.button("🔄 새로고침"): st.experimental_rerun()

st.markdown("---")

if query:
    show_card(query)

with st.sidebar:
    st.header("📂 내 보관함")
    if st.session_state.saved_cards:
        for saved in st.session_state.saved_cards:
            st.write(f"- {saved}")
    else:
        st.caption("아직 저장된 카드가 없어요 💡")

    st.markdown("---")
    flashcard_mode()

