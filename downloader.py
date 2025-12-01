import yt_dlp
import os
import re
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------
# Backend: Downloader
# ------------------------
def make_folder(path):
    os.makedirs(path, exist_ok=True)

def clean_title(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_with_ytdlp(url, mode="video", hook=None):
    mode = mode.lower()
    if mode not in ["video", "audio"]:
        mode = "video"

    is_playlist = "playlist" in url or "list=" in url
    base_folder = "downloads"
    folder = os.path.join(base_folder, "playlists", mode) if is_playlist else os.path.join(base_folder, mode)
    make_folder(folder)

    def default_progress(d):
        if d["status"] == "downloading":
            p = d.get("_percent_str", "").strip()
            s = d.get("_speed_str", "").strip()
            print(f"\r{p} | {s}", end="")
        elif d["status"] == "finished":
            print("\nFinalizing...")

    common_opts = {
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "noplaylist": False,
        "progress_hooks": [hook] if hook else [default_progress],
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
    else:  # video
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
# Frontend: Tkinter GUI
# ------------------------
def start_download_thread():
    """Run download in a separate thread to keep GUI responsive"""
    threading.Thread(target=start_download).start()

def progress_hook(d):
    """Update GUI progress bar and label"""
    if d["status"] == "downloading":
        percent_str = d.get("_percent_str", "").strip()
        percent = float(percent_str.replace("%", "")) if percent_str else 0
        progress_var.set(percent)
        filename = d.get("filename", "Unknown")
        filename = os.path.basename(filename)
        video_label.config(text=f"Downloading: {filename}")
    elif d["status"] == "finished":
        video_label.config(text="Finalizing...")

def start_download():
    url = url_entry.get().strip()
    mode = mode_var.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    try:
        download_with_ytdlp(url, mode, hook=progress_hook)
        progress_var.set(100)
        video_label.config(text="Download complete!")
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\n{e}")

# ------------------------
# Tkinter Window
# ------------------------
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("500x250")

tk.Label(root, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

tk.Label(root, text="Format:").pack(pady=5)
mode_var = tk.StringVar(value="video")
tk.Radiobutton(root, text="Video", variable=mode_var, value="video").pack()
tk.Radiobutton(root, text="Audio", variable=mode_var, value="audio").pack()

tk.Button(root, text="Download", command=start_download_thread).pack(pady=10)

video_label = tk.Label(root, text="No download in progress")
video_label.pack(pady=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, length=400, variable=progress_var)
progress_bar.pack(pady=10)

root.mainloop()
