# 20220912_Azure活用講座サンプルコード

## クイックガイド
※実際にCustom Visionを使っているのはpredict.pyだけです。  
15行目の変数「url」にAPIのURLを、17行目の変数「headers」にAPIのPrediction-KeyとContent-Typeを入力します。  
15行目：`url = {API_URL}`  
17行目：`headers = {"Prediction-Key": {PREDICTION_KEY}}, "Content-Type": {CONTENT_TYPE}}`  
35行目で実際にAPIリクエストを送信し、変数「res」にレスポンスデータを格納します。  
35行目：`res = requests.post(url, image, headers=headers)`  
レスポンスデータは`[{'probability': xxx, 'tagId': 'xxx', 'tagName': 'xxx'}, {'probability': xxx, 'tagId': 'xxx', 'tagName': 'xxx'}]`のような形で返ってきますので、必要に応じてデータを処理してみてください。  
※`librosa`、`matplotlib`、`numpy`などの外部ライブラリを使用しています。ソースコードをご参照の上適宜インストールをお願いいたします。
## 使い方

1. musicフォルダを作成し、手持ちの音楽ファイル（mp3で統一することを推奨）をmusicフォルダ直下に格納する。
1. 2.で用意した音楽のアーティスト名でフォルダを作成する。そのフォルダの中にspectrumフォルダ（音楽を視覚化した画像を格納するためのフォルダ）も作成しておく。  
1. split.pyを実行し、一定時間（デフォルトで10秒）ごとに分割したい音楽のアーティスト名と曲名（ファイル名）を入力する。分割は主にデータ数を稼ぐために行っている。  
1. visualize.pyのartistsとtracksに、これまで処理してきた音楽のアーティスト名と曲名（ファイル名）をそれぞれ入力しておく。  
1. visualize.pyを実行し、各アーティストフォルダのspectrumフォルダ内にjpgファイルが生成されていることを確認する。
1. 生成されたjpgファイルを用いてCustom Visionで機械学習を行う（講座資料を参照）
1. 1.~6.の手順で予測したい音楽も同様にjpgファイルに処理する。  
1. predict.pyのurlとheadersにCustom Visionで生成したAPIのURLとPrediction-Keyをそれぞれ入力する。  
1. predict.pyを実行し、8.で処理した音楽のアーティスト名と曲名（ファイル名）を入力する。
1. AIが学習データに基づき、その音楽がどのアーティストっぽいか分析する。  

## ファイル構成イメージ
```
.
├── music
│   ├── artist01
│   │    ├── spectrum
│   │    │    ├── image01
│   │    │    ├── image02
│   │    │    └── image03
│   │    ├── splitted_track01
│   │    ├── splitted_track02
│   │    └── splitted_track03
│   ├── artist02
│   │    ├── spectrum
│   │    │    ├── image01
│   │    │    ├── image02
│   │    │    └── image03
│   │    ├── splitted_track01
│   │    ├── splitted_track02
│   │    └── splitted_track03
│   ├── artist03
│   │    ├── spectrum
│   │    │    ├── image01
│   │    │    ├── image02
│   │    │    └── image03
│   │    ├── splitted_track01
│   │    ├── splitted_track02
│   │    └── splitted_track03
│   ├── full_track01
│   ├── full_track02
│   └── full_track03
├── .env
├── .gitignore
├── predict.py
├── README.md
├── split.py
├── visualize.py
```