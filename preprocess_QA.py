import json
import os
import sys

with open(sys.argv[1], 'r') as f:
    original_data = json.load(f)

with open(sys.argv[3], 'r') as context:
    context_data = json.load(context)

os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)


QA_data = {'data': []}

if 'answer' in original_data[0].keys():
  for i, data in enumerate(original_data):
    temp = {
      'id': data['id'],
      'context': context_data[data['relevant']],
      'question': data['question'],
      'answers': {'text': [data['answer']['text']], 'answer_start': [data['answer']['start']]}
    }
    QA_data['data'].append(temp)
else:
  print('tranform test data')
  for i, data in enumerate(original_data[:]):
    temp = {
      'id': data['id'],
      'context': data['relevant'],
      'question': data['question'],
      'answers': {'text': ['0'], 'answer_start': [0]}
    }
    QA_data['data'].append(temp)
# print(QA_data['data'][0])
json.dump(QA_data, open(sys.argv[2], 'w',encoding='utf-8'),indent=2, ensure_ascii=False)