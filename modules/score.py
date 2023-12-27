import sys
import os
import re
import pandas as pd
from ctypes import *
import modules.utagger.bin.utagger as ut

def score_spm():
    vid_dir = "data/vid"
    out_dir = "out"

    metadata_dir = "bin/metadata"

    for file in os.listdir("bin/txt"):
        vid_name, vid_ext = file.split(".")
        output_path = f"{out_dir}/{vid_name}_score_spm.txt"
        if os.path.exists(output_path):
            continue
        
        with open(f"{metadata_dir}/{vid_name}_vid.txt", "r", encoding='UTF8') as f:
            fraction = f.readlines()
            num = int(fraction[0].strip())
            denom = int(fraction[1])

        with open(f"{metadata_dir}/{vid_name}_txt.txt", "r", encoding='UTF8') as f:
            syllables = int(f.readlines()[0])

        score = float(syllables / (num / denom))
        rank = "범위 외(spm이 210 이상, 390 이하일 경우에만 등급을 산출할 수 있습니다.)"
        if score>=210 and score<270:
            rank = "초급"
        elif score>=270 and score<330:
            rank = "중급"
        elif score>=330 and score<390:
            rank = "고급"

        with open(output_path, "w", encoding='UTF8') as f:
            f.write(f"spm: {str(score)}\n")
            f.write(f"등급: {str(rank)}\n")
            f.write(f"발화 시간: {float(num / denom)}(분)\n")
            f.write(f"음절 수: {syllables}")
            
        print(f"**** score(spm) 계산 완료: {output_path}")
        
def tagpos(root_path):
    
    tagger, lib = ut.Init_Utagger(root_path)

    txt_dir = "bin/txt"
    tagged_dir = "bin/tagged"
    out_dir = "out"
    
    for txt_file in os.listdir(txt_dir):
        txt_name, txt_ext = txt_file.split(".")
        print(f"**** start analyzing {txt_name}")
        # if txt_name.startswith("dummy"): continue
        
        txt_path = f"{txt_dir}/{txt_file}"
        output_path_syntax = f"{out_dir}/{txt_name}_score_syntax.txt"
        output_path_vocab = f"{out_dir}/{txt_name}_score_vocab.txt"
        if os.path.exists(output_path_syntax) and os.path.exists(output_path_vocab):
            continue
        
        with open(txt_path, "r", encoding='utf-8') as f:
            text = f.read()
        if len(text) == 0: continue
        if os.path.exists(f"bin/tagged/{txt_name}.csv"):
            continue
        
        preprocessed = re.sub(r"[.,?!]", "", text)
        tagged = tagger(0, c_wchar_p(preprocessed), 3) # analyze
        tagged = tagged.rstrip("\n").replace("+", " ")
        tagged_list = tagged.split(" ")
        tagged_matrix = [item.split("/") for item in tagged_list]
        
        df = pd.DataFrame(tagged_matrix).iloc[:, 0:2]
        df.columns = ["단어", "분류"]

        # 전체 기준 탐색
        
        ## type(type-token ratio 할 때 그거)
        dict = {word:0 for word in df["단어"]}
        types = dict.keys()
        cnt_types = len(types)
        cnt_tokens = df.shape[0]
        with open(txt_path, "a", encoding='utf-8') as f:
            f.write(str(cnt_types))
            f.write(str(cnt_tokens))
        
        ## 동음이의어, 다의어
        cnt_동형이의어 = 0
        cnt_다의어 = 0
        cnt_syntax_rank = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
        
        선어말어미 = ["EP"]
        연결어미 = ["EC"]
        전성어미 = ["ETN", "ETM"]
        종결어미 = ["EF"]
        조사 = ["JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JX", "JC"]
        rank_syntax = pd.DataFrame(pd.read_csv("bin/rank/syntax.csv", encoding='utf8'))
    
        n = df.shape[0]
        weighted_sum_syntax = 0
        for i in range(n):
            word = df.iloc[i]["단어"]
            pos = df.iloc[i]["분류"]
            
            syntax_flag = 0
            searchword = word
            if pos in 선어말어미: 
                searchpos = "선어말어미"
                syntax_flag = 1
            if pos in 연결어미: 
                searchpos = "연결어미"
                syntax_flag = 1
            if pos in 전성어미: 
                searchpos = "전성어미"
                syntax_flag = 1
            if pos in 종결어미: 
                searchpos = "종결어미"
                syntax_flag = 1
            if pos in 조사: 
                searchpos = "조사"
                syntax_flag = 1
            
            if "__" in word:
                name, num = word.split("__")
                if len(num)==0:
                    continue
                if len(num)==6 and num[2:]!="0000":
                    cnt_다의어 += 1
                if num[:2]!="00":
                    cnt_동형이의어 += 1
                    searchword = name+num[:2]
                    if num[0]=="0":
                        searchword = name + num[1]
                        
            if syntax_flag:
                try:
                    index = rank_syntax["단어"].tolist().index(searchword)
                    rank = str(int(rank_syntax.iloc[index]["등급"]))
                    cnt_syntax_rank[rank] = cnt_syntax_rank[rank] + 1
                    weighted_sum_syntax = weighted_sum_syntax + int(rank)
                except:
                    pass
                
        type_token_ratio = cnt_types / cnt_tokens
        
        score_homo = cnt_동형이의어 / cnt_tokens
        score_poly = cnt_다의어 / cnt_tokens
        score_syntax = weighted_sum_syntax * 10 / cnt_types + type_token_ratio
        
        with open(f"{out_dir}/{txt_name}_score_vocab.txt", "w", encoding='utf-8') as f:
            f.write(f"전체 토큰 수: {str(cnt_tokens)}\n")
            f.write(f"동음이의어 출현 비율(빈도/토큰 수): {str(score_homo)}\n")
            f.write(f"동음이의어 빈도: {str(cnt_동형이의어)}\n")
            f.write(f"다의어 출현 비율(빈도/토큰 수): {str(score_poly)}\n")
            f.write(f"다의어 빈도: {str(cnt_다의어)}\n")
        print(f"**** score(동음이의어, 다의어) 계산 완료: {out_dir}/{txt_name}_score_vocab.txt")
        
        with open(f"{out_dir}/{txt_name}_score_syntax.txt", "w", encoding='utf-8') as f:
            f.write(f"문형 난도: {str(score_syntax)}\n")
            f.write(f"A급: {str(cnt_syntax_rank['1'])}\n")
            f.write(f"B급: {str(cnt_syntax_rank['2'])}\n")
            f.write(f"C급: {str(cnt_syntax_rank['3'])}\n")
            f.write(f"D급: {str(cnt_syntax_rank['4'])}\n")
            f.write(f"E급: {str(cnt_syntax_rank['5'])}\n")
            f.write(f"F급: {str(cnt_syntax_rank['6'])}\n")
            f.write(f"타입 토큰 비율: {str(cnt_types)} / {str(cnt_tokens)} = {str(type_token_ratio)}")

        print(f"**** score(문형) 계산 완료: {out_dir}/{txt_name}_score_syntax.txt")
        
        print(f"**** done analyzing {txt_name}")
        
    lib.deleteUCMA(0) # 0번 객체 삭제
    lib.Global_release() # 메모리 해제 