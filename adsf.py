import os
import re
import pandas as pd
# dir = "bin/txt"
# for file in os.listdir(dir):
#     if file.startswith("dummy"):
#         lines = []
#         document = ""
        
#         with open(f"{dir}/{file}", "r") as f:
#             lines = f.readlines()
#         lines = lines[1::2]
#         for i, line in enumerate(lines):
#             index = line.find(":")
#             if index != -1 and index < 10:
#                 lines[i] = line[index+1:]

#         document = " ".join(lines)

#         with open(f"{dir}/{file}", "w") as f:
#             f.write(document)

data = pd.read_csv("data/rank/syntax.csv")
df = pd.DataFrame(data)
df = df.iloc[:,:6]

for i, row in enumerate(df.iloc()):
    row["대표형"] = row["대표형"].lstrip("-").rstrip("-")
    if row["관련형"] != "":
        related = row["관련형"].split(",")
        related = [word.lstrip("-").rstrip("-") for word in related]
        
        rank = row["등급"]
        cat = row["분류"]
        inter = row["국제통용 (2단계)"]
        educat = row["문법.표현 교육내용개발(1-4단계)"]
        
        for word in related:
            df.append([rank, cat, word, "", inter, educat])
        row["관련형"] = ""

df.to_csv("data/rank/syntax.csv")