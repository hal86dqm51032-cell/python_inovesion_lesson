# 1
# age=15
# if age>=20:
#     print("成人です")
# elif age>=13 and age<20:
#     print("10代です")
# elif age<13:
#     print("子供です")

# 2
# total=0
# for i in range(1,11):
#     total+=i
# print(f"1から10までの合計:{total}")

# count=10
# while count>0:
#     print(count)
#     count-=1

# 3
import streamlit as st
st.title("streamlitアプリ")
st.header("テキスト入力セクション")

name=st.text_input("あなたの名前を入力してね")

if st.button("挨拶する"):
    if name:
        st.success(f"こんにちは、{name}さん！今日も素晴らしい一日ですね")
    else:
        st.error("名前を入力してください")