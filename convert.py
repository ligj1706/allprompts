import csv
import json

def convert_csv_to_json():
    prompts = []
    
    with open('prompts.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            prompts.append({
                'id': i,
                'actor': row['actor'],
                'prompt': row['prompt'].replace('\n', '\\n')
            })
    
    with open('public/data/prompts.json', 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False)

if __name__ == '__main__':
    convert_csv_to_json()