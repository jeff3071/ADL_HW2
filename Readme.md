# ADL HW2

給定四段文章，使用Bert找出問題的答案，可以細分為兩個task：Context Selection、Question Answering

```
├── CS.py
├── QA.py
├── Readme.md
├── convert_ans.py
├── preprocess_CS.py
├── preprocess_QA.py
├── run.sh
├── test_CS.sh
├── test_QA.sh
├── trainer_qa.py
└── utils_qa.py
```

## Training

兩個task皆使用hfl/chinese-roberta-wwm-ext

### Context Selection

```
python CS.py \
--model_name_or_path hfl/chinese-roberta-wwm-ext \
--train_file ./CS_data/train.json \
--validation_file ./CS_data/valid.json \
--cache_dir ./cache/ \
--do_train \
--do_eval \
--gradient_accumulation_steps 8 \
--pad_to_max_length \
--max_seq_length 512 \
--save_steps 5000 \
--learning_rate 3e-5 \
--num_train_epochs 3 \
--output_dir ./model/CS/ \
--overwrite_output_dir \
--per_device_eval_batch_size 2 \
--per_device_train_batch_size 2 \
```

### Question Answering

```
python QA.py \
  --model_name_or_path ./model/QA/ \
  --train_file ./QA_data/train.json \
  --validation_file ./QA_data/valid.json \
  --do_eval \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 8 \
  --per_device_eval_batch_size 8 \
  --eval_accumulation_steps 8 \
  --learning_rate 3e-5 \
  --num_train_epochs 3 \
  --pad_to_max_length \
  --max_seq_length 512 \
  --logging_steps 100 \
  --save_total_limit 1 \
  --output_dir ./model/QA/ \
  --overwrite_output_dir \
  --evaluation_strategy steps \
```


## Testing

```
bash download.sh

bash ./run.sh </path/to/context.json> </path/to/test.json> </path/to/pred/prediction.csv>

# bash ./run.sh ./data/context.json ./data/test.json ./prediction.csv
```

## Kaggle Score

0.79113