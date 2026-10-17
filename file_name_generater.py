import shutil
import subprocess
from pathlib import Path

dirpath = Path.cwd() / "AizuAtCo"


def to_dirname(raw_title: str) -> str:
    return raw_title.strip().replace(" ", "_")


def make_dir_and_file(title: str) -> Path:
    target_dir = dirpath / title
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
    title = to_dirname(input("titleを入力 : "))
    solve_file = make_dir_and_file(title)
    print(f"{title}が作成されました。")
    open_in_vscode(solve_file)