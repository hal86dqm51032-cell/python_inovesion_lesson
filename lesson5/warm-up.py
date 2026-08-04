import streamlit as st
st.title("マイプロフィール")
name=st.text_input("名前を入力してください")
introduction=st.text_area("自己紹介を入力してください")
birthday=st.date_input("誕生日を選んでください")

st.write(f"名前:{name}")
st.write(f"自己紹介:{introduction}")
st.write(f"誕生日:{birthday}")
