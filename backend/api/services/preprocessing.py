from trafilatura import fetch_url, extract, html2txt
import json
from pathlib import Path

file_path = Path('output.json')

def preprocess(url, content):
    main_text = extract(content)
    transformToJson(url, main_text)
    return content

def transformToJson(url, text_data):

    if not file_path.exists():
        with open(file_path, mode='w', encoding='utf-8') as f:
            json.dump([], f)

    with open(file_path, "r") as file:
        data = json.load(file)
    
    new_entry = {"url": url, "content": text_data}
    data.append(new_entry)
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)