import os
from pathlib import Path

proced_title = ""
dirpath = Path.cwd()/"AizuAtCo"


def replace_space_underbar(row_title: str):
    global proced_title
    raw_title = row_title
    proced_title = raw_title.replace(" ", "_")
    

def make_dir_and_file(title :str):
    os.mkdir(f"{dirpath/title}")
    with open(f"{dirpath/title}/solve1.py","w") as f:
        pass

if __name__ == "__main__":
    replace_space_underbar(input("titleを入力 : "))
    make_dir_and_file(proced_title)
    print(f"{proced_title}が作成されました。")