# YouTube Downloader (GUI Version)

A Python-based YouTube video and audio downloader with playlist support and a simple graphical interface using Tkinter.  
This project allows you to download single videos or entire playlists from YouTube in **video (MP4)** or **audio (MP3)** format, with a live progress bar and display of the currently downloading video.

Bundled **FFmpeg** ensures the app works without requiring a separate installation.

---

## Features

- Download **single videos** or **entire playlists**  
- Choose download format: **Video (MP4)** or **Audio (MP3)**  
- Tkinter GUI with **progress bar** and current video title display  
- Clean filenames automatically for Windows  
- Cross-platform (Python 3.9+ tested on Windows)  
- Bundled FFmpeg for audio extraction and video merging  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Bilal-2099/Youtube_downloaer.git
cd Youtube_downloaer
```

2. Install the dependency:

```bash
pip install yt-dlp
```

> **Note:** FFmpeg is already included in the `ffmpeg` folder, so you do not need to install it separately.

---

## Usage

Run the GUI script:

```bash
python youtube_downloader_gui.py
```

1. Enter the YouTube video or playlist URL.  
2. Select the download format (`video` or `audio`).  
3. Click **Download**.  
4. The progress bar and label will show the download progress and current video name.

The downloaded files are saved in the `downloads` folder:

```
downloads/
    video/         # For single videos
    audio/         # For single audio
    playlists/
        video/     # Playlist videos
        audio/     # Playlist audios
```

---

## Example

**Single video (audio):**

```
Enter URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Select format: Audio
Downloading audio...
Progress bar updates...
Download complete!
Saved to: downloads/audio
```

**Playlist (video):**

```
Enter URL: https://www.youtube.com/playlist?list=PLxxx
Select format: Video
Downloading playlist...
Progress bar updates...
Download complete!
Saved to: downloads/playlists/video
```

---

## Project Structure

```
Youtube_downloaer/
├─ youtube_downloader_gui.py   # Main GUI script
├─ downloader.py               # Backend downloader logic
├─ ffmpeg/                     # Bundled FFmpeg for audio/video processing
│   └─ bin/
│       ├─ ffmpeg.exe
│       └─ ffprobe.exe
├─ downloads/                  # Folder where videos/audio are saved
└─ README.md                   # Project documentation
```

---

## Skills Demonstrated

- Python scripting and file handling  
- GUI development with Tkinter  
- Handling user input and error management  
- Working with external libraries (`yt-dlp`)  
- Audio/video processing with FFmpeg  
- Playlist and batch processing logic  
- Threading for responsive GUI

---

## License

This project is for learning and portfolio purposes.  
Feel free to use or modify it, but do not redistribute commercially.

