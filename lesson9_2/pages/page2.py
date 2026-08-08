import streamlit as st
# ボタンが押されたらsessionstateをリセットするページ
st.title("データリセット")
st.write("下のボタンを押すと、入力したデータをすべてリセットします")
if st.button("リセット") and (st.session_state.user_name != "" or st.session_state.grade != "" or st.session_state.hobby != []):
    st.session_state.user_name=""
    st.session_state.grade=""
    st.session_state.hobby=[]
else:
    st.error("リセットするデータはありません")