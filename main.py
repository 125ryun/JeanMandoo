# import modules
from modules import convert, metadata, s2

# video(speech) -> text
## transcribe ... 표준 발음
## transcribe ... 들리는 대로

# video(speech), text 메타 데이터 연산
# metadata.calc_vid_len() # 영상 길이(min)의 분자, 분모를 차례대로 각 줄에 저장
# convert.vid_to_aud()
convert.aud_to_txt()
metadata.calc_txt_len() # 텍스트 어절 수를 저장

# 평가 준거별로 점수 산출
## 음운 변동
## 발화 속도(spm)
s2.score_spm()
## 통사적 복잡성

# 최종 점수 산출