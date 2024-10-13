import csv
import json
import os

CHUNK_SIZE = 1000

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_text(text):
    # 将连续的换行符替换为单个换行符，然后分割成段落
    paragraphs = [p.strip() for p in text.replace('\n\n', '\n').split('\n') if p.strip()]
    return paragraphs

def convert_csv_to_json_chunks():
    ensure_dir('public/data')
    
    prompts = []
    chunk_count = 0
    
    with open('prompts.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            title = row['actor']
            content = process_text(row['prompt'])
            prompts.append({
                'id': i,
                'title': title,
                'content': content
            })
            
            if len(prompts) == CHUNK_SIZE:
                with open(f'public/data/chunk_{chunk_count}.json', 'w', encoding='utf-8') as f:
                    json.dump(prompts, f, ensure_ascii=False)
                chunk_count += 1
                prompts = []
    
    # 保存最后一批数据
    if prompts:
        with open(f'public/data/chunk_{chunk_count}.json', 'w', encoding='utf-8') as f:
            json.dump(prompts, f, ensure_ascii=False)
        chunk_count += 1
    
    # 生成索引文件
    with open('public/data/index.json', 'w', encoding='utf-8') as f:
        json.dump({
            'totalChunks': chunk_count,
            'chunkSize': CHUNK_SIZE
        }, f)

if __name__ == '__main__':
    convert_csv_to_json_chunks()