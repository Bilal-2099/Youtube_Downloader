import os
import re
import tempfile
import yt_dlp
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings
import zipfile

# Path to ffmpeg folder inside your project
FFMPEG_PATH = os.path.join(settings.BASE_DIR, "ffmpeg", "bin")

def sanitize_filename(name):
    """Remove invalid filename characters."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_page(request):
    return render(request, "index.html")

def download(request):
    if request.method != "POST":
        return HttpResponse("Invalid Request")

    url = request.POST.get("video_url")
    file_format = request.POST.get("format")   # 'video' or 'audio'
    is_playlist = request.POST.get("is_playlist") == "true"

    # Temporary directory for downloads
    temp_dir = tempfile.mkdtemp()
    outtmpl = os.path.join(temp_dir, "%(title)s.%(ext)s")

    # Common yt-dlp options
    ydl_opts = {
        "outtmpl": outtmpl,
        "ffmpeg_location": FFMPEG_PATH,
        "quiet": True,
    }

    # Format options
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

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        if is_playlist:
            # Extract info and download playlist
            info_dict = ydl.extract_info(url, download=True)
            playlist_title = sanitize_filename(info_dict.get("title", "playlist"))

            # Create ZIP file with all downloaded media
            zip_path = os.path.join(temp_dir, f"{playlist_title}.zip")
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for f in os.listdir(temp_dir):
                    if f.endswith(".mp4") or f.endswith(".mp3"):
                        zipf.write(os.path.join(temp_dir, f), f)

            return FileResponse(
                open(zip_path, "rb"),
                as_attachment=True,
                filename=f"{playlist_title}.zip"
            )
        else:
            # Single video/audio download
            info = ydl.extract_info(url, download=True)
            title = sanitize_filename(info.get("title", "download"))
            ext = "mp4" if file_format == "video" else "mp3"
            filepath = os.path.join(temp_dir, f"{title}.{ext}")

            return FileResponse(
                open(filepath, "rb"),
                as_attachment=True,
                filename=f"{title}.{ext}"
            )
