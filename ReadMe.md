# YouTube Downloader (CLI Version)

A clean and simple command-line YouTube downloader built with Python.\
It supports videos, audio, and full playlists --- with real-time
progress, download speed, and the current video title displayed directly
in the terminal.

FFmpeg is bundled inside the project, so no extra installation is
required.

------------------------------------------------------------------------

## Features

-   Download single videos or entire playlists\
-   Choose between **Video (MP4)** or **Audio (MP3)**\
-   Shows progress %, download speed, and current video title\
-   Auto-clean filenames for Windows\
-   Built-in FFmpeg for merging and audio extraction\
-   Simple, lightweight CLI

------------------------------------------------------------------------

## Installation

Clone the repository:

``` bash
git clone https://github.com/Bilal-2099/Youtube_downloaer.git
cd Youtube_downloaer
```

Install the required dependency:

``` bash
pip install yt-dlp
```

> FFmpeg is already included in the `ffmpeg` directory---no setup
> needed.

------------------------------------------------------------------------

## Usage

Run the downloader:

``` bash
python downloader.py
```

Enter: 1. A YouTube URL (video or playlist)\
2. The format: `video` or `audio`

Downloaded files will be stored in:

    downloads/
        video/
        audio/
        playlists/
            video/
            audio/

------------------------------------------------------------------------

## Examples

### Single Video → MP3

    Enter URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Enter format: audio
    Downloading audio...
    45% | 1.2MiB/s | Rick Astley - Never Gonna Give You Up.mp3
    Saved to: downloads/audio

### Playlist → MP4

    Enter URL: https://www.youtube.com/playlist?list=PLxxx
    Enter format: video
    Downloading playlist...
    10% | 2.3MiB/s | Video 1.mp4
    27% | 1.9MiB/s | Video 2.mp4
    Saved to: downloads/playlists/video

------------------------------------------------------------------------

## Project Structure

    Youtube_downloaer/
    ├─ downloader.py
    ├─ ffmpeg/
    │   └─ bin/
    │       ├─ ffmpeg.exe
    │       └─ ffprobe.exe
    ├─ downloads/
    └─ README.md

------------------------------------------------------------------------

## Skills Demonstrated

-   Python scripting\
-   Batch and playlist automation\
-   Using `yt-dlp` for media extraction\
-   Leveraging FFmpeg inside Python\
-   Clean command-line app structure\
-   Portfolio-ready project organization

------------------------------------------------------------------------

## License

This project is for learning and portfolio use.\
Feel free to modify it for personal projects.
