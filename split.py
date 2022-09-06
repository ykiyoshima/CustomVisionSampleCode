import librosa
import librosa.display
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import os

file_name = input("曲名を入力：")
artist_name = input("アーティスト名を入力")
file_index = 1
pre_time = 0
# 10秒（10000msec）ごとに分割
rea_time = 10000

file_dir = "./music/" + file_name + ".mp3"
music, fs = librosa.audio.load(file_dir)
# play_time内の分母の数字は分割する時間（sec）にする（10秒ごとに分割するなら10）
play_time = int(librosa.samples_to_time(len(music), fs)/10)

for k in range(play_time):
    audio_data = AudioSegment.from_file(file_dir, format="mp3")
    split_audio = audio_data[pre_time:rea_time]
    # 10秒（10000msec）ごとに分割
    pre_time += 10000
    rea_time += 10000
    
    split_audio.export("./music/" + artist_name + "/" + file_name + "_" + str(file_index) + ".mp3", format = "mp3")
    
    file_index += 1