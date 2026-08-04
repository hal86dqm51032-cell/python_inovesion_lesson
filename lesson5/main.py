# 1
# with open('sample.txt','r',encoding='utf-8') as file:
#     content=file.read()
#     print('---read()の結果---')
#     print(content)

# 2
# with open("output1.text","w",encoding="utf-8") as file:
#     file.write("こんにちは,python!\n")
#     file.write("ファイル操作を学んでいます")

# lines=["1行目:pythonでファイル操作\n",
#        "2行目:とても便利です\n",
#        "3行目:試してみましょう!"]

# with open("output2.txt","w",encoding="utf-8") as file:
#     file.writelines(lines)

# 3
# with open("input.txt","r",encoding="utf-8") as input_file:
#     content=input_file.read()
#     processed_content=content.upper()
#     with open("uppercase.txt","w",encoding="utf-8") as output_file:
#         output_file.write(processed_content)

# 4
with open("memo.txt","w",encoding="utf-8") as file:
    Content=input()
    file.write("今日のメモ\n")
    file.write("Pythonでファイル操作を勉強しました\n")
    file.write(Content)
with open("memo.txt","r",encoding="utf-8") as read_file:
    content=read_file.read()
    print(content)