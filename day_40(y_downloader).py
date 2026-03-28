import yt_dlp

url = "https://youtu.be/6MgsHSAcI9k?si=gSm13TkPUJ76hZmW"

# Download lowest resolution (like your original code)
ydl_opts = {
    'format': 'worstvideo+worstaudio/worst',
    'outtmpl': '%(title)s.%(ext)s',  # saves as video title
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])