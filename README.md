# Markdown-i18n

[English](README.md) | [Chinese](README_CN.md) | [Traditional Chinese](README_zh-hant.md) | [Japanese](README_ja.md) | [Korean](README_ko.md)

Updating project documentation each time and maintaining two or more versions in different languages is really too painful, so I wrote a script to help me update multilingual README documents. I hope to write documentation in my native language and translate it into any language while keeping the document format unchanged. Markdown-i18n solved these pain points.

## Features

- Add i18n support to any markdown document, supporting translation from any language to any language.
- Perfectly follow the format of the original file.
- At the same time, ensure the translation is authentic and accurate.
- Efficient translation.

## User Guide

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Start translating

Method One: Create a new python file

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
check_markdown_parse(input_file_path) # Check if the markdown file is parsed correctly; if parsed correctly, it can be translated. If there is an error, contact the author to fix it. This step is not necessary, just to ensure the accuracy of the translation format.
translate(input_file_path, output_file_path, language, api_key, api_url, engine) # Translate the original markdown file to the target language and save it to the output file
```

Method Two: Using the pre-existing scripts in the repository

Directly modify the configuration in the translate_md.py file, and then run the script.

```python
input_file_path = "README_CN.md" # Original file path
output_file_path = "README.md"   # Output file path
language = "English"             # Target language
api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL default is "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # Language model
```