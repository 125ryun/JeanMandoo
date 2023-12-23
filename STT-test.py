import os
import khaiii
from khaiii import KhaiiiApi

api=KhaiiiApi()
sentence = "금일 센터 행사로 인해 촬영기기가 마련되어 있지 않습니다."
analyzed = api.analyze(sentence)
for word in analyzed:
    print(word)

exit(1)

import openai
import pydub
from pydub import AudioSegment
# import whisper_client
# from whisper_client import WhisperASRClient

AUDIO_DIR = "./data/"
WHISPER_API_KEY = "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"

def count_syllables(text):
    syllables_count = sum(1 for char in text if 0xac00 <= ord(char) <= 0xd7a3)
    return syllables_count

def calculate_speech_rate(audio_file_path):
    #audio = AudioSegment.from_file(audio_file_path)
    # whisper_client = WhisperASRClient(api_key=WHISPER_API_KEY)
    openai.api_key = WHISPER_API_KEY
    audio_file = open(audio_file_path, "rb")
    #clip_length_seconds = len(audio_file) / 1000
    # transcription_result = whisper_client.transcribe(audio_file_path)
    transcription_result = openai.Audio.transcribe(model="whisper-1", file = audio_file, response_format="srt")
    #
    syllable_count = count_syllables(transcription_result['text'])

    #speech_rate = syllable_count / clip_length_seconds
    return syllable_count

filename = "./data/강의녹음.m4a"
speech_rate = calculate_speech_rate(filename)
print(f"Speech rate for {filename}: {speech_rate}")