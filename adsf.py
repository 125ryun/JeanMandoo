import os
import re

dir = "bin/txt"
for file in os.listdir(dir):
    if file.startswith("dummy"):
        lines = []
        document = ""
        
        with open(f"{dir}/{file}", "r") as f:
            lines = f.readlines()
        lines = lines[1::2]
        for i, line in enumerate(lines):
            index = line.find(":")
            if index != -1 and index < 10:
                lines[i] = line[index+1:]

        document = " ".join(lines)

        with open(f"{dir}/{file}", "w") as f:
            f.write(document)