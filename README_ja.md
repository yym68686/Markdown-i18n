# マークダウン-i18n

[英文](README.md) | [中文](README_CN.md) | [繁体中文](README_zh-hant.md) ｜ [日本語](README_ja.md) | [한국어](README_ko.md)

毎回プロジェクトドキュメントを更新するたびに、二つ以上の言語のドキュメントを同時に管理するのは本当に苦痛なので、複数言語の README ドキュメントを更新するためのスクリプトを書きました。自分の母語でドキュメントを書き、同時にどの言語にも翻訳でき、ドキュメントのフォーマットを変えずに維持できることを望んでいます。Markdown-i18n はこれらの痛点を解決しました。

## 特性

- 支持増量翻訳。のみ翻訳された部分、未翻訳部分は繰り返し翻訳されません。翻訳効率を大幅に向上させる。トークン消費を大幅に削減する。
- 任意の markdown ドキュメントに i18n サポートを追加し、任意の言語から任意の言語への翻訳をサポートします。
- 完美遵循原文件的格式。
- 同時に翻訳が自然で正確であることを保証します。
- 高効率な翻訳。

## 使用指南

1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

2. 開始翻訳

方法一：新しい python ファイルを作成する

```python
import os
from translate_md import translate
from parse_markdown import check_markdown_parse

api_key = os.getenv("API")       # OpenAI APIキー
api_url = os.getenv("API_URL")   # OpenAI API URL
engine = "gpt-4o"                # 言語モデル

input_file_path = "README-zh.md" # 原ファイルパス
output_file_path = "README.md"   # 出力ファイルパス
language = "English"             # 目標言語
check_markdown_parse(input_file_path) # markdownファイルが正しく解析されているか確認する。正しく解析されていれば翻訳可能。エラーが出た場合は作者に修正を依頼する。このステップは必須ではなく、翻訳のフォーマットの正確性を保証するためのもの。
translate(input_file_path, output_file_path, language, api_key, api_url, engine) # 原markdownファイルを目標言語に翻訳し、出力ファイルに保存する
```

方法二：使用仓库里现成的脚本

直接変更 translate_md.py ファイルの設定を行い、スクリプトを実行するだけです。

```python
input_file_path = "README_CN.md" # 原ファイルパス
output_file_path = "README.md"   # 出力ファイルパス
language = "English"             # 目標言語
api_key = os.getenv("API")       # OpenAI APIキー
api_url = os.getenv("API_URL")   # OpenAI API URL デフォルトは "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # 言語モデル
```