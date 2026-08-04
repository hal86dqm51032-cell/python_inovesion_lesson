# list
# foods=["ラーメン","カレー","寿司"]
# foods.append("ハンバーガー")
# foods.append("うどん")
# foods.remove("カレー")
# for food in foods:
#     print(food)

# dictionary
dictionary={"北海道":"ジャガイモ",
            "青森":"りんご",
            "宮城":"牛タン",
            "京都":"八つ橋",
            "沖縄":"シークワーサー",}
dictionary["大阪"]="たこ焼き"
dictionary["福岡"]="明太子"
for key,value in dictionary.items():
    print(f"{key}の特産品は{value}です")