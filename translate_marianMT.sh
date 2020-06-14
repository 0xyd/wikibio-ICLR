#!/bin/bash
#for lang in de fr cs ru fi nl lv it 
#do
#  echo "Translating $lang ..."
#  python marianMT.py \
#    --model_name=Helsinki-NLP/opus-mt-en-$lang \
#    --input_path=./top200/$lang/top200_test.en \
#    --output_path=./top200/$lang/top200_test.kd.$lang
#done

#echo "Translating ja ..."
#python marianMT.py \
#  --model_name=Helsinki-NLP/opus-mt-en-jap \
#  --input_path=./top200/ja/top200_test.en \
#  --output_path=./top200/ja/top200_test.kd.ja

#for lang in es lt
#for lang in lt
#do
#  echo "Translating $lang ..."
#  python marianMT.py \
#    --model_name=Helsinki-NLP/opus-mt-en-de \
#    --input_path=./top200/$lang/top200_test.en \
#    --output_path=./top200/$lang/tmp_top200_test.kd.de
#  python marianMT.py \
#    --model_name=Helsinki-NLP/opus-mt-de-$lang \
#    --input_path=./top200/$lang/tmp_top200_test.kd.de \
#    --output_path=./top200/$lang/top200_test.kd.$lang \
#    --batch_size=8
#done

#echo "Translating zh"
#python marianMT.py \
#  --model_name=Helsinki-NLP/opus-mt-en-fi \
#  --input_path=./top200/zh/top200_test.en \
#  --output_path=./top200/zh/tmp_top200_test.kd.fi

#python marianMT.py \
#  --model_name=Helsinki-NLP/opus-mt-fi-ZH \
#  --input_path=./top200/zh/tmp_top200_test.kd.fi \
#  --output_path=./top200/zh/top200_test.kd.zh

#echo "Translating tr"
#python marianMT.py \
#  --model_name=Helsinki-NLP/opus-mt-en-fi \
#  --input_path=./top200/tr/top200_test.en \
#  --output_path=./top200/tr/tmp_top200_test.kd.fi
#python marianMT.py \
#  --model_name=Helsinki-NLP/opus-mt-fi-tr \
#  --input_path=./top200/tr/tmp_top200_test.kd.fi \
#  --output_path=./top200/tr/top200_test.kd.tr

echo "Translationg ar"
python marianMT.py \
  --model_name=./ar-en \
  --input_path=./top200/ar/top200_test.en \
  --output_path=./top200/ar/tmp_top200_test.kd.ar
