# YouTube Downloader

A simple Python-based YouTube video and audio downloader with playlist support.  
This project allows you to download single videos or entire playlists from YouTube in either **video (MP4)** or **audio (MP3)** format.  

It also includes support for bundled **FFmpeg**, so it can work on Windows systems without FFmpeg installed globally.

---

## Features

- Download **single videos** or **entire playlists**  
- Choose download format: **Video (MP4)** or **Audio (MP3)**  
- Clean filenames automatically for Windows  
- Cross-platform (Python 3.9+ tested on Windows)  
- Bundled FFmpeg support for audio extraction and merging  

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

Run the main script:

```bash
python downloader.py
```

1. Enter the YouTube video or playlist URL when prompted.  
2. Choose the download format (`video` or `audio`).  
3. The downloaded files will be saved in the `downloads` folder:

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
Enter the URL (video or playlist): https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter format (video/audio) [default: video]: audio
Downloading audio...
Saved to: downloads/audio
```

**Playlist (video):**

```
Enter the URL (video or playlist): https://www.youtube.com/playlist?list=PLxxx
Enter format (video/audio) [default: video]: video
Downloading playlist...
Saved to: downloads/playlists/video
```

---

## Project Structure

```
Youtube_downloaer/
├─ downloader.py        # Main script
├─ ffmpeg/             # Bundled FFmpeg for audio extraction/merging
│   └─ bin/
│       ├─ ffmpeg.exe
│       └─ ffprobe.exe
├─ downloads/          # Folder where videos/audio are saved
└─ README.md           # Project documentation
```

---

## Skills Demonstrated

- Python scripting and file handling  
- Handling user input and error management  
- Working with external libraries (`yt-dlp`)  
- Audio/video processing with FFmpeg  
- Playlist and batch processing logic  

---

## License

This project is for learning and portfolio purposes.  
Feel free to use or modify it, but do not redistribute commercially.