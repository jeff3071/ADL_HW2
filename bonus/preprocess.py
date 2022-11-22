import json
import os
import sys

with open(sys.argv[1], 'r') as context1:
  train_data = json.load(context1)

res = []
for data in train_data:
  temp = {
    'text': data['text'],
    'label': data['intent'],
    'id': data['id']
  }
  res.append(temp)

os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
json.dump(res, open(sys.argv[2], 'w',encoding='utf-8'), indent=2, ensure_ascii=False)
