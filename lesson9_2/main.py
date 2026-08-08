import streamlit as st
st.title("ユーザー情報入力")

if "user_name" not in st.session_state:
    st.session_state.user_name = ""
 
if "grade" not in st.session_state:
    st.session_state.grade=""

if "hobby" not in st.session_state:
    st.session_state.hobby=[]

if "age" not in st.session_state:
    st.session_state.age=""

name=st.text_input("あなたの名前を入力してください")
if st.button("名前を保存"):
    st.session_state.user_name = name
    st.success("名前を保存しました")
st.write(f"現在保存されている名前:{st.session_state.user_name}")

grade=st.selectbox("学年を選択して下さい",["小5","小６","中１","中２","中３"])
if st.button("学年を保存"):
    st.session_state.grade=grade
    st.success("学年を保存しました")
st.write(f"現在保存されている学年:{st.session_state.grade}")

hobby=st.multiselect("趣味を選択してください",["読書","スポーツ","ゲーム","音楽","絵画","その他"])
if st.button("趣味を保存"):
    st.session_state.hobby=hobby
    st.success("趣味を保存しました")
st.write(f"現在保存されている趣味:{st.session_state.hobby}")

age=st.slider("年齢をスライダーで選択してください",1,100)
if st.button("年齢を保存"):
    st.session_state.age=age
    st.success("年齢を保存しました")
st.write(f"現在保存されている年齢:{age}")
