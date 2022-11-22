# "${1}": path to the training file.
# "${2}": path to the validation file.

python3 train_slot.py \
  --model_name_or_path roberta-base \
  --train_file "${1}"\
  --validation_file "${2}" \
  --per_device_train_batch_size 64 \
  --output_dir ./model/roberta/slot \
  --do_train \
  --do_eval \
  --save_steps 5000 \
  --learning_rate 1e-4 \
  --num_train_epochs 10 \
  --overwrite_output_dir \
  --evaluation_strategy steps \
  --eval_steps 100