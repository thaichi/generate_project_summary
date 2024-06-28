# Scripts Project Summary Generator

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
generate_project_summary\
├── __init__.py
├── main.py                 # メインスクリプト
├── summary_generator.py    # プロジェクト概要生成ロジック
├── file_utils.py           # ファイル操作ユーティリティ
├── ignore_patterns.py      # 除外パターン処理
└── gui.py                  # ファイル選択GUI
setup.bat                   # セットアップスクリプト
uninstall.bat               # アンインストールスクリプト
README.md                   # 本ドキュメント
LICENSE                     # ライセンスファイル
```

## 必要条件

- Windows 10 または 11
- Python 3.6以上

## インストール手順

1. このリポジトリを任意のディレクトリにクローンまたはダウンロードしてください。
   ```
   git clone https://github.com/thaichi/generate_project_summary.git
   ```
   または、ZIPファイルをダウンロードして任意のディレクトリに展開してください。

2. インストール先ディレクトリ内の `setup.bat` を実行してください。
   - エクスプローラーでインストール先ディレクトリを開きます。
   - `setup.bat` をダブルクリックして実行します。

3. セットアップが完了したら、コマンドプロンプトを再起動してください。

注意：setup.batは管理者権限なしで実行できます。ただし、一部の環境設定によっては管理者権限が必要な場合があります。

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

1. インストール先ディレクトリ内の `uninstall.bat` を実行してください。
   - エクスプローラーでインストール先ディレクトリを開きます。
   - `uninstall.bat` をダブルクリックして実行します。

2. アンインストールが完了したら、コマンドプロンプトを再起動してください。

注意：
- uninstall.batは管理者権限なしで実行できます。
- アンインストールスクリプトは、generate_project_summary関連のファイルとディレクトリを削除します。

## トラブルシューティング

エラーが発生した場合は、以下を確認してください：

1. Pythonがインストールされていること（Python 3.6以上を推奨）
2. スクリプトが正しくインストールされていること
3. `setup.bat` が正常に実行されたこと
4. 新しいコマンドプロンプトを開いて実行していること（PATH環境変数の更新を反映するため）

環境によっては、setup.batやuninstall.batの実行に管理者権限が必要な場合があります。その場合は、ファイルを右クリックし、「管理者として実行」を選択してください。

## 注意事項

- このスクリプトは主にテキストファイルの内容を抽出します。バイナリファイルは除外されます。
- 大規模なプロジェクトの場合、概要の生成に時間がかかる可能性があります。
- スクリプトを実行する前に、重要なデータのバックアップを取ることをお勧めします。

## 貢献

バグ報告や機能リクエストは、GitHubのIssueを通じて行ってください。プルリクエストも歓迎します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。