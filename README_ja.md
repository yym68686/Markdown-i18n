# Markdown-i18n

[英文](README.md) | [中文](README_CN.md) | [繁体中文](README_zh-hant.md) ｜ [日本語](README_ja.md) | [한국어](README_ko.md)

毎回プロジェクトのドキュメントを更新するたびに、2つ以上の言語でドキュメントを同時に維持するのは本当に苦痛なので、スクリプトを書いて多言語の README ドキュメントを更新するのを手伝ってもらいました。自分の母国語でドキュメントを書き、同時にどの言語にも翻訳でき、ドキュメントのフォーマットを維持できることを望んでいます。Markdown-i18n はこれらの痛点を解決しました。

## Characteristics

- 任意の markdown ドキュメントに i18n サポートを追加し、任意の言語から任意の言語への翻訳をサポートします。
- 完璧に元のファイルの形式に従う。
- Ensure the translation is idiomatic and accurate.
- Efficient translation.

## ユーザーガイド

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. 開始翻訳

方法一：新しい python ファイルを作成する

```python
import os
from translate_md import translate
from parse_markdown import check_markdown_parse

api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL
engine = "gpt-4o"                # Language model

input_file_path = "README-zh.md" # Original file path
output_file_path = "README.md"   # Output file path
language = "English"             # Target language
check_markdown_parse(input_file_path) # Check if the markdown file parses correctly. If it parses correctly, it can be translated. If there is an error, contact the author for a fix. This step is not necessary, just to ensure the accuracy of the translation format.
translate(input_file_path, output_file_path, language, api_key, api_url, engine) # Translate the original markdown file to the target language and save it to the output file
```

Method 2: Using pre-existing scripts in the repository

直接 translate_md.py ファイルの設定を変更し、スクリプトを実行するだけです。

```python
input_file_path = "README_CN.md" # 原ファイルパス
output_file_path = "README.md"   # 出力ファイルパス
language = "English"             # 目標言語
api_key = os.getenv("API")       # OpenAI APIキー
api_url = os.getenv("API_URL")   # OpenAI API URL デフォルトは "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # 言語モデル
```