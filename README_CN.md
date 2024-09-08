# Markdown-i18n

[英文](README.md) | [中文](README_CN.md)

每次更新项目文档都要同时维护两份或者多种语言的文档实在过于痛苦了，于是我写了个脚本来帮我更新多语言 README 文档。我希望可以用自己的母语写文档，并能同时翻译到任何语言，并且保持文档格式不变。Markdown-i18n 解决了这些痛点。

## 特性

- 给任何 markdown 文档添加 i18n 支持，支持从任何语言翻译到任何语言。
- 完美遵循原文件的格式。
- 同时保证翻译地道、准确。
- 高效翻译。

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