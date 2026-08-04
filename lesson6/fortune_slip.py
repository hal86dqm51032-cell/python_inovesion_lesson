import streamlit as st
import random

st.title("今日の運勢占い 🔮")

# 1. 各種データの初期化
if "draw_count" not in st.session_state:
    st.session_state.draw_count = 0
if "last_fortune" not in st.session_state:
    st.session_state.last_fortune = None  # 前回の結果を記憶する箱

def draw_omikuji():
    st.session_state.draw_count += 1
    
    # 確率の設定用データ
    fortunes = ["????","大吉", "中吉", "小吉", "凶","大凶"]
    weights = [1,9, 30, 40, 15,5]  # 大吉10%, 中吉40%, 小吉40%, 凶10%
    
    # 【確率版】まずは指定した確率で1回おみくじを引く
    fortune = random.choices(fortunes, k=1, weights=weights)[0]
    
    # 【重複防止】「前回の結果と同じである間」は、違うのが出るまで引き直し続ける
    while fortune == st.session_state.last_fortune:
        fortune = random.choices(fortunes, k=1, weights=weights)[0]
        
    st.header(f"運勢: **{fortune}**")
    
    if fortune == "大吉":
        st.balloons()
        st.success("良い日！")
    elif fortune == "中吉":
        st.info("いいことあるかも！")
    elif fortune == "小吉":
        st.warning("少し注意。")
    elif fortune=="????":
        st.balloons()
        st.success("良く当てれたね")
    elif fortune=="凶":
        st.error("今日は慎重に。")
    else:
        st.error("今日は気を付けた方がいいよ...")
        
    # 今回の結果を「前回の結果」として保存
    st.session_state.last_fortune = fortune

if st.button("おみくじを引く！"):
    draw_omikuji()

st.write(f"---")
st.write(f"📊 これまでにおみくじを引いた回数: **{st.session_state.draw_count}回**")
