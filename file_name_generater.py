import shutil
import subprocess
from pathlib import Path

dirpath = Path.cwd() / "algorithms"


def to_dirname(raw_title: str) -> str:
    return raw_title.strip().replace(" ", "_")


def make_dir_and_file(category: str, title: str) -> Path:
    target_dir = dirpath / category / title
    target_dir.mkdir(parents=True, exist_ok=True)   # 既にあってもエラーにしない
    solve_file = target_dir / "solve1.py"
    solve_file.touch(exist_ok=True)                 # 空ファイル作成
    return solve_file


def open_in_vscode(file: Path) -> None:
    code_cmd = shutil.which("code")  # Windowsでは code.cmd も見つけてくれる
    if code_cmd is None:
        print("code コマンドが見つかりません。VS Codeで PATH に登録してください。")
        return
    # -r: 今開いているウィンドウで開く / -g: ファイルを開いてカーソルを置く
    subprocess.run([code_cmd, "-r", "-g", str(file)])


if __name__ == "__main__":
    categories = sorted(d.name for d in dirpath.iterdir() if d.is_dir())
    print("既存のアルゴリズム : " + ", ".join(categories))
    category = to_dirname(input("アルゴリズムを入力 : "))
    title = to_dirname(input("titleを入力 : "))
    solve_file = make_dir_and_file(category, title)
    print(f"{title}が作成されました。")
    open_in_vscode(solve_file)