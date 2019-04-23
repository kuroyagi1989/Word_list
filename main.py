# coding: UTF-8

# ライブラリの読み込み

# txt to csv
import re
from collections import Counter
import csv

# pdf to text
import subprocess




text = subprocess.check_output(['pdf2txt.py', './56.pdf']).decode('utf-8')

file = open('words.txt','w')
file.write(text)
file.close()

# 00 テキストの取得
f= open('wordsgit.txt','r',encoding='UTF-8')
target_text  = f.read()
f.close()

# 01 文章を単語に分ける
# 複数の区切り文字を指定するため re.split を使う
words = re.split(r'\s|\,|\.|\(|\)', target_text.lower())

# 02 集計する
counter = Counter(words)

# 03 csvへの書き込み関数の定義
def new():
    open('data.csv', 'w')
    pass

def add(x):
    with open('data.csv','a',encoding='UTF-8',newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(x)

def reset(x):
    with open('data.csv','w',encoding='UTF-8',newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(x)

# 単語帳書き込み用csv生成
new()

# 04 ファイルの初期化
label = []
label.append('tanogocho')
reset(label)

# 05 集計結果の出力とcsvへの書き込み
for word, count in counter.most_common():
    csvlist = []
    if len(word) > 0:
        # print("%s,%d" % (word, count))
        csvlist.append(word)
        csvlist.append(count)
        add(csvlist)

# ファイルクローズ
f.close()