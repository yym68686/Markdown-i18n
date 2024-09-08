# Markdown-i18n

[English](README.md) | [Chinese](README_CN.md)

Every time I update the project documentation, maintaining two or more versions in different languages is really painful. So, I wrote a script to help me update multi-language README documents. I hope to write the documentation in my native language and translate it into any other language while keeping the document format unchanged. Markdown-i18n solves these pain points.

## Features

- Add i18n support to any markdown document, supporting translation from any language to any language.
- Perfectly follow the format of the original document.
- At the same time, ensure the translation is authentic and accurate.
- Efficient translation.

## User Guide

Install dependencies

```bash
pip install -r requirements.txt
```

Modify the configuration in the translate_md.py file

```python
input_file_path = "README_CN.md" # Original file path
output_file_path = "README.md"   # Output file path
language = "English"             # Target language
api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL default is "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # Language model
```