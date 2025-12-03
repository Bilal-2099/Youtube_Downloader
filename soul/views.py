import os
import tempfile
import yt_dlp
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import zipfile
import re
import imageio_ffmpeg as ffmpeg

FFMPEG_PATH = ffmpeg.get_ffmpeg_exe()

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_page(request):
    return render(request, "index.html")

def download(request):
    if request.method != "POST":
        return HttpResponse("Invalid Request")

    url = request.POST.get("video_url")
    file_format = request.POST.get("format")   # 'video' or 'audio'
    is_playlist = request.POST.get("is_playlist") == "true"

    temp_dir = tempfile.mkdtemp()

    ydl_opts = {
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
        "ffmpeg_location": FFMPEG_PATH,
        "quiet": True,
    }

    if file_format == "video":
        ydl_opts.update({
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        })
    else:
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if is_playlist:
                playlist_title = sanitize_filename(info.get("title", "playlist"))
                zip_path = os.path.join(temp_dir, f"{playlist_title}.zip")
                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                    # Loop through entries and get the actual downloaded filename
                    for entry in info.get('entries', []):
                        file_path = ydl.prepare_filename(entry)
                        if file_format == "audio":
                            file_path = os.path.splitext(file_path)[0] + ".mp3"
                        if os.path.exists(file_path):
                            zipf.write(file_path, os.path.basename(file_path))
                
                return FileResponse(open(zip_path, "rb"),
                                    as_attachment=True,
                                    filename=f"{playlist_title}.zip")

            else:
                # Single file
                file_path = ydl.prepare_filename(info)
                if file_format == "audio":
                    file_path = os.path.splitext(file_path)[0] + ".mp3"

                return FileResponse(open(file_path, "rb"),
                                    as_attachment=True,
                                    filename=os.path.basename(file_path))
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
