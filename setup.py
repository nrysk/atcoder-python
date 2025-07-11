#!.venv/bin/python3

import pathlib
import shutil
import subprocess

WORKSPACE_PATH = pathlib.Path(__file__).parent
URL_FORMAT = "https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{problem_id}"

contest_id = input("Enter the contest ID (e.g abc001): \n").strip()
problem_id = input("Enter the problem ID (e.g a): \n").strip()

contest_dir = WORKSPACE_PATH / contest_id
problem_dir = WORKSPACE_PATH / contest_id / problem_id
url = URL_FORMAT.format(contest_id=contest_id, problem_id=problem_id)

flags = {
    "exist_contest_dir": contest_dir.exists(),
    "exist_problem_dir": problem_dir.exists(),
    "exist_problem_file": (problem_dir / "main.py").exists(),
}

# コンテストディレクトリの作成
try:
    problem_dir.mkdir(parents=True, exist_ok=False)
    (problem_dir / "main.py").touch()
    print(f"Created directory {problem_dir} and main.py file.")
except FileExistsError:
    print(f"Directory {problem_dir} already exists. Skipping creation.")

# テストケースのダウンロード
# 対応する問題が存在しない場合はロールバック処理を行う
try:
    subprocess.run(["oj", "d", url], cwd=problem_dir, check=True)
    print(f"Downloaded problem data from {url}.")
except subprocess.CalledProcessError:
    print(f"Failed to download problem data from {url}.")
    if not flags["exist_contest_dir"]:
        shutil.rmtree(contest_dir)
    elif not flags["exist_problem_dir"]:
        shutil.rmtree(problem_dir)
    elif not flags["exist_problem_file"]:
        (problem_dir / "main.py").unlink()
