import sys
import os
from ctypes import *

import utagger.bin.utagger as ut

# current_directory = os.path.dirname(__file__)
# parent_directory = os.path.join(current_directory, '..', 'utagger', 'bin', 'utagger')
# sys.path.append(parent_directory)

# # 이제 utagger 모듈을 임포트할 수 있습니다.
# from utagger import Init_Utagger
# # from .utagger.bin import Init_Utagger
# import utagger.bin.utagger as ut
# tagger, lib = Init_Utagger()
tagger, lib = ut.Init_Utagger()

os.chdir("C:/Users/User/source/repos/JeanMandoo")
txt_dir = "bin/txt/"
out_dir = "bin/tagged/"
for txt_file in os.listdir(txt_dir):
    txt_name, txt_ext = txt_file.split(".")
    txt_path = txt_dir + txt_file
    output_path = out_dir + txt_name + ".txt"
    
    # with open(txt_path, "r") as f:
    with open(txt_path, "r", encoding='utf-8') as f:
        text = f.read()
    if len(text) == 0: continue
    
    rt = tagger(0, c_wchar_p(text), 3) # analyze
    print(rt)
    exit(1)
    # print(sentences[0])
    
lib.deleteUCMA(0) # 0번 객체 삭제
lib.Global_release() # 메모리 해제

print("terminate")