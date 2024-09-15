# 마크다운-i18n

[영어](README.md) | [중국어](README_CN.md) | [번체 중국어](README_zh-hant.md) ｜ [일본어](README_ja.md) | [한국어](README_ko.md)

매번 프로젝트 문서를 업데이트할 때마다 두 개 이상의 언어로 된 문서를 동시에 유지하는 것은 정말 고통스러웠습니다. 그래서 여러 언어로 된 README 문서를 업데이트하는 데 도움을 주기 위해 스크립트를 작성했습니다. 저는 모국어로 문서를 작성하고 동시에 다른 언어로 번역할 수 있으며 문서 형식을 유지하고 싶었습니다. Markdown-i18n은 이러한 문제점을 해결했습니다.

## 특성

- 지원 증분 번역. 수정된 부분만 번역하고, 수정되지 않은 부분은 반복 번역하지 않습니다. 번역 효율을 크게 향상시킵니다. token 소비를 크게 줄입니다.
- 모든 markdown 문서에 i18n 지원을 추가하고, 모든 언어에서 모든 언어로 번역을 지원합니다.
- 원본 파일의 형식을 완벽하게 따르십시오.
- 동시에 번역이 자연스럽고 정확하도록 보장합니다.
- 고효율 번역.

## 사용 지침

1. 의존성 설치

```bash
pip install -r requirements.txt
```

2. 번역 시작

방법 1: 새로운 python 파일 생성

```python
import os
from translate_md import translate
from parse_markdown import check_markdown_parse

api_key = os.getenv("API")       # OpenAI API key
api_url = os.getenv("API_URL")   # OpenAI API URL
engine = "gpt-4o"                # Language model

input_file_path = "README-zh.md" # 원본 파일 경로
output_file_path = "README.md"   # 출력 파일 경로
language = "English"             # 목표 언어
check_markdown_parse(input_file_path) # markdown 파일이 올바르게 파싱되었는지 확인합니다. 올바르게 파싱되면 번역할 수 있고, 오류가 발생하면 작성자에게 수정 요청을 해야 합니다. 이 단계는 필수는 아니지만, 번역 형식의 정확성을 보장하기 위함입니다.
translate(input_file_path, output_file_path, language, api_key, api_url, engine) # 원본 markdown 파일을 목표 언어로 번역하여 출력 파일에 저장합니다.
```

방법 2: 창고에 있는 기존 스크립트 사용

직접 translate_md.py 파일의 설정을 수정한 후 스크립트를 실행하면 됩니다.

```python
input_file_path = "README_CN.md" # 원본 파일 경로
output_file_path = "README.md"   # 출력 파일 경로
language = "English"             # 대상 언어
api_key = os.getenv("API")       # OpenAI API 키
api_url = os.getenv("API_URL")   # OpenAI API URL 기본값은 "https://api.openai.com/v1/chat/completions"
engine = "gpt-4o"                # 언어 모델
```