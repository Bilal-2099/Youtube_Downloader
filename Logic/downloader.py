import yt_dlp
import os
import re

# ------------------------
# Helper Functions
# ------------------------
def make_folder(path):
    os.makedirs(path, exist_ok=True)

def clean_title(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

# ------------------------
# Main Downloader
# ------------------------
def download_with_ytdlp(url, mode="video"):
    mode = mode.lower()
    if mode not in ["video", "audio"]:
        mode = "video"

    is_playlist = "playlist" in url or "list=" in url
    base_folder = "downloads"
    folder = os.path.join(base_folder, "playlists", mode) if is_playlist else os.path.join(base_folder, mode)
    make_folder(folder)

    def progress_hook(d):
        if d["status"] == "downloading":
            percent_str = d.get("_percent_str", "").strip()
            speed = d.get("_speed_str", "").strip()
            title = os.path.basename(d.get("filename", "Unknown"))
            print(f"\r{percent_str} | {speed} | {title}", end="")
        elif d["status"] == "finished":
            print("\nFinalizing...")

    common_opts = {
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "noplaylist": not is_playlist,
        "progress_hooks": [progress_hook],
        "windowsfilenames": True,
        "concurrent_fragment_downloads": 3,
    }

    if mode == "audio":
        ydl_opts = {
            **common_opts,
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "ffmpeg_location": "./ffmpeg/bin",
        }
    else:
        ydl_opts = {
            **common_opts,
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "ffmpeg_location": "./ffmpeg/bin",
        }

    try:
        print("Downloading playlist..." if is_playlist else f"Downloading {mode}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nSaved to: {folder}")
    except Exception as e:
        print(f"Error: {e}")

# ------------------------
# Command-line Interface
# ------------------------
if __name__ == "__main__":
    url = input("Enter the YouTube URL (video or playlist): ").strip()
    mode = input("Enter format (video/audio) [default: video]: ").strip().lower() or "video"
    download_with_ytdlp(url, mode)
