# warm-up1
# smartphone={"name":"スーパーフォン","price":65000,"color":"黒","memory":"128GB"}

# (1)
# print(smartphone["price"])

# (2)
# smartphone["camera"]="高性能カメラ搭載"
# print(smartphone["camera"])

# (3)
# smartphone["color"]="青"
# print(smartphone["color"])

# (4)
# del smartphone["memory"]
# print(smartphone)

# (5)
# for key,value in smartphone.items():
    # print(f"{key}:{value}")

# # streamlit warm-up
# import streamlit as st
# st.title("warm-up")
# # 1
# user_name=st.text_input("名前を入力してください")
# st.text(f"{user_name}さん")
# age=st.slider("何歳ですか",
#           0,100)
# st.text(f"{age}歳")
# # 2
# st.text("誕生日はいつ？")
# month=st.slider("月",
#           1,12)
# day=st.slider("日",
#           1,31)
# st.text(f"{user_name}さんの誕生日は{month}月{day}日だね")
# # checkbox=st.checkbox("a")
# # if checkbox:
# #     st.radio("a",
# #              [1,2,3,4,5])
# # 3
# st.radio("好きな色は？",
#          ["赤","青","黄","緑","紫"])
# # 4
# st.selectbox("selectbox",
#              ["りんご","バナナ","オレンジ"])
# # 5
# st.multiselect("multiselect",
#                ["赤","青","黄","緑","紫"])


# importについて
# import math as m
# print(m.pi)
# print(m.sqrt(16))

# from math import pi,sqrt
# print(pi)
# print(sqrt(16))

# import math as m
# print(m.pi)

# from math import sqrt as square_root
# print(square_root(16))

# import emoji
# print(emoji.emojize("Python is::"))

# text_areaについて
import streamlit as st
from datetime import date,timedelta
# user_comment=st.text_area("感想を教えてね!")
# st.write(f"あなたの感想:{user_comment}")

# description=st.text_area(
#     label="自己紹介を書いてみよう",
#     height=150,
#     placeholder="ここに自己紹介を書いてね...",
#     key="self_introduction",
# )
# st.write(f"あなたの自己紹介:{description}")
# selected_date=st.date_input("好きな日付を選んでね")
# st.write(f"選んだ日付:{selected_date}")

# date_inputについて
today=date.today()
next_week=today+timedelta(days=7)
nextmonth=today+timedelta(days=30)
event_date=st.date_input(
    "イベントの日付はいつ？",
    value=next_week,
    min_value=today,
    max_value=nextmonth
)
st.write(f"イベント日:{event_date}")

# time_inputについて
# import streamlit as st
# from datetime import time
# meeting_time=st.time_input("ミーティングは何時から？")
# st.write(f"ミーティング時間:{meeting_time}")
# default_time=time(13,30)
# appointment=st.time_input(
#     "予約時間を選んでね",
#     value=default_time
# )
# st.write(f"予約時間:{appointment}")

# selected_date=st.date_input("日付を選んでね")
# selected_time=st.time_input("時間を選んでね")
# st.write(f"選んだ日時:{selected_date}{selected_time}")

# カラーピッカーについて
# import streamlit as st
# color=st.color_picker("好きな色を選んでね")
# st.write(f"選んだ色:{color}")

# theme_color=st.color_picker(
#     "アプリのテーマカラーを選んでね",
#     value="#00BFFF"
# )
# st.color_picker("あなたの選んだ色",theme_color,disabled=True)