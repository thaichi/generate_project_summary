import os
import sys

# スクリプトのディレクトリをモジュール検索パスに追加
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from summary_generator import generate_project_summary

if __name__ == '__main__':
    project_directory = os.getcwd()  # 現在のディレクトリをデフォルトとして使用
    generate_project_summary(project_directory)
    print(f"Project summary generated: {os.path.join(project_directory, os.path.basename(project_directory) + '_project_summary.txt')}")