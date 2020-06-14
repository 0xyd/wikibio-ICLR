import argparse
import torch
from transformers import MarianMTModel, MarianTokenizer

def translate(model, tokenizer, device, src_txt):
  encoded_txt = tokenizer.prepare_translation_batch(src_txt).to(device)
  tgt_text = model.generate(**encoded_txt)
  tgt_text = tokenizer.batch_decode(tgt_text, skip_special_tokens=True)
  return tgt_text

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--model_name', type=str, required=True)
  parser.add_argument('--input_path', type=str, required=True)
  parser.add_argument('--output_path', type=str, required=True)
  parser.add_argument('--batch_size', type=int, default=32)
  args = parser.parse_args() 
  
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  tokenizer = MarianTokenizer.from_pretrained(args.model_name)
  model = MarianMTModel.from_pretrained(args.model_name).to(device)

  tgt = open(args.output_path, 'w')
  with open(args.input_path) as src:
    batch = []
    for s in src.read().split('\n'):
      if len(s) == 0: continue
      batch.append(s)
      if len(batch) == args.batch_size:
        tgt_text = translate(model, tokenizer, device, batch)
        for t in tgt_text:
          tgt.write(t+'\n')
        batch = []
    if len(batch) > 0:
      tgt_text = translate(model, tokenizer, device, batch)
      for t in tgt_text:
        tgt.write(t+'\n')
    tgt.close()

if __name__ == '__main__':
  main()
