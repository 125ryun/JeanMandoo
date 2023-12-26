import os
import av
import re

def calc_vid_len():
    vid_dir = "data/vid"
    out_dir = "bin/metadata"
    for vid_file in os.listdir(vid_dir):
        vid_name, vid_ext = vid_file.split(".")
        out_file = f"{vid_name}_vid.txt"

        # if already done handling metadata, pass
        if os.path.exists(f"{out_dir}/{out_file}"):
            print("calc_vid_len - pass", vid_file)
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
        with open(f"{out_dir}/{out_file}", "w") as f:
            f.write(str(numerator))
            f.write("\n")
            f.write(str(denominator))

def calc_txt_len():
    txt_dir = "bin/txt"
    out_dir = "bin/metadata"
    for txt_file in os.listdir(txt_dir):
        txt_path = f"{txt_dir}/{txt_file}"
        #out_file = f"{txt_file.split('.')[0]}_txt.txt"
        output_path = f"{out_dir}/{txt_file.split('.')[0]}_txt.txt"

        # if already done handling metadata, pass
        if os.path.exists(f"{out_dir}/{txt_file}"):
            print("calc_txt_len - pass", txt_file)
            continue

        # open txt file
        with open(txt_path, "r", encoding='UTF8') as f:
            document = f.read()
            document = re.sub(r"[^가-힣]", "", document)
            document = re.sub(r"\s", "", document)
            txt_len = len(document)

        with open(output_path, "w") as f:
            f.write(str(txt_len))