import streamlit as st
st.title("挨拶アプリ")
user_name=st.text_input("名前を入力してください")
st.text("名前を入力してください")
if st.button("挨拶する"):    
    st.text(f"こんにちは{user_name}さん!　今日も素晴らしい一日ですね")
