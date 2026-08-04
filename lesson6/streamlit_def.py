import streamlit as st

# def get_sound(animal):
#     if animal=="dog":
#         return "ワンワン"
#     if animal=="cat":
#         return "ニャーニャー"
#     else:
#         return "その動物はデータがありません"
    
# st.title("動物の鳴き声アプリ")
# selected=st.selectbox("動物を選んでね",["dog","cat","bird"])
# if st.button("鳴き声を聞く"):
#     st.write(f"{get_sound(selected)}")

# columns
# col1,col2,col3=st.columns(3)
# with col1:
#     st.write("左")
# with col2:
#     st.write("中")
# with col3:
#     st.write("右")

# tabs
tab1,tab2=st.tabs(["情報","設定"])
with tab1:
    st.write("アプリ情報")
with tab2:
    st.slider("設定値",0,100)