# Markdown-i18n

[英文](README.md) | [中文](README_CN.md) | [繁體中文](README_zh-hant.md) ｜ [日本語](README_ja.md) | [한국어](README_ko.md)

每次更新項目文檔都要同時維護兩份或者多種語言的文檔實在過於痛苦了，於是我寫了個腳本來幫我更新多語言 README 文檔。我希望可以用自己的母語寫文檔，並能同時翻譯到任何語言，並且保持文檔格式不變。Markdown-i18n 解決了這些痛點。

## 特性

- 給任何 markdown 文件添加 i18n 支援，支援從任何語言翻譯到任何語言。
- 完美遵循原文件的格式。
- 同時保證翻譯地道、準確。
- 高效翻譯。

## 使用指南

1. 安裝依賴

```bash
pip install -r requirements.txt
```

2. 開始翻譯

方法一：創建一個新的 python 文件

```python
import os
from translate_md import translate
from parse_markdown import check_markdown_parse

api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL
engine = "gpt-4o"                # 語言模型

input_file_path = "README-zh.md" # 原文件路徑
output_file_path = "README.md"   # 輸出文件路徑
language = "English"             # 目標語言
check_markdown_parse(input_file_path) # 檢查 markdown 文件是否解析正確，解析正確就可以翻譯，如果報錯需要聯繫作者修復。這一步不是必要的，只是為了保證翻譯的格式準確性。
translate(input_file_path, output_file_path, language, api_key, api_url, engine) # 翻譯原markdown文件到目標語言並保存到輸出文件
```

方法二：使用倉庫裡現成的腳本

直接修改 translate_md.py 文件中的配置，然後運行腳本即可。

```python
input_file_path = "README_CN.md" # 原文件路径
output_file_path = "README.md"   # 輸出文件路徑
language = "English"             # 目標語言
api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL 默認是 "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # 語言模型
```