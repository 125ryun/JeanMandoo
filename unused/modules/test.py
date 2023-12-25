# from jamo import hangul_to_jamo,j2h
from jamo import hangul_to_jamo,j2h, h2j, j2hcj

#음절의 끝소리규칙
def end_sound_rule(text):
    flag=['' for _ in range(len(text))]
    

    for t in range(len(text)-2):
        
        # ㅎ받침 처리 종성 ㅎ,ㄶ, ㅀ 뒤의 자음 ㄱ, ㄷ,ㅂ,ㅈ 이 거센소리 ㅋ,ㅌ,ㅍ,ㅊ 로 바뀌고 ㅎ이 사라짐
        
        hflag=0
        if text[t] in [chr(0x11c2),chr(0x11ad),chr(0x11b6)]:#종성 ㅎ,ㄶ,ㅀ 이라면
            if text[t+1] ==chr(0x1100): # 초성 ㄱ
                text[t+1]=chr(0x110f) # 초성 ㅋ변환
                hflag=1
                
            elif text[t+1] ==chr(0x1103): # 초성 ㄷ
                text[t+1]=chr(0x1110) # 초성 ㅌ변환
                hflag=1
            
            elif text[t+1] ==chr(0x1107): # 초성 ㅂ
                text[t+1]=chr(0x1111) # 초성 ㅍ변환
                hflag=1
            
            elif text[t+1] ==chr(0x110c): # 초성 ㅈ
                text[t+1]=chr(0x110e) # 초성 ㅊ변환
                hflag=1
            
            elif text[t+1] ==chr(0x1109): # 초성 ㅅ 된소리된다.
                text[t+1]=chr(0x110a) # 초성 ㅆ변환
                hflag=1
                
            
                
                
                
            if text[t]==chr(0x11c2) and hflag==1:# 종성 ㅎ
                text[t]=''#축약

            elif text[t]==chr(0x11ad) and hflag==1:# 종성 ㄶ
                text[t]=chr(0x11ab)#종성 ㄴ 변환

            elif text[t]==chr(0x11b6) and hflag==1:#종성 ㅀ
                text[t]=chr(0x11af)#종성 ㄹ 변환
        
        
        
        
        
        
        if text[t]==chr(0x11c1): #ㅍ 을 ㅂ으로 변환
            text[t]=chr(0x11b8) # ㅂ
            
        if text[t] in [chr(0x11ba),chr(0x11bb),chr(0x11bd),chr(0x11be),chr(0x11c0)]:  #ㅅ,ㅆ,ㅈ,ㅊ,ㅌ 을 ㄷ으로 변환
            text[t]=chr(0x11ae) #ㄷ
        
        if text[t] in [chr(0x11a9),chr(0x11bf)]: #ㄲ,ㅋ 을 ㄱ으로 변환
            text[t]=chr(0x11a8) #ㄱ
            
        if text[t]== chr(0x11b9): # ㅄ 을 ㅂ으로 변환
            flag[t]=chr(0x11b9)  # flag 에 ㅄ 저장
            text[t]=chr(0x11b8)  # ㅂ 
        
        if text[t]== chr(0x11aa): #ㄳ 을 ㄱ으로 변환
            flag[t]=chr(0x11aa)   # flag에 ㄳ 저장
            text[t]=chr(0x11a8)   # ㄱ
        
        if text[t] in [chr(0x11b3),chr(0x11b4)] : # ㄽ , ㄾ 을 ㄹ으로 변환
            if text[t]==chr(0x11b3):
                flag[t]=chr(0x11b3) #flag에 ㄽ 저장
            else:
                flag[t]=chr(0x11b4)# flag에 ㄾ 저장

            text[t]=chr(0x11af)   # ㄹ
            
            
        if text[t]== chr(0x11ac): # ㄵ 을 ㄴ으로 변환
            flag[t]=chr(0x11ac)  # flag 에 ㄵ 저장
            text[t]=chr(0x11ab)  # ㄴ 
        
        if text[t] in [chr(0x11b1),chr(0x11b5)]: # ㄻ , ㄿ 을 ㅁ ㅍ으로 변환
            if text[t]==chr(0x11b1):
                flag[t]=chr(0x11b1) #flag에 ㄻ 저장
                text[t]=chr(0x11b7)   # ㅁ
            else:
                flag[t]=chr(0x11b5)# flag에 ㄿ 저장
                text[t]=chr(0x11b8)   # ㅂ
        
        
        if text[t] in [chr(0x11b0),chr(0x11b2)] : # ㄺ, ㄼ 을 ㄹ으로 변환 (불규칙적이지만 허용)
            if text[t]==chr(0x11b0):
                flag[t]=chr(0x11b0) #flag에 ㄺ 저장
                
            else:
                flag[t]=chr(0x11b2)# flag에 ㄼ 저장
            
            text[t]=chr(0x11af)   # ㄹ
        
                
    #겹받침 조건문
    for i in range(len(text)-2):
        if flag[i] !="": # 겹받침 출현
            if text[i+1]==chr(0x110b) and (text[i+2] in [chr(0x1161),chr(0x1165),chr(0x1166),chr(0x1173),chr(0x1175)]): #초성 ㅇ 뒤 중성ㅏ,ㅓ,ㅔ,ㅡ,ㅣ올때
                if flag[i]==chr(0x11b9): #ㅄ 
                    text[i+1]=chr(0x1109) #ㅅ
                    
                elif flag[i]==chr(0x11aa): #ㄳ 
                    text[i+1]=chr(0x1109) #ㅅ
                    
                elif flag[i]==chr(0x11b3): #ㄽ 
                    text[i+1]=chr(0x1109) #ㅅ
                    
                elif flag[i]==chr(0x11b4): #ㄾ 
                    text[i+1]=chr(0x1110) #ㅌ
                    
                elif flag[i]==chr(0x11ac): #ㄵ 
                    text[i+1]=chr(0x110c) #ㅈ
                    
                elif flag[i]==chr(0x11b0): #ㄺ 
                    text[i+1]=chr(0x1100) #ㄱ
                    
                elif flag[i]==chr(0x11b2): #ㄼ 
                    text[i+1]=chr(0x1107) #ㅂ
                    
                elif flag[i]==chr(0x11b5): #ㄿ
                    text[t]=chr(0x11af)   # ㄹ
                    text[i+1]=chr(0x1111) #ㅍ
                    
            elif flag[i] in [chr(0x11b0),chr(0x11b2),chr(0x11ac) ] and (text[i+1] == chr(0x1112)): #종성 ㄺ, ㄼ, ㄵ 초성 ㅎ 
                if flag[i]==chr(0x11b0): #종성 ㄺ
                    text[i+1]=chr(0x110f) #초성 ㅋ
                    
                elif flag[i]==chr(0x11b2): #종성 ㄼ
                    text[i+1]=chr(0x1111) #초성 ㅍ
                
                elif flag[i]==chr(0x11ac): #종성 ㄵ
                    text[i+1]=chr(0x110e) #초성 ㅊ
                    

                    
                    
#구개음화 우선순위 1
def openmouth_sound_rule(text):
    for i in range(len(text)-2):
        
        if text[i]==chr(0x11ae) : #종성이 ㄷ 
            
            if text[i+1]==chr(0x110b) and text[i+2] == chr(0x1175): #초성 ㅇ 뒤 중성 ㅣ올때
                
                text[i]='' #나중에 인풋으로 넘길때는 지워야할 듯 ex)strip
                
                text[i+1]=chr(0x110c) #초성 ㅈ 변환
                
        
        if text[i]==chr(0x11c0) : #종성이 ㅌ
            if text[i+1]==chr(0x110b) and text[i+2] == chr(0x1175): #초성 ㅇ 뒤 중성 ㅣ올때
                
                text[i]='' #나중에 인풋으로 넘길때는 지워야할 듯
    
                text[i+1]=chr(0x110e) #초성 ㅊ 변환
        
        
#연음 우선 순위 2
def relay_sound_rule(text):
    for i in range(len(text)-2):
        if text[i+1]==chr(0x110b) and (text[i+2] in [chr(0x1161),chr(0x1165),chr(0x1166),chr(0x1173),chr(0x1175)]): #초성 ㅇ 뒤 중성ㅏ,ㅓ,ㅔ,ㅡ,ㅣ올때
            
            if text[i]==chr(0x11a8): # 종성 ㄱ
                text[i]=''
                text[i+1]=chr(0x1100) # 초성 ㄱ 변환
                
            if text[i]==chr(0x11a9): # 종성 ㄲ
                text[i]=''
                text[i+1]=chr(0x1101) # 초성 ㄲ 변환
            
            if text[i]==chr(0x11ab): # 종성 ㄴ
                text[i]=''
                text[i+1]=chr(0x1102) # 초성 ㄴ 변환
            
            if text[i]==chr(0x11ae): # 종성 ㄷ
                text[i]=''
                text[i+1]=chr(0x1103) # 초성 ㄷ 변환
            
            if text[i]==chr(0x11af): # 종성 ㄹ
                text[i]=''
                text[i+1]=chr(0x1105) # 초성 ㄹ 변환
            
            if text[i]==chr(0x11b7): # 종성 ㅁ
                text[i]=''
                text[i+1]=chr(0x1106) # 초성 ㅁ 변환
            
            if text[i]==chr(0x11b8): # 종성 ㅂ
                text[i]=''
                text[i+1]=chr(0x1107) # 초성 ㅂ 변환
            
            if text[i]==chr(0x11ba) : #종성이 ㅅ 
                text[i]=''
                text[i+1]=chr(0x1109) # 초성 ㅅ 변환
            
            if text[i]==chr(0x11bb) : #종성이 ㅆ 
                text[i]=''
                text[i+1]=chr(0x110a) # 초성 ㅆ 변환
            
            if text[i]==chr(0x11bd) : #종성이 ㅈ 
                text[i]=''
                text[i+1]=chr(0x110c) # 초성 ㅈ 변환
                
            if text[i]==chr(0x11be) : #종성이  ㅊ
                text[i]=''
                text[i+1]=chr(0x110e) # 초성 ㅊ 변환
            
            if text[i]==chr(0x11bf) : #종성이 ㅋ 
                text[i]=''
                text[i+1]=chr(0x110f) # 초성 ㅋ 변환
            
            if text[i]==chr(0x11c0) : #종성이 ㅌ 
                text[i]=''
                text[i+1]=chr(0x1110) # 초성 ㅌ 변환
            

            if text[i]==chr(0x11c1): # 종성 ㅍ
                text[i]=''
                text[i+1]=chr(0x1111) # 초성 ㅍ 변환
                

#격음화 
def hiet_sound_rule(text):
    for i in range(len(text)-2):
        
                
        if text[i] in [chr(0x11a8),chr(0x11ae),chr(0x11b8),chr(0x11bd)] and text[i+1]==chr(0x1112):#종성 ㄱ,ㄷ,ㅂ,ㅈ 이고 초성이 ㅎ이라면
            if text[i]==chr(0x11a8): #종성 ㄱ
                text[i]='' # 탈락
                text[i+1]=chr(0x110f) #초성 ㅋ
            
            elif text[i]==chr(0x11ae): #종성 ㄷ
                text[i]='' # 탈락
                text[i+1]=chr(0x1110) #초성 ㅌ
                
            elif text[i]==chr(0x11b8): #종성 ㅂ
                text[i]='' # 탈락
                text[i+1]=chr(0x1111) #초성 ㅍ
            
            elif text[i]==chr(0x11bd): #종성 ㅈ
                text[i]='' # 탈락
                text[i+1]=chr(0x110e) #초성 ㅊ
                
                
# 자음 동화
def smooth_sound_rule(text):
    for i in range(len(text)-2):
        if text[i] in [chr(0x11b8),chr(0x11ae),chr(0x11a8)] and text[i+1] in [chr(0x1106),chr(0x1102)] : #종성 ㅂ,ㄷ,ㄱ이 초성 ㅁ,ㄴ 앞에 나오면 ㅁ,ㄴ,ㅇ,으로 바꿈
            if text[i]==chr(0x11b8): # 종성 ㅂ
                text[i]=chr(0x11b7) # 종성 ㅁ 변환
                
            elif text[i]==chr(0x11ae): #종성 ㄷ
                text[i]=chr(0x11ab) #종성 ㄴ 변환
            
            elif text[i]==chr(0x11a8): # 종성 ㄱ
                text[i]=chr(0x11bc) # 종성 ㅇ 변환
                
        elif text[i] in [chr(0x11b7), chr(0x11bc)] and text[i+1]==chr(0x1105) : # 종성 ㅁ, ㅇ 이 초성 ㄹ 앞에 나오면 초성 ㄹ을 ㄴ으로 바꿈
            text[i+1]=chr(0x1102) # 초성 ㄴ 변환
            
        elif text[i]==chr(0x11af) and text[i+1]==chr(0x1102) : #종성 ㄹ 뒤 초성 ㄴ , 초성 ㄴ 이 ㄹ로 변환
            text[i+1]=chr(0x1105)
            
        elif text[i]==chr(0x11ab) and text[i+1]==chr(0x1105) : #종성 ㄴ 뒤 초성 ㄹ , 종성 ㄴ 이 ㄹ로 변환
            text[i]=chr(0x11af)
            
            
            
            
#통합 음운변동 모듈

def total_koreanmoving(text):
    openmouth_sound_rule(text)
    relay_sound_rule(text)
    hiet_sound_rule(text)
    end_sound_rule(text)
    smooth_sound_rule(text)
    return text

def tokenize(text, as_id=False):
    # jamo package에 있는 hangul_to_jamo를 이용하여 한글 string을 초성/중성/종성으로 나눈다.
    
    # for char in text:

    # tokens = list(j2hcj(h2j(text)))
    # print('tokens : ', tokens)
    tokens = list(hangul_to_jamo(text)) # '존경하는'  --> ['ᄌ', 'ᅩ', 'ᆫ', 'ᄀ', 'ᅧ', 'ᆼ', 'ᄒ', 'ᅡ', 'ᄂ', 'ᅳ', 'ᆫ', '~']

    return [token for token in tokens] 
    
def korean_cleaners(text):
    text = tokenize(text) # '존경하는' --> ['ᄌ', 'ᅩ', 'ᆫ', 'ᄀ', 'ᅧ', 'ᆼ', 'ᄒ', 'ᅡ', 'ᄂ', 'ᅳ', 'ᆫ', '~']
     
    # 전민재 자리
    #CNSL전민재 자체 제작 음운변동 모듈
    text=total_koreanmoving(text) 
    text=[_ for _ in text if _ !=''] # 공백제거    
    
    return text

if __name__ == "__main__":
    text="안간힘"
    cleantext=korean_cleaners(text)
    
    print(cleantext)