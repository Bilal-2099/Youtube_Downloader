from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=ZWrhh8iMvhE"

ydl_opts = {
    'format': 'best',
    'outtmpl': 'downloads/%(title)s.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

