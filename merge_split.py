import re
import os.path as osp
import argparse
from collections import Counter

def pairwise_file_read(file_1, file_2):
  try:
    file1 = open(file_1)
    file2 = open(file_2)
  except:
    return [], []

  pairwise_sentence = []
  pairwise_sentence_set = set()
  line_count = 0
  line_numbers = []
  for l1, l2 in zip(file1, file2):
    if (l1, l2) not in pairwise_sentence_set:
      line_numbers.append(line_count)
      pairwise_sentence.append((l1, l2))
      pairwise_sentence_set.update([(l1, l2)])
    line_count += 1
  return pairwise_sentence, line_numbers

def pairwise_file_write(data, f1_path, f2_path):

  file1 = open(f1_path, 'w')
  file2 = open(f2_path, 'w')
  
  for s, t in data:
    file1.write(s)  
    file2.write(t)
  
  file1.close()
  file2.close()

def read_id_with_specific_line(fpath, line_numbers):
  line_numbers_set = set(line_numbers) 
  ids = []
  ids_set = set(ids)
  try:
    with open(fpath) as f:
      for i, id in enumerate(f):
        if i in line_numbers_set and i not in ids_set:
          ids.append(id)
  except:
    pass 
  return ids

def remove_duplicate(data, data_ids):
  while True:

    src = [d[0] for d in data]
    tgt = [d[1] for d in data]
    src_duplicate_counter = Counter([d for d in src])
    src_duplicates = [d for d, c in src_duplicate_counter.items() if c > 1 and d is not None]
    tgt_duplicate_counter = Counter([d for d in tgt])
    tgt_duplicates = [d for d, c in tgt_duplicate_counter.items() if c > 1 and d is not None]

    if len(src_duplicates) == 0 and len(tgt_duplicates) == 0:
      break
    
    for d in src_duplicates:
      duplicated_index = src.index(d)
      src[duplicated_index] = None
      data[duplicated_index] = None
      data_ids[duplicated_index] = None
    for d in tgt_duplicates:
      duplicated_index = tgt.index(d)
      tgt[duplicated_index] = None
      data[duplicated_index] = None
      data_ids[duplicated_index] = None

    data = [d for d in data if d is not None]
    data_ids = [d for d in data_ids if d is not None]
  
  return data, data_ids
  
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--src_train_path', required=True, type=str)
  parser.add_argument('--src_valid_path', required=True, type=str)
  parser.add_argument('--src_test_path', required=True, type=str)
  parser.add_argument('--tgt_train_path', required=True, type=str)
  parser.add_argument('--tgt_valid_path', required=True, type=str)
  parser.add_argument('--tgt_test_path', required=True, type=str)
  parser.add_argument('--src_train_id_path', required=True, type=str)
  parser.add_argument('--src_valid_id_path', required=True, type=str)
  parser.add_argument('--src_test_id_path', required=True, type=str)
  parser.add_argument('--output_path', required=True, type=str)
  args = parser.parse_args()
  lang = args.tgt_train_path[-2:]
  
  data = []
  
  src_tgt, train_line_numbers = pairwise_file_read(args.src_train_path, args.tgt_train_path)
  data.extend(src_tgt)
  src_tgt, valid_line_numbers = pairwise_file_read(args.src_valid_path, args.tgt_valid_path)
  data.extend(src_tgt)
  src_tgt, test_line_numbers = pairwise_file_read(args.src_test_path, args.tgt_test_path)
  data.extend(src_tgt)

  data_ids = []
  data_ids.extend(read_id_with_specific_line(args.src_train_id_path, train_line_numbers))
  data_ids.extend(read_id_with_specific_line(args.src_valid_id_path, valid_line_numbers))
  data_ids.extend(read_id_with_specific_line(args.src_test_id_path, test_line_numbers))
  
  data, data_ids = remove_duplicate(data, data_ids)

  assert len(data) == len(set(data))
  assert len(data_ids) == len(set(data_ids)) 

  train_data = data[:-4000]
  test_data = data[-4000:-2000]
  valid_data = data[-2000:]
  print('Number of training set: %d' % len(train_data))
  print('Number of valid set: %d' % len(valid_data))
  print('Number of test set: %d' % len(test_data))
  
  train_data_ids = data_ids[:-4000]
  test_data_ids = data_ids[-4000:-2000]
  valid_data_ids = data_ids[-2000:]
  print('Number of training set id: %d' % len(train_data_ids))
  print('Number of valid set id: %d' % len(valid_data_ids))
  print('Number of test set id: %d' % len(test_data_ids))
  
  pairwise_file_write(
    train_data, 
    osp.join(args.output_path, 'new_train.en'), 
    osp.join(args.output_path, 'new_train.' + lang))  

  pairwise_file_write(
    test_data, 
    osp.join(args.output_path, 'new_test.en'), 
    osp.join(args.output_path, 'new_test.' + lang))

  pairwise_file_write(
    valid_data, 
    osp.join(args.output_path, 'new_valid.en'), 
    osp.join(args.output_path, 'new_valid.' + lang))

  train_data_ids = [str(d) for d in train_data_ids]
  test_data_ids = [str(d) for d in test_data_ids]
  valid_data_ids = [str(d) for d in valid_data_ids]

  with open(osp.join(args.output_path, 'new_train.id'), 'w') as f:
    for id in train_data_ids:
      f.write("%s" % id)
  with open(osp.join(args.output_path, 'new_valid.id'), 'w') as f:
    for id in valid_data_ids:
      f.write("%s" % id)
  with open(osp.join(args.output_path, 'new_test.id'), 'w') as f:
    for id in test_data_ids:
      f.write("%s" % id)

if __name__ == "__main__":
  main()
