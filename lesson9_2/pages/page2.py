import streamlit as st
# ボタンが押されたらsessionstateをリセットするページ
st.title("データリセット")
st.write("下のボタンを押すと、入力したデータをすべてリセットします")
if st.button("リセット"):
    if st.session_state.user_name != "" or st.session_state.grade != "" or st.session_state.hobby != [] or st.session_state.age != "":
        st.session_state.user_name=""
        st.session_state.grade=""
        st.session_state.hobby=[]
        st.session_state.age=""
    else:
        st.error("リセットするデータはありません")
else:
    st.error("リセットボタンが押されていません")