import os
import av
import re

def calc_vid_len():
    vid_dir = "data/vid"
    out_dir = "bin/metadata"
    for vid_file in os.listdir(vid_dir):
        vid_name, vid_ext = vid_file.split(".")
        output_path = f"{out_dir}/{vid_name}_vid.txt"

        # if already done handling metadata, pass
        if os.path.exists(output_path):
            continue

        # import video
        container = av.open(f"{vid_dir}/{vid_file}")
        video = container.streams.video[0]

        # calc video length(min)
        time_base = video.time_base # 1 / frame_rate
        duration = video.duration # # of frame

        numerator = duration # 분자
        denominator = 60 / time_base # 분모

        # write video length(min) in float
        with open(output_path, "w", encoding='UTF8') as f:
            f.write(str(numerator))
            f.write("\n")
            f.write(str(denominator))
            
        print(f"video 재생시간 계산 완료: {output_path}")

def calc_txt_len():
    txt_dir = "bin/txt"
    out_dir = "bin/metadata"
    for txt_file in os.listdir(txt_dir):
        txt_name, txt_ext = txt_file.split(".")
        txt_path = f"{txt_dir}/{txt_file}"
        output_path = f"{out_dir}/{txt_name}_txt.txt"

        # if already done handling metadata, pass
        if os.path.exists(output_path):
            continue

        # open txt file
        with open(txt_path, "r", encoding='UTF8') as f:
            document = f.read()
            document = re.sub(r"[^가-힣]", "", document)
            document = re.sub(r"\s", "", document)
            txt_len = len(document)

        with open(output_path, "w", encoding='UTF8') as f:
            f.write(str(txt_len))
            
        print(f"text 음절 수 계산 완료: {output_path}")
        