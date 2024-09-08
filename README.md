# Markdown-i18n

Add i18n support to any markdown document, supporting translation from any language to any language.

[English](README.md) | [Chinese](README_CN.md)

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