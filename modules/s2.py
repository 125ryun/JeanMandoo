import os

def score_spm():
    vid_dir = "data/"
    out_dir = "bin/score/"

    metadata_dir = "bin/metadata/"

    # for vid_file in os.listdir(vid_dir):

    for vid_file in os.listdir("bin/txt"):
        vid_name, vid_ext = vid_file.split(".")
        
        with open(metadata_dir + vid_name + "_vid.txt", "r") as f:
            fraction = f.readlines()
            num = int(fraction[0].strip())
            denom = int(fraction[1])

        with open(metadata_dir + vid_name + "_txt.txt", "r") as f:
            syllables = int(f.readline())

        score = float(syllables / (num / denom))

        with open(out_dir + vid_name + "_scr2.txt", "w") as f:
            f.write(str(score))