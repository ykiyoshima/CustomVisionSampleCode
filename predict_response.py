import requests
import json
import os
from os.path import join, dirname
import time
import statistics
from dotenv import load_dotenv
from pprint import pprint

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Custom Visionで発行したAPIのURL
url = os.environ.get("PREDICTION_URL")
# Custom Visionで発行したAPIのPrediction-Keyと、リクエストで送信する画像ファイルの形式に応じたContent-Type
headers = {"Prediction-Key": os.environ.get("PREDICTION_KEY"), "Content-Type": "application/octet-stream"}
file_number = 1
bump_probability_array = []
ado_probability_array = []
larc_probability_array = []
siina_probability_array = []
sekai_probability_array = []

artist = input("分析したい音楽のアーティスト名を入力：")
track = input("分析したい音楽の曲名を入力：")

while os.path.isfile(f"./music/{artist}/spectrum/{track}_{file_number}.jpg"):
    #POSTするファイルの読込
    f = open(f"./music/{artist}/spectrum/{track}_{file_number}.jpg", "rb")
    image = f.read()
    f.close()

    # Custom Visionで発行したAPIにリクエストを送信し、レスポンスを取得
    res = requests.post(url, image, headers=headers)
    predictions_array = [] + json.loads(res.text)["predictions"]
    # 1秒あたりのリクエスト回数制限に引っかからないよう、1リクエストごとに何もしない時間を少し（今回は0.2秒）設ける
    time.sleep(0.2)
    
    print("")
    pprint(predictions_array)

    file_number += 1