import os  # For file and folder operations
import tempfile  # To create temporary directories
import yt_dlp  # Library to download videos/audio from YouTube
from django.http import FileResponse, HttpResponse  # Django responses for files and text
from django.shortcuts import render  # To render HTML templates
import zipfile  # To create zip files
import re  # Regular expressions for text processing
import imageio_ffmpeg as ffmpeg  # To handle audio/video conversion

# Get the path to the ffmpeg executable for conversions
FFMPEG_PATH = ffmpeg.get_ffmpeg_exe()


# Function to remove invalid characters from filenames
def sanitize_filename(name):
    # Remove characters that are not allowed in filenames
    return re.sub(r'[\\/*?:"<>|]', "", name)


# View to render the main page with the form
def download_page(request):
    return render(request, "index.html")


# View to handle the download request
def download(request):
    # Only accept POST requests (when form is submitted)
    if request.method != "POST":
        return HttpResponse("Invalid Request")

    # Get the video URL and format from the form
    url = request.POST.get("video_url")
    file_format = request.POST.get("format")   # Either 'video' or 'audio'
    is_playlist = request.POST.get("is_playlist") == "true"  # Check if user wants a playlist download

    # Create a temporary directory to store downloads
    temp_dir = tempfile.mkdtemp()

    # Basic options for yt-dlp
    ydl_opts = {
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),  # Save files with their title in temp dir
        "ffmpeg_location": FFMPEG_PATH,  # Path to ffmpeg for conversions
        "quiet": True,  # Suppress console output
    }

    # Update options based on user's choice of video or audio
    if file_format == "video":
        ydl_opts.update({
            "format": "bestvideo+bestaudio/best",  # Download best quality video + audio
            "merge_output_format": "mp4",  # Merge video/audio into MP4
        })
    else:
        ydl_opts.update({
            "format": "bestaudio/best",  # Download best quality audio
            "postprocessors": [{  # Convert downloaded audio to mp3
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })

    try:
        # Use yt-dlp to download the video/audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)  # Download and get metadata

            if is_playlist:
                # If it's a playlist, we need to zip all files
                playlist_title = sanitize_filename(info.get("title", "playlist"))  # Safe filename
                zip_path = os.path.join(temp_dir, f"{playlist_title}.zip")  # Path for zip file

                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                    # Loop through each video in the playlist
                    for entry in info.get('entries', []):
                        file_path = ydl.prepare_filename(entry)  # Get downloaded filename
                        if file_format == "audio":
                            file_path = os.path.splitext(file_path)[0] + ".mp3"  # Change extension if audio
                        if os.path.exists(file_path):  # Check if file exists
                            zipf.write(file_path, os.path.basename(file_path))  # Add file to zip
                
                # Return the zip file as a downloadable response
                return FileResponse(open(zip_path, "rb"),
                                    as_attachment=True,
                                    filename=f"{playlist_title}.zip")

            else:
                # Single video/audio file download
                file_path = ydl.prepare_filename(info)  # Get downloaded filename
                if file_format == "audio":
                    file_path = os.path.splitext(file_path)[0] + ".mp3"  # Change extension if audio

                # Return the file as a downloadable response
                return FileResponse(open(file_path, "rb"),
                                    as_attachment=True,
                                    filename=os.path.basename(file_path))
    except Exception as e:
        # If any error occurs, show it as plain text
        return HttpResponse(f"Error: {str(e)}")
