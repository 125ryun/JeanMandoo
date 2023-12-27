import os
import re
import pandas as pd

def format_syntax_rank(): 
    out_dir = "bin/rank"
    
    data = pd.read_csv("data/rank/syntax.csv", na_values="", na_filter="")
    df = pd.DataFrame(data)
    df = df[["등급", "분류", "대표형", "관련형"]]
    df = df[df["분류"] != "표현"]

    new_mat = []
    N = df.shape[0]
    for i in range(N):
        row = df.iloc[i]
        
        rank = row["등급"].rstrip("급")
        type = row["분류"]
        words = [row["대표형"].strip("-")]
        if row["관련형"] != "":
            for word in row["관련형"].split(","):
                words.append(word.strip(" ").strip("-"))
        
        for word in words:
            new_mat.append([rank, type, word])

    new_df = pd.DataFrame(new_mat)
    new_df.columns = ["등급", "분류", "단어"]
    new_df = new_df[["분류", "단어", "등급"]]
    new_df.to_csv(f"{out_dir}/syntax.csv", index=False)