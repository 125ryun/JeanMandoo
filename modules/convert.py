import os
from moviepy.editor import VideoFileClip
import openai

from modules.KEY import OPENAI_API_KEY

def vid_to_aud():
    vid_dir = "data/vid/"
    out_dir = "bin/audio/"

    for vid_file in os.listdir(vid_dir):
        vid_path = vid_dir + vid_file
        output_path = out_dir + vid_file.split(".")[0] + ".mp3"
        if os.path.exists(output_path):
            continue
        try:
            video_clip = VideoFileClip(vid_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_path)
            print(f"Audio extracted and saved to {output_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

def aud_to_txt():
    openai.api_key = OPENAI_API_KEY

    aud_dir = "bin/audio/"
    out_dir = "bin/txt/"

    for aud_file in os.listdir(aud_dir):
        aud_path = aud_dir + aud_file
        output_path = out_dir + aud_file.split(".")[0] + ".txt"
        if os.path.exists(output_path):
            continue

        with open(aud_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            
            text = transcript['text']
            with open(output_path, "w") as txt_file:
                txt_file.write(text)