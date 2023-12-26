import os

def score_spm():
    vid_dir = "data/vid"
    out_dir = "out"

    metadata_dir = "bin/metadata"

    # for vid_file in os.listdir(vid_dir):
    for vid_file in os.listdir("bin/txt"):
        vid_name, vid_ext = vid_file.split(".")
        output_path = f"{out_dir}/{vid_name}_score_spm.txt"
        if os.path.exists(output_path):
            continue
        
        with open(f"{metadata_dir}/{vid_name}_vid.txt", "r") as f:
            fraction = f.readlines()
            num = int(fraction[0].strip())
            denom = int(fraction[1])

        with open(f"{metadata_dir}/{vid_name}_txt.txt", "r") as f:
            syllables = int(f.readline())

        score = float(syllables / (num / denom))

        with open(output_path, "w") as f:
            f.write(str(score))