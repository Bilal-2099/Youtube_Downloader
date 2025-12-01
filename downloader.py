import yt_dlp
import os
import re

def make_folder(path):
    os.makedirs(path, exist_ok=True)

def clean_title(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_with_ytdlp(url, mode="video"):
    mode = mode.lower()

    if mode not in ["video", "audio"]:
        print("Invalid mode. Defaulting to video.")
        mode = "video"

    # Detect playlist
    is_playlist = "playlist" in url or "list=" in url

    base_folder = "downloads"
    if is_playlist:
        folder = os.path.join(base_folder, "playlists", mode)
    else:
        folder = os.path.join(base_folder, mode)

    make_folder(folder)

    def progress_hook(d):
        if d["status"] == "downloading":
            p = d.get("_percent_str", "").strip()
            s = d.get("_speed_str", "").strip()
            print(f"\r{p} | {s}", end="")
        elif d["status"] == "finished":
            print("\nFinalizing...")

    # FIX: Removed "paths" to stop double folder creation
    common_opts = {
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "noplaylist": False,
        "progress_hooks": [progress_hook],
        "windowsfilenames": True,
        "concurrent_fragment_downloads": 3,
    }

    # AUDIO
    if mode == "audio":
        ydl_opts = {
            **common_opts,
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    # VIDEO
    else:
        ydl_opts = {
            **common_opts,
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        }

    try:
        print("Downloading playlist..." if is_playlist else f"Downloading {mode}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nSaved to: {folder}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = input("Enter the URL (video or playlist): ")
    mode = input("Enter format (video/audio) [default: video]: ").strip().lower() or "video"

    download_with_ytdlp(url, mode)
