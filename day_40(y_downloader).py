import yt_dlp

url = "https://youtu.be/6MgsHSAcI9k"

ydl_opts = {
    'format': 'worst',
    'outtmpl': '%(title)s.%(ext)s',
    'cookiefile': r'C:\Users\anonymous\Desktop\cookies.txt',
    'extractor_args': {
        'youtube': {
            'player_client': ['web'],  # uses JS runtime (Node.js)
        }
    },
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])