import streamlit as st
# ボタンが押されたらsessionstateをリセットするページ
st.title("データリセット")
st.write("下のボタンを押すと、入力したデータをすべてリセットします")
if st.button("全リセット"):
    if st.session_state.user_name != "" or st.session_state.grade != "" or st.session_state.hobby != [] or st.session_state.age != "":
        st.session_state.user_name=""
        st.session_state.grade=""
        st.session_state.hobby=[]
        st.session_state.age=""
        st.success("すべてのデータをリセットしました")
    else:
        st.error("リセットするデータはありません")
if st.button("名前リセット") and st.session_state.user_name != "":
    st.session_state.user_name = ""
    st.success("名前のデータをリセットしました")
else:
    st.error("名前はリセットされているか、保存されていません")

if st.button("学年リセット") and st.session_state.grade != "":
    st.session_state.grade = ""
    st.success("学年のデータをリセットしました")
else:
    st.error("学年はリセットされているか、保存されていません")

if st.button("趣味リセット") and st.session_state.hobby != []:
    st.session_state.hobby = []
    st.success("趣味をのデータをリセットしました")
else:
    st.error("趣味はリセットされているか、保存されていません")

if st.button("年齢をリセット") and st.session_state.age != "":
    st.session_state.age = ""
    st.success("年齢のデータをリセットしました")
else:
    st.error("年齢のデータはリセットされているか、保存されていません")

if st.session_state.user_name == "" and st.session_state.grade == "" and st.session_state.hobby == "" and st.session_state.age == "":
    st.error("リセットするデータはありません")
    st.write("メインページでデータを入力,保存してください")