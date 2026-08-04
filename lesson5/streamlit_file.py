import streamlit as st
# uploaded_file=st.file_uploader("ファイルをアップロードしてね")

# if uploaded_file is not None:
#     st.success("ファイルがアップロードされたよ!")
#     st.write("ファイル名:",uploaded_file.name)
#     st.write("ファイルタイプ:",uploaded_file.type)
#     st.write("ファイルサイズ",uploaded_file.size,"バイト")

# 実装例1
# st.title("ファイルアップロードのデモ")

# text_file=st.file_uploader(
#     "テキストファイルをアップロードしてね",
#     type=["txt","csv"],
#     help="テキストファイル(.txt)かCSVファイル(.csv)だけだよ"
# )
# if text_file is not None:
#     st.success(f"テキストファイル「{text_file.name}」がアップロードされたよ!")
#     text_data=text_file.getvalue().decode("utf-8")
#     st.write("テキスト内容:")
#     st.text_area("ファイルの内容",text_data,height=150)

# 実装例2
# multiple_files=st.file_uploader(
#     "複数のファイルをアップロードしてね",
#     accept_multiple_files=True
# )

# if multiple_files:
#     st.write(f"{len(multiple_files)}個のファイルがアップロードされたよ")
#     for file in multiple_files:
#         st.write(f"-{file.name}({file.size}バイト)")

# ファイルダウンロード機能
# text_contents="""これはダウンロードできるテキストファイルだよ。
# 複数行にわたるテキストも大丈夫!
# Streamlitでファイルダウンロード機能を使ってみよう!"""

# st.download_button(
#     label="テキストファイルをダウンロード",
#     data=text_contents,
#     file_name="sample_text.txt",
#     mime="text/plain"    
#     )

# シンプルなメモ帳アプリ
# st.title("シンプルメモ帳")

# memo_text=st.text_area("メモを入力してね",height=200)

# file_name=st.text_input("保存するファイル名","memo.txt")

# if memo_text:
#     st.download_button(
#         label="メモをダウンロード",
#         data=memo_text,
#         file_name=file_name,
#         mime="text/plain"
#     )
# else:
#     st.info("メモを入力するとダウンロードボタンが表示されるよ")

# 画像ファイルの表示
# st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png"
# ,
# caption="Streamlitロゴ")

# st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png"
# ,
# caption="幅を300pxに指定"
# , width=300)

# 画像のアップロードと表示
from PIL import Image

# st.title("画像アップロードと表示")

# uploaded_image=st.file_uploader("画像をアップロードしてね",
#                                 type=["jpg","jpeg","png"])

# if uploaded_image is not None:
#     st.write(f"ファイル名:{uploaded_image.name}")

#     image=Image.open(uploaded_image)
#     st.image(image,caption=uploaded_image.name,use_column_width=True)

# 総合演習アプリ
st.title("テキストエディタ")

memo_text=st.text_area("テキストを入力してね",height=200)

file_name=st.text_input("保存するファイル名","text.txt")
if memo_text:
    st.download_button(
        label="テキストをファイルとしてダウンロード",
        data=memo_text,
        file_name=file_name,
        mime="text/plain"
    )
else:
    st.info("テキストを入力するとダウンロードボタンが表示されるよ")


uploaded_image=st.file_uploader("画像をアップロードすることもできるよ",
                                type=["jpg","jpeg","png"])
if uploaded_image is not None:
    st.write(f"ファイル名:{uploaded_image.name}")

    image=Image.open(uploaded_image)
    st.image(image,caption=uploaded_image.name,use_column_width=True)
