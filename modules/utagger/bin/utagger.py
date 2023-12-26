#-*- coding: utf-8 -*-
import sys
import os
from ctypes import *
from ctypes import cdll

def Init_Utagger(root_path):
    print("python call utagger function")
    
    lib = cdll.LoadLibrary(f"{root_path}/modules/utagger/bin/UTaggerR64.dll") # dll 로드 윈도우
    
    hlx_pass = os.path.join( os.path.dirname(sys.argv[0]), f"{root_path}/modules/utagger/Hlxcfg.txt")
    hlx_pass = os.path.abspath(hlx_pass)
    cstr_hlx = c_char_p( hlx_pass.encode('cp949') )#hlxcfg 파일 경로를 cp949로 인코딩.

    lib.Global_init2.restype = c_wchar_p #유태거 초기화 함수의 반환자 정의

    os.chdir(f"{root_path}/modules/utagger/bin")
    msg = lib.Global_init2(cstr_hlx , 0) # Hlxcfg.txt 위치 지정. 학습 파일 로딩. 오래걸림.

    if msg != '': # Hlxcfg.txt와 모든 학습 파일을 읽었는지 확인.
        print("hlxcfg bug")
        print(msg)
        sys.exit(1)

    lib.newUCMA2.restype = c_wchar_p #ucma 생성 함수의 반환자 정의
    msg = lib.newUCMA2(0) # 유태거의 0번 객체 생성(0~99까지 생성 가능)
    if msg != '':
        print("newUCMA bug")
        print(msg)
        sys.exit(1)

    lib.cmaSetNewlineN(0) #유태거 tag_line이 newline을 만들 때 /r/n 이 아니라 /n이 되게 한다.
    #dll의 태깅함수 정의. 사용하기 편하게.
    tag_line = lib.cma_tag_line_BSP #함수 가져오기
    tag_line.restype = c_wchar_p #반환자 설정.

    os.chdir(f"{root_path}")
    
    return tag_line, lib