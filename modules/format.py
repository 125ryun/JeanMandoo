import os
import re
import pandas as pd

def format_syntax_rank(): 
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

    df_선어말어미 = new_df[new_df["분류"] == "선어말어미"]
    df_연결어미 = new_df[new_df["분류"] == "연결어미"]
    df_전성어미 = new_df[new_df["분류"] == "전성어미"]
    df_종결어미 = new_df[new_df["분류"] == "종결어미"]
    df_조사 = new_df[new_df["분류"] == "조사"]

    df_선어말어미 = df_선어말어미[["단어", "등급"]]
    df_연결어미 = df_연결어미[["단어", "등급"]]
    df_전성어미 = df_전성어미[["단어", "등급"]]
    df_종결어미 = df_종결어미[["단어", "등급"]]
    df_조사 = df_조사[["단어", "등급"]]

    rank_dir = "bin/rank"
    df_선어말어미.to_csv(f"{rank_dir}/선어말어미.csv", index=False)
    df_연결어미.to_csv(f"{rank_dir}/연결어미.csv", index=False)
    df_전성어미.to_csv(f"{rank_dir}/전성어미.csv", index=False)
    df_종결어미.to_csv(f"{rank_dir}/종결어미.csv", index=False)
    df_조사.to_csv(f"{rank_dir}/조사.csv", index=False)