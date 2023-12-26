import sys
import os
import pandas as pd
from ctypes import *
import modules.utagger.bin.utagger as ut

def score_syntax(root_path):

    tagger, lib = ut.Init_Utagger(root_path)

    txt_dir = "bin/txt/"
    out_dir = "bin/tagged"
    for txt_file in os.listdir(txt_dir):
        txt_name, txt_ext = txt_file.split(".")
        txt_path = txt_dir + txt_file
        output_path = out_dir + txt_name + ".txt"
        
        with open(txt_path, "r", encoding='utf-8') as f:
            text = f.read()
        if len(text) == 0: continue
        
        tagged = tagger(0, c_wchar_p(text), 3) # analyze
        tagged = tagged.rstrip("\n").replace("+", " ")
        tagged_list = tagged.split(" ")
        tagged_matrix = [item.split("/") for item in tagged_list]

        df = pd.DataFrame(tagged_matrix).iloc[:, 0:2]
        df.to_csv(f"{out_dir}/{txt_name}.csv", index=False)
        
    lib.deleteUCMA(0) # 0번 객체 삭제
    lib.Global_release() # 메모리 해제