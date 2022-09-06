import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

# グラフ化したい音楽のアーティスト名と曲名を事前に入力しておく
artists = ["{アーティスト1}", "{アーティスト2}", "{アーティスト3}"]
tracks = [["{アーティスト1の曲名1}", "{アーティスト1の曲名2}", "{アーティスト1の曲名3}"], ["{アーティスト2の曲名1}", "{アーティスト2の曲名2}", "{アーティスト2の曲名3}"], ["{アーティスト3の曲名1}", "{アーティスト3の曲名2}", "{アーティスト3の曲名3}"]]

# オーディオファイルを読み込んでグラフ化 → spectrumフォルダにjpgで保存
for i in range(0, len(artists)):
    for track in tracks[i]:
        file_number = 1
        while os.path.isfile("./music/" + artists[i] + f"/{track}_{file_number}" + ".mp3"):
            file_dir = "./music/" + artists[i] + f"/{track}_{file_number}" + ".mp3"
            export_dir = "./music/" + artists[i] + "/spectrum/" + f"{track}_{file_number}" + ".jpg"
            y, sr = librosa.audio.load(file_dir)

            S = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, win_length=512, hop_length=512)
            # dB単位に変換
            S_dB = librosa.power_to_db(S, ref=np.max)
            plt.figure(figsize=(8, 8))
            librosa.display.specshow(S_dB, y_axis='mel', sr=sr, x_axis='time')
            plt.savefig(export_dir)

            file_number += 1