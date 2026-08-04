
import streamlit as st
# 1
st.title("warm-up")
st.slider("slider",
          0,100)
# 2
st.checkbox("checkbox")

# 3
st.radio("radio",
         ["赤","青","黄","緑"])
# 4
st.selectbox("selectbox",
             ["りんご","バナナ","オレンジ"])
# 5
st.multiselect("multiselect",
               ["赤","青","黄","緑","紫"])