## 1スライダー

# import streamlit as st

# age=st.slider("年齢を選択",0,100,25)
# st.write(f"選択された年齢:{age}歳")

# price_range=st.slider(
#     "価格帯を選択",
#     0,10000,(2000,5000)
# )

# st.write(f"選択された価格帯:{price_range[0]}円から{price_range[1]}円")

# step_value=st.slider(
#     "5刻みで選択",
#     0,100,25,step=5
# )

# st.write(f"選択された値{step_value}")

# # 2チェックボックス
# import streamlit as st
# show_details=st.checkbox("詳細を表示する")

# if show_details:
#     st.write("ここに詳細情報を表示します")
#     st.write("さらに多くの情報...")
# else:
#     st.write("チェックボックスをオンにすると詳細が表示されるよ")


# # 複数のチェックボックス
# st.write("###好きな果物を選んでね")
# apple=st.checkbox("りんご")
# banana=st.checkbox("バナナ")
# orange=st.checkbox("オレンジ")

# selected_fruits=[]
# if apple:
#     selected_fruits.append("りんご")
# if banana:
#     selected_fruits.append("バナナ")
# if orange:
#     selected_fruits.append("オレンジ")

# if selected_fruits:
#     st.write(f"選んだ果物:{','.join(selected_fruits)}")
# else:
#     st.write("まだ何も選んでないよ")

# ラジオボタン
# import streamlit as st

# option=st.radio(
#     "好きな色を選んでね",
#     ["赤","青","緑","黄","黒","白","紫","橙","桃","水","灰","茶","紺","金","銀"]
# )
# st.write(f"あなたが選んだ色:{option}")

# # 選択リスト:ドロップダウン
# import streamlit as st
# option=st.selectbox(
#     "好きな果物を選んでね",
#     ["りんご","バナナ","オレンジ","ぶどう","メロン"]
# )

# st.write(f"あんたが選んだ果物:{option}")

# fruits_dict={
#     "りんご":"🍎",
#     "バナナ":"🍌",
#     "オレンジ":"🍊",
#     "ぶどう":"🍇",
# }
# fruit=st.selectbox("フルーツを選択",list(fruits_dict.keys()))
# st.write(f"選んだフルーツの絵文字:{fruit}")

import streamlit as st

options=st.multiselect(
    "好きな色を選んでね(複数選択可)",
    ["赤","青","緑","黄","紫","橙"]
)
if options:
    st.write(f"あなたが選んだ色:{','.join(options)}✨")
else:
    st.write("色を選んでね👆")