import streamlit as st
st.title("ユーザー情報表示ページ")
if "user_name" in st.session_state and st.session_state.user_name:
    st.success(f"こんにちは、{st.session_state.user_name}さん")
else:
    st.error("ユーザー名が設定されていません")
    st.write("メインページで名前を入力してください")

if "grade" in st.session_state and st.session_state.grade:
    st.success(f"あなたの学年は{st.session_state.grade}ですね!")
else:
    st.error("学年が設定されていません")
    st.write("メインページで学年を選択してください")

if "hobby" in st.session_state and st.session_state.hobby:
    st.success(f"あなたは{st.session_state.hobby}が好きなんですね!")
else:
    st.error("趣味が1つも選択されていません")
    st.write("メインページで趣味を１つ以上選択してください")

if "user_name" in st.session_state and st.session_state.user_name and "grade" in st.session_state and st.session_state.grade and "hobby" in st.session_state and st.session_state.hobby:
    st.balloons()
    # もしすべてのsession_stateが入力/選択されたら風船を飛ばす