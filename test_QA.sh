python QA.py \
  --model_name_or_path ./model/QA \
  --test_file ./QA_data/test.json \
  --do_predict \
  --doc_stride 128 \
  --max_seq_length 512 \
  --pad_to_max_length \
  --output_dir ./model/QA
