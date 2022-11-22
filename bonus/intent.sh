# "${1}": path to the training file.
# "${2}": path to the validation file.

python train_intent.py \
  --model_name_or_path roberta-base \
  --train_file "${1}" \
  --validation_file "${2}" \
  --do_train \
  --do_eval \
  --max_seq_length 512 \
  --per_device_train_batch_size 8 \
  --learning_rate 3e-5 \
  --num_train_epochs 3 \
  --save_steps 5000 \
  --output_dir ./model/roberta/intent \
  --overwrite_output_dir \