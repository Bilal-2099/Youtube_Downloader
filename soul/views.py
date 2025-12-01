from django.shortcuts import render
from django.http import StreamingHttpResponse
import yt_dlp
import tempfile
import os

def home(request):
    return render(request, "soul/index.html")

def download_video(request):
    if request.method == "POST":
        video_url = request.POST.get("video_url")
        if not video_url:
            return render(request, "soul/index.html", {"error": "No URL provided."})

        try:
            # Create a temporary file to hold the video
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            temp_file.close()  # We'll let yt-dlp write to it

            # Download using yt-dlp to the temp file
            ydl_opts = {
                'format': 'best',
                'outtmpl': temp_file.name
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            # Stream the file to the user
            def file_iterator(file_path, chunk_size=8192):
                with open(file_path, "rb") as f:
                    while True:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break
                        yield chunk
                os.remove(file_path)  # Clean up temp file after sending

            filename = os.path.basename(temp_file.name)
            response = StreamingHttpResponse(file_iterator(temp_file.name), content_type="video/mp4")
            response['Content-Disposition'] = f'attachment; filename="video.mp4"'
            return response

        except Exception as e:
            return render(request, "soul/index.html", {"error": str(e)})

    return render(request, "soul/index.html")
