import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  "sample_music" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'},
        {'key': 'FFmpegMetadata'},
    ],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)
info_dict = ydl.extract_info(input("YouTubeのURL："), download=True)