# Markdown-i18n

给任何 markdown 文档添加 i18n 支持，支持从任何语言翻译到任何语言。

[英文](README.md) | [中文](README_CN.md)

## 使用指南

安装依赖

```bash
pip install -r requirements.txt
```

修改 translate_md.py 文件中的配置

```python
input_file_path = "README_CN.md" # 原文件路径
output_file_path = "README.md"   # 输出文件路径
language = "English"             # 目标语言
api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL 默认是 "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # 语言模型
```