# pip install pytube
from pytube import YouTube
url ='https://youtu.be/6MgsHSAcI9k?si=gSm13TkPUJ76hZmW'
yt = YouTube(url)


stream = yt.streams.get_lowest_resolution()
stream.download()
print("Download Completed")
