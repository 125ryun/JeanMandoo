import os
import csv
import pandas as pd
import konlpy
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Okt

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-21'
print("set environment variable: ", 'JAVA_HOME' in os.environ)

text = open('./data/document_01.txt', encoding='utf8').read()

hannanum = Hannanum()
kkma = Kkma()
komoran = Komoran()
okt = Okt()

pos_tagged_hannanum = hannanum.pos(text)
pos_tagged_kkma = kkma.pos(text)
pos_tagged_komoran = komoran.pos(text)
pos_tagged_okt = okt.pos(text)

for file in os.scandir('./out'):
    os.remove(file.path)

out_file = open('./out/out_hannanum.txt', 'w', encoding='utf8')
for item in pos_tagged_hannanum:
    out_file.write(item[0] + "/" + item[1] + "\n")
out_file.close()

out_file = open('./out/out_kkma.txt', 'w', encoding='utf8')
for item in pos_tagged_kkma:
    out_file.write(item[0] + "/" + item[1] + "\n")
out_file.close()

out_file = open('./out/out_komoran.txt', 'w', encoding='utf8')
for item in pos_tagged_komoran:
    out_file.write(item[0] + "/" + item[1] + "\n")
out_file.close()

out_file = open('./out/out_okt.txt', 'w', encoding='utf8')
for item in pos_tagged_okt:
    out_file.write(item[0] + "/" + item[1] + "\n")
out_file.close()

# with open('out.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

pt_hannanum = pd.DataFrame({'hannanum':pos_tagged_hannanum})
pt_kkma = pd.DataFrame({'kkma':pos_tagged_kkma})
pt_komoran = pd.DataFrame({'komoran':pos_tagged_komoran})
pt_okt = pd.DataFrame({'okt':pos_tagged_okt})

# print(pt_hannanum)

# result = pd.concat([pt_hannanum, pt_kkma, pt_komoran, pt_okt])
result = pd.concat([pt_hannanum, pt_kkma, pt_komoran, pt_okt], axis=1)
# result = pt_hannanum
# result.join(pt_kkma)
# result.join(pt_komoran)
# result.join(pt_okt)
print(result)
print(result['kkma'][0]) # 'kkma'열 0행
# result.to_csv('./out/result.csv', sep=',', na_rep='-', encoding='utf-8-sig')
# out_csv = open('./out/result.csv', 'w')