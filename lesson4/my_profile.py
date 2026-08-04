import streamlit as st
from datetime import date,timedelta
st.title("毎プロフィール作成アプリ")

user_name=st.text_input("名前を入力してください")
st.write(user_name)

today=date.today()
next_week=today+timedelta(days=7)
nextmonth=today+timedelta(days=30)
ten_years_ago=today.replace(year=today.year-13)
year_end=date(today.year,12,31)
user_birthday=st.date_input(
    "誕生日を入力してください",
    value=today,
    min_value=ten_years_ago,
    max_value=year_end)

user_age=st.slider("年齢を選んでください",
                   0,100)

user_like_color=st.color_picker(
    "好きな色を選んでください",
    value="#000000"
)

user_introduction=st.text_area("自己紹介する文を入力してください")

show_profile=st.button("プロフィールをまとめて表示")
if show_profile:
    st.header("あなたのプロフィール")
    st.write("**名前**:",user_name)
    st.write("**誕生日**:",user_birthday)
    st.write("**年齢**:",user_age)
    st.color_picker("**好きな色**:",value=user_like_color)
    st.write("**自己紹介**:",user_introduction)