import sys
import os
import re
import pandas as pd
from ctypes import *
import modules.utagger.bin.utagger as ut

def score_syntax(root_path):
    
    tagger, lib = ut.Init_Utagger(root_path)

    txt_dir = "bin/txt"
    out_dir = "bin/tagged"
    for txt_file in os.listdir(txt_dir):
        txt_name, txt_ext = txt_file.split(".")
        txt_path = f"{txt_dir}/{txt_file}"
        output_path = f"{out_dir}/{txt_name}.txt"
        if os.path.exists(f"{out_dir}/{txt_name}.txt"):
            continue
        
        with open(txt_path, "r", encoding='utf-8') as f:
            text = f.read()
        if len(text) == 0: continue
        
        preprocessed = re.sub(r"[^가-힣]", "", text)
        tagged = tagger(0, c_wchar_p(preprocessed), 3) # analyze
        tagged = tagged.rstrip("\n").replace("+", " ")
        tagged_list = tagged.split(" ")
        tagged_matrix = [item.split("/") for item in tagged_list]
        
        df = pd.DataFrame(tagged_matrix).iloc[:, 0:2]
        df.columns=["단어", "품사태그"]
        df.to_csv(f"{out_dir}/{txt_name}.csv")   

        cnt_동형이의어 = 0
        cnt = {'초급':0, '중급':0, '고급':0, '최상급':0}
        
        for word in df["단어"]:
            if "__" in word:
                cnt_동형이의어 += 1
        
        df_선어말어미 = df[df["품사태그"] == "EP"]
        df_연결어미 = df[df["품사태그"] == "EC"]
        df_전성어미 = df[df["품사태그"][:2] == "ET"]
        df_종결어미 = df[df["품사태그"] == "EF"]
        df_조사 = df[df["품사태그"][0] == "J"]
        dfs = [df_선어말어미, df_연결어미, df_전성어미, df_종결어미, df_조사]
        
        rank_dir = "data/rank"
        rank_file = "syntax.csv"
        data_rank = pd.read_csv(f"{rank_dir}/{rank_file}")
        df_rank = pd.DataFrame(data_rank)
        
        for df in dfs:
            for item in df.iloc():
                word = item[0]
                
                cnt[df_rank[df_rank["단어"] == word]] += 1
        
        with open(output_path, "w", encoding='utf8') as f:
            f.write(####)
                    
    lib.deleteUCMA(0) # 0번 객체 삭제
    lib.Global_release() # 메모리 해제 
    
    print(f"**** score(syntax) 계산 완료: {output_path}")
