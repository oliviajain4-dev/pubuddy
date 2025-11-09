# =========================================================
# 🎨 PyBuddy UI — 메인 실행 파일
# =========================================================
import streamlit as st
import sys, os

# 폴더 인식 확장
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 로직 불러오기
from 2_modules.logic import show_card


# 🔽 모듈 경로 연결
from 2_modules.logic import show_card
from 2_modules.auth import create_user, authenticate, update_user_cards

# 페이지 설정
st.set_page_config(page_title="🐍 PyBuddy", page_icon="🐍", layout="centered")
st.title("🐍 PyBuddy — 파이썬 지식 도감")
st.caption("50개 필수 개념 + 설명형 검색 챗봇 💡")

# 사용자 입력
query = st.text_input("🔍 찾고 싶은 파이썬 개념이나 설명을 입력하세요 (예: 리스트 추가, print, 조건문 등):")

# 결과 표시
if query:
    show_card(query)