# YouTube Downloader (CLI Version)

A simple Python-based YouTube downloader for videos and audio, including full playlist support.  
This command-line tool allows downloading single videos or entire playlists in **video (MP4)** or **audio (MP3)** format, with live progress and video title display.

Bundled **FFmpeg** ensures the app works on systems without needing a separate installation.

---

## Features

- Download **single videos** or **entire playlists**
- Choose download format: **Video (MP4)** or **Audio (MP3)**
- Shows progress percentage, download speed, and current video title in terminal
- Clean filenames automatically for Windows
- Bundled FFmpeg for audio extraction and video merging
- Simple command-line interface

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

> **Note:** FFmpeg is already included in the `ffmpeg` folder, so no separate installation is needed.

---

## Usage

Run the script:

```bash
python downloader.py
```

1. Enter the YouTube video or playlist URL.  
2. Select the download format (`video` or `audio`).  
3. The terminal will display download progress and the video title.
4. The downloaded files are saved in the `downloads` folder:

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
Enter format: audio
Downloading audio...
45% | 1.2MiB/s | Rick Astley - Never Gonna Give You Up.mp3
Download complete!
Saved to: downloads/audio
```

**Playlist (video):**

```
Enter URL: https://www.youtube.com/playlist?list=PLxxx
Enter format: video
Downloading playlist...
10% | 2.3MiB/s | Video 1.mp4
25% | 1.8MiB/s | Video 2.mp4
...
Download complete!
Saved to: downloads/playlists/video
```

---

## Project Structure

```
Youtube_downloaer/
├─ downloader.py             # Main CLI downloader script
├─ ffmpeg/                   # Bundled FFmpeg for audio/video processing
│   └─ bin/
│       ├─ ffmpeg.exe
│       └─ ffprobe.exe
├─ downloads/                # Folder where videos/audio are saved
└─ README.md                 # Project documentation
```

---

## Skills Demonstrated

- Python scripting and file handling
- Playlist and batch processing
- Working with external libraries (`yt-dlp`)
- Audio/video processing with FFmpeg
- Command-line interface design
- Clean, professional coding style for portfolio showcase

---

## License

This project is for learning and portfolio purposes.  
Feel free to use or modify it, but do not redistribute comme