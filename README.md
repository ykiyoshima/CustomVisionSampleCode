# 20220912_Azure活用講座サンプルコード
※実際にCustom Visionを使っているのはpredict.pyだけなので、手っ取り早くCustom Visionの使用例をご覧になりたい方はpredict.pyの中身をご参照ください。  
※`librosa`、`youtube_dl`、`matplotlib`などの外部ライブラリを使用しています。ソースコードをご参照の上適宜インストールをお願いいたします。
## 使い方

1. musicフォルダ（音楽ファイルを格納するためのフォルダ）を作成する。  
1. youtube.pyを実行し、欲しい音楽のYouTube URLを入力する。ダウンロードが完了したらファイル名を曲名に変更し、musicフォルダに移動させる。  
1. 2.でダウンロードした音楽のアーティスト名でフォルダを作成する。そのフォルダの中にspectrumフォルダ（音楽を視覚化した画像を格納するためのフォルダ）も作成しておく。  
1. split.pyを実行し、一定時間（デフォルトで10秒）ごとに分割したい音楽のアーティスト名と曲名を入力する。分割は主にデータ数を稼ぐために行っている。  
1. visualize.pyのartistsとtracksに、これまで処理してきた音楽のアーティスト名と曲名をそれぞれ入力しておく。  
1. visualize.pyを実行し、各アーティストフォルダのspectrumフォルダ内にjpgファイルが生成されていることを確認する。
1. 生成されたjpgファイルを用いてCustom Visionで機械学習を行う（講座資料を参照）
1. 1.~6.の手順で予測したい音楽をjpgファイルに処理する。  
1. predict.pyのurlとheadersにCustom Visionで生成したAPIのURLとPrediction-Keyをそれぞれ入力する。  
1. predict.pyを実行し、8.で処理した音楽のアーティスト名と曲名を入力する。
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
├── predict_response.py
├── predict.py
├── README.md
├── split.py
├── visualize.py
└── youtube.py
```