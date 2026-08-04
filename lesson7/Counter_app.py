# import streamlit as st

# st.title("カウンターアプリ")
# if "count" not in st.session_state:
#     st.session_state.count=0

# if st.button("カウントアップ"):
#     st.session_state.count+=1
# if st.button("カウントダウン"):
#     st.session_state.count-=1
# if st.button("カウントリセット"):
#     st.session_state.count=0

# st.markdown("___")
# st.subheader(f"現在のカウント:{st.session_state.count}")

# import streamlit as st

# st.title("シンプル電卓アプリ 🧮")

# # 1. ユーザーが数字を入力するエリア（初期値は0）
# num1 = st.number_input("1つ目の数字を入力してください", value=0)
# num2 = st.number_input("2つ目の数字を入力してください", value=0)

# # 2. 計算結果を保存する箱をセッション状態に用意
# if "calc_result" not in st.session_state:
#     st.session_state.calc_result = 0

# # 3. カウンターアプリのボタン構造を活かして、四則演算のボタンを配置
# st.write("計算方法を選んでください：")

# # st.columnsを使うと、ボタンを横一列に綺麗に並べることができます
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     if st.button("➕ 足し算"):
#         st.session_state.calc_result = num1 + num2

# with col2:
#     if st.button("➖ 引き算"):
#         st.session_state.calc_result = num1 - num2

# with col3:
#     if st.button("✖️ 掛け算"):
#         st.session_state.calc_result = num1 * num2

# with col4:
#     if st.button("➗ 割り算"):
#         # 0で割ろうとしたときのバグ（エラー）を防ぐセーフティ
#         if num2 == 0:
#             st.session_state.calc_result = "エラー（0で割ることはできません）"
#         else:
#             st.session_state.calc_result = num1 / num2

# st.markdown("---")

# # 4. 計算結果を表示するエリア
# st.subheader("📊 計算結果")
# st.header(f"{st.session_state.calc_result}")

import streamlit as st

st.title("便利ツールアプリ 🛠️")

# タブを2つ作成
tab1, tab2 = st.tabs(["🔢 カウンター", "🧮 電卓"])

# ──────────────────────────────────────────────────
#  タブ1：カウンターアプリ
# ──────────────────────────────────────────────────
with tab1:
    st.header("カウンターアプリ")
    
    if "count" not in st.session_state:
        st.session_state.count = 0

    if st.button("カウントアップ"):
        st.session_state.count += 1
    if st.button("カウントダウン"):
        st.session_state.count -= 1
    if st.button("カウントリセット"):
        st.session_state.count = 0

    st.markdown("___")
    st.subheader(f"現在のカウント: {st.session_state.count}")

# ──────────────────────────────────────────────────
#  タブ2：電卓アプリ
# ──────────────────────────────────────────────────
with tab2:
    st.header("シンプル電卓アプリ")
    
    # 【変更点】valueを「0.0」にしつつ、stepを「1」に設定します
    # これにより、ボタンでの増減は1ずつ（整数っぽく）、直接入力は小数が可能になります
    num1 = st.number_input("1つ目の数字を入力してください", value=0.0, step=1.0, key="calc_num1")
    num2 = st.number_input("2つ目の数字を入力してください", value=0.0, step=1.0, key="calc_num2")

    if "calc_result" not in st.session_state:
        st.session_state.calc_result = 0.0

    st.write("計算方法を選んでください：")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("➕ 足し算"):
            st.session_state.calc_result = num1 + num2
    with col2:
        if st.button("➖ 引き算"):
            st.session_state.calc_result = num1 - num2
    with col3:
        if st.button("✖️ 掛け算"):
            st.session_state.calc_result = num1 * num2
    with col4:
        if st.button("➗ 割り算"):
            if num2 == 0:
                st.session_state.calc_result = "エラー（0で割ることはできません）"
            else:
                st.session_state.calc_result = num1 / num2

    st.markdown("---")
    st.subheader("📊 計算結果")
    
    # 結果の表示（エラー文字のときはそのまま、数字のときは綺麗に表示）
    result = st.session_state.calc_result
    if isinstance(result, str):
        st.error(result)
    else:
        st.header(f"{result}")
