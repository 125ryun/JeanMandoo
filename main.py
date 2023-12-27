# import modules
import os
from modules import format, convert, metadata, score

ROOT_PATH = os.getcwd()
format.format_syntax_rank()

# video -> audio(speech) -> text
convert.vid_to_aud()
convert.aud_to_txt()

# video(speech), text 메타 데이터 연산
metadata.calc_vid_len() # 영상 길이(min)의 분자, 분모를 차례대로 각 줄에 저장
metadata.calc_txt_len() # 텍스트 어절 수를 저장

# 평가 준거별로 점수 산출
score.score_spm() # 발화 속도(spm)
score.tagpos(ROOT_PATH) # 통사적 복잡성 & 동음이의어, 다의어 출현