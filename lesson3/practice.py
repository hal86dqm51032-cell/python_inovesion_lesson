import streamlit as st

if "character_name" not in st.session_state:
    st.session_state.character_name="キャラクター"
character_name=st.text_input(
    "キャラクターの名前を入力して下さい"
)
st.write(f"キャラクターの名前:{character_name}")
level=st.slider(f"{character_name}のレベル",
          1,100)
st.write(f"{character_name}のレベル:{level}")
special=st.checkbox(
    "特殊能力を持っている"
)
if special:
    special_select=st.radio(
                "どの特殊能力ですか？",
                ["戦闘開始時HPアップ",
                 "戦闘開始時MPアップ",
                 "戦闘開始時攻撃力アップ",
                 "戦闘開始時防御力アップ",
                 "戦闘開始時素早さアップ",
                 "戦闘開始時一度死んでも生き返る効果付与",
                 "行動開始時、たまに会心率アップ",
                 "みかわしされない"]
                )
    if special_select:
        st.write(f"{character_name}の特殊能力:{special_select}")
    
else:
    st.write("特殊能力を持っていません")
occupation=st.radio(
    f"{character_name}の職業を選んでください",
    ["戦士","魔法使い","盗賊"]
)
warrior_skill={
    20:"火炎切り",
    40:"回転切り",
    60:"さみだれ切り",
    80:"氷結切り",
    100:"雷回転切り",
}
wizard_skill={
    20:"火の呪文",
    40:"回復呪文",
    60:"氷の呪文",
    80:"雷の呪文",
    100:"火炎の呪文"
}
thief_skill={
    20:"盗む",
    40:"ブーメラン投げ"
}
st.write(f"{character_name}の職業:{occupation}")
birthplace=st.selectbox(
    f"{character_name}の出身地を選んでください",
    ["砂漠","森","雪国","都市"]
)
st.write(f"{character_name}の出身地:{birthplace}")
weapons=st.multiselect(
    f"{character_name}の得意武器を選んでください",
    ["剣","弓","杖","ナイフ"]
)
st.write(f"{character_name}の得意武器")
for weapon in weapons:
    st.write(weapon)
