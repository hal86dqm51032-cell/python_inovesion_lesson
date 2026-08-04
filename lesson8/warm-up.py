import streamlit as st
st.title("シンプルカウンターアプリ")
count=0
if "count" not in st.session_state:
    st.session_state.count=0
if st.button("カウントアップ"):
    st.session_state.count+=1
st.write(f"現在のカウント:{st.session_state.count}")