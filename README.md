# Project Summary Generator

## 概要

このプロジェクトは、指定されたディレクトリ内のファイル構造とファイル内容を要約し、プロジェクトの概要を生成するPythonスクリプトです。主にWindowsの開発環境で使用することを想定しています。

## 主な機能

1. ディレクトリ構造の表示
2. ファイル内容の抽出（バイナリファイルを除く）
3. .gitignoreパターンに基づくファイル除外
4. GUIを使用したファイル選択による除外
5. プロジェクト概要の生成（Markdown形式）

## ファイル構成

```
src\
├── __init__.py
├── main.py                 # メインスクリプト
├── summary_generator.py    # プロジェクト概要生成ロジック
├── file_utils.py           # ファイル操作ユーティリティ
├── ignore_patterns.py      # 除外パターン処理
└── gui.py                  # ファイル選択GUI
setup.bat                   # セットアップスクリプト
README.md                   # 本ドキュメント
LICENSE                     # ライセンスファイル
```

## 必要条件

- Windows 10 または 11
- Pythonの組み込みの`os`と`sys`と`fnmatch`と`tkinter`モジュールを使用します。

## インストール手順

1. このリポジトリを任意のディレクトリにクローンまたはダウンロードしてください。
   ```
   git clone https://github.com/thaichi/generate_project_summary.git
   ```
   または、ZIPファイルをダウンロードして任意のディレクトリに展開してください。

2. インストール先ディレクトリ内の `setup.bat` を実行してください。
   - エクスプローラーでインストール先ディレクトリを開きます。
   - `setup.bat` をダブルクリックして実行します。
   - セットアップが完了するとユーザー環境変数にPATHが追加されます。

## 使用方法

1. エクスプローラーで、概要を生成したいプロジェクトのディレクトリに移動します。

2. アドレスバーをクリックし、「cmd」と入力してEnterキーを押します。これにより、現在のディレクトリでコマンドプロンプトが開きます。

3. 開いたコマンドプロンプトで、以下のコマンドを実行します：
   ```
   generate_project_summary
   ```

4. GUIウィンドウが表示されるので、概要から除外したいファイルやディレクトリを選択します。

5. 生成された概要は `[プロジェクト名]_project_summary.md` という名前で現在のディレクトリに保存されます。

## カスタマイズ

- GUIウィンドウで、プロジェクト固有の除外ファイルやディレクトリを選択できます。
- デフォルトの除外パターンは `ignore_patterns.py` で定義されています。必要に応じて編集してください。

## アンインストール

1. スクリプトのインストールディレクトリを手動で削除してください。

2. ユーザー環境変数PATHから、スクリプトのディレクトリへのパスを削除してください：
   - Windowsの検索バーで「環境変数」と入力し、「システム環境変数の編集」を選択
   - 「ユーザー環境変数」セクションで「Path」を選択し、「編集」をクリック
   - スクリプトのディレクトリへのパスを見つけて削除
   - 「OK」をクリックして変更を保存
     
## トラブルシューティング

エラーが発生した場合は、以下を確認してください：

1. Pythonがインストールされていること
2. スクリプトが正しくインストールされていること
3. `setup.bat` が正常に実行されたこと
4. コマンドプロンプトを使用していること

## 貢献

バグ報告や機能リクエストは、GitHubのIssueを通じて行ってください。プルリクエストも歓迎します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。
