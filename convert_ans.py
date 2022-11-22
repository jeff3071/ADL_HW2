import json
import os
import sys

with open(sys.argv[1], 'r') as f:
    original_data = json.load(f)

with open(sys.argv[2], 'w', encoding="utf-8") as csvfile:
    csvfile.write("id,answer\n")
    for id in original_data:
        if ',' in original_data[id]:
            original_data[id] = "\"" + original_data[id]+"\""
            print(original_data[id])
        csvfile.write(f'{id},{original_data[id]}\n')
csvfile.close()
