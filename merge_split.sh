#!/bin/bash
for l in zh ja de ar fr it es ru nl cs ko vi tr fi lt lv
do
  echo "check lang: $l"
  python merge_split.py \
    --output_path=$l \
    --src_train_path=$l/train.en \
    --src_test_path=$l/test.en \
    --src_valid_path=$l/valid.en \
    --src_train_id_path=$l/train.id \
    --src_valid_id_path=$l/valid.id \
    --src_test_id_path=$l/test.id \
    --tgt_train_path=$l/train.$l \
    --tgt_test_path=$l/test.$l \
    --tgt_valid_path=$l/valid.$l
  python check_replica.py \
    --file_1=$l/new_train.en \
    --file_2=$l/new_test.en
  python check_replica.py \
    --file_1=$l/new_train.en \
    --file_2=$l/new_valid.en
  python check_replica.py \
    --file_1=$l/new_train.$l \
    --file_2=$l/new_test.$l
  python check_replica.py \
    --file_1=$l/new_train.$l \
    --file_2=$l/new_valid.$l
  python check_replica.py \
    --file_1=$l/new_test.en \
    --file_2=$l/new_valid.en
  python check_replica.py \
    --file_1=$l/new_test.$l \
    --file_2=$l/new_valid.$l
  #python check_replica.py \
  #  --file_1=$l/new_train.ib \
  #  --file_2=$l/new_test.ib
  #python check_replica.py \
  #  --file_1=$l/new_train.ib \
  #  --file_2=$l/new_valid.ib
  #python check_replica.py \
  #  --file_1=$l/new_test.ib \
  #  --file_2=$l/new_valid.ib
  python check_replica.py \
    --file_1=$l/new_train.id \
    --file_2=$l/new_valid.id
  python check_replica.py \
    --file_1=$l/new_train.id \
    --file_2=$l/new_test.id
  python check_replica.py \
    --file_1=$l/new_test.id \
    --file_2=$l/new_valid.id  
  
done


