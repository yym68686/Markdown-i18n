import os
import difflib
import subprocess
from ModelMerge import chatgpt
from parse_markdown import get_entities_from_markdown_file, process_markdown_entities_and_save

def get_latest_commit_file_content(file_path):
    try:
        # 获取文件所在的 Git 仓库根目录
        repo_root = subprocess.run(["git", "-C", os.path.dirname(file_path), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()

        # 将文件路径转换为相对路径
        relative_path = os.path.relpath(file_path, repo_root)

        # 获取最新提交的文件内容
        command = ["git", "-C", repo_root, "show", f"HEAD:{relative_path}"]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()

        return result.stdout
    except Exception as e:
        print(f"发生未知错误：{e}")
        return None

def translate_text(text, agent):
    result = agent.ask(text)
    return result

def get_latest_commit_file_entities(input_file_path, current_source_content):
    latest_commit_content = get_latest_commit_file_content(input_file_path)
    if latest_commit_content:
        latest_commit_entities = get_entities_from_markdown_file(None, raw_text=latest_commit_content)
    else:
        latest_commit_entities = [entity.copy() for entity in current_source_content]
        for entity in latest_commit_entities:
            entity.content = ""
    return latest_commit_entities

def translate(input_file_path, output_file_path="output.md", language="English", api_key=None, api_url="https://api.openai.com/v1/chat/completions", engine="gpt-4o"):
    if not api_key:
        raise ValueError("API key is required for translation.")
    translator_prompt = (
        "You are a translation engine, you can only translate text and cannot interpret it, and do not explain. "
        "Translate the text to {}, please do not explain any sentences, just translate or leave them as they are. "
        "Retain all spaces and line breaks in the original text. "
        "Please do not wrap the code in code blocks, I will handle it myself. "
        "If the code has comments, you should translate the comments as well. "
        "If the original text is already in {}, please do not skip the translation and directly output the original text. "
        "This is the content you need to translate: "
    ).format(language, language)

    agent = chatgpt(
        api_key=api_key,
        api_url=api_url,
        engine=engine,
        system_prompt=translator_prompt,
        use_plugins=False
    )

    # 读取当前源文件内容
    current_source_content = get_entities_from_markdown_file(input_file_path)

    # 读取已翻译的文件内容
    if os.path.exists(output_file_path):
        current_translated_entities = get_latest_commit_file_entities(output_file_path, current_source_content)
        # print("latest_commit_entities", current_translated_entities)
    else:
        # 如果输出文件不存在，自动创建文件，并返回空字符串
        current_translated_entities = get_entities_from_markdown_file(output_file_path)
    # 获取最新提交的源文件内容
    latest_commit_entities = get_latest_commit_file_entities(input_file_path, current_source_content)

    # 使用 difflib 比较两个版本的差异
    differ = difflib.Differ()
    diff = list(differ.compare([entity.content for entity in latest_commit_entities],
                               [entity.content for entity in current_source_content]))

    # print("diff", diff)
    # 翻译修改的部分
    translated_entities = []
    source_index = 0
    translated_index = 0

    for line in diff:
        if line.startswith('  '):  # 未修改的行
            # print("line", repr(line), translated_index < len(current_translated_entities), current_translated_entities[translated_index].content != '', repr(current_translated_entities[translated_index].content))
            if translated_index < len(current_translated_entities) and current_translated_entities[translated_index].content != '':
                translated_entities.append(current_translated_entities[translated_index])
                translated_index += 1
            else:
                # 如果已翻译内容不足，则翻译源内容
                entity = current_source_content[source_index]
                # print("entity", entity)
                if entity.content.strip():
                    translated_text = translate_text(entity.content, agent)
                    print(">", entity.content)
                    entity.content = translated_text if translated_text else entity.content
                    print("<", repr(entity.content), end="\n\n")
                translated_entities.append(entity)
            source_index += 1
        elif line.startswith('+ '):  # 新增的行
            entity = current_source_content[source_index]
            if entity.content.strip():
                translated_text = translate_text(entity.content, agent)
                print(">", entity.content)
                entity.content = translated_text if translated_text else entity.content
                print("<", repr(entity.content), end="\n\n")
            translated_entities.append(entity)
            source_index += 1
        elif line.startswith('- '):  # 删除的行
            if translated_index < len(current_translated_entities):
                translated_index += 1

    # 检查是否所有行都未修改
    all_unchanged = all(line.startswith('  ') for line in diff)
    is_all_empty = all(entity.content.strip() == '' for entity in current_translated_entities)
    if all_unchanged and not is_all_empty:
        translated_entities = current_translated_entities
        # 输出翻译结果

    is_all_empty = all(entity.content.strip() == '' for entity in translated_entities)
    if not is_all_empty:
        process_markdown_entities_and_save(translated_entities, output_file_path, linemode=True)

if __name__ == "__main__":
    input_file_path = "README_CN.md"
    output_file_path = "README.md"
    language = "English"
    api_key = os.getenv("API")
    api_url = os.getenv("API_URL")
    engine = "gpt-4o"
    translate(input_file_path, output_file_path, language, api_key, api_url, engine)