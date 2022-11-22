# ADL HW2 Bonus

利用Bert做HW1的task

- intent classification
- slot tagging

```
.
├── Readme.md
├── intent.sh
├── preprocess.py
├── slot.sh
├── train_intent.py
└── train_slot.py
```
- preprocess.py: 將intent classification的data進行前處理
- train_intent.py: 訓練intent classification的model
- train_slot.py: 訓練slot tagging的model

## Intent Classification

### Train

```
python preprocess.py <path_to_data> <target_position>

# python preprocess.py ./data/train.json ./intent_data/train.json

bash intent.sh <path_to_train_data> <path_to_val_data>

# bash intent.sh ./intent_data/train.json ./intent_data/eval.json
```

## Slot Tagging

```
bash slot.sh <path_to_train_data> <path_to_val_data>

# bash slot.sh ./slot_data/train.json ./slot_data/eval.json
```