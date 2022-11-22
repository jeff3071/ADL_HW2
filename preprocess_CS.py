import json
import os
import sys

with open(sys.argv[1], 'r') as f:
    original_data = json.load(f)

with open(sys.argv[3], 'r') as context:
    context_data = json.load(context)

CS_data ={'data': []}

for i, data in enumerate(original_data):
    temp = {
        'id': data['id'],
        'question': data['question'],
        'paragraphs': [context_data[paragraph_index] for paragraph_index in data['paragraphs']],
        'label': data['paragraphs'].index(data['relevant']) if 'relevant' in data.keys() else 0
    }
    CS_data['data'].append(temp)

os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
json.dump(CS_data, open(sys.argv[2], 'w',encoding='utf-8'), indent=2, ensure_ascii=False)