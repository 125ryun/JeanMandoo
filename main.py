import os
import pandas as pd
import konlpy
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Okt

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-21'
print("set environment variable: ", 'JAVA_HOME' in os.environ)

hannanum = Hannanum()
kkma = Kkma()
komoran = Komoran()
okt = Okt()
print("set module object")

# for file in os.scandir('./out'):
#     os.remove(file.path)

def pos_tagging():
    print("start pos tagging")

    # initialize data frame
    result = pd.DataFrame()
    tmp = pd.DataFrame()

    # data 텍스트를 문장들의 리스트로 불러들이기
    text = open('./data/document_01.txt', encoding='utf8').readlines()

    # text의 각 문장 line에 대해 pos tagging 실시 후 기존 데이터에 이어 붙이기
    for line in text:
        # do pos tagging
        pos_tagged_hannanum = hannanum.pos(line, ntags=22)
        pos_tagged_kkma = kkma.pos(line)
        pos_tagged_komoran = komoran.pos(line)
        pos_tagged_okt = okt.pos(line)

        # write out file(txt)
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

        pt_hannanum = pd.DataFrame({'hannanum':pos_tagged_hannanum})
        pt_kkma = pd.DataFrame({'kkma':pos_tagged_kkma})
        pt_komoran = pd.DataFrame({'komoran':pos_tagged_komoran})
        pt_okt = pd.DataFrame({'okt':pos_tagged_okt})

        tmp = pd.concat([pt_hannanum, pt_kkma, pt_komoran, pt_okt], axis=1)
        result = pd.concat([result, tmp])
    
    # write out file(csv)
    result.to_csv('./out/result_02.csv', sep=',', na_rep='-', encoding='utf-8-sig')

    print("**** DONE ****")

pos_tagging()