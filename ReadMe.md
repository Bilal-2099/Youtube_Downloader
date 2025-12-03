# Downloader Tube

Downloader Tube is a YouTube downloader project built in **two versions**:

1. **Web Version (Django)** – Download videos or audio directly from a web browser. Supports playlists and automatic MP3 conversion.
2. **CLI Version (Python)** – Download videos, audio, or playlists from the command line with real-time progress and download speed display. FFmpeg is bundled.

---

## Features

### Web Version

* Download YouTube videos in MP4 format.
* Download YouTube audio in MP3 format.
* Download entire playlists as a ZIP file.
* Loading spinner shows progress while processing.
* Simple, clean web interface.

### CLI Version

* Command-line interface for videos, audio, and playlists.
* Shows download progress %, speed, and current video title in terminal.
* Automatic filename cleanup for Windows.
* Built-in FFmpeg for merging video/audio and audio extraction.
* Lightweight, no extra setup for FFmpeg.

---

## Installation

### Web Version

1. Clone the repository:

```bash
git clone <your-web-repo-url>
cd downloader_tube
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
python manage.py runserver
```

5. Open browser at `http://127.0.0.1:8000/`

### CLI Version

1. Clone the repository:

```bash
git clone https://github.com/Bilal-2099/Youtube_downloaer.git
cd Youtube_downloaer
```

2. Install the required dependency:

```bash
pip install yt-dlp
```

> FFmpeg is included in the `ffmpeg/` directory — no extra setup required.

---

## Usage

### Web Version

1. Open the homepage.
2. Paste a YouTube URL in the input field.
3. Choose the format: **Video (MP4)** or **Audio (MP3)**.
4. Click **Download**.
5. Playlists will download as a ZIP file containing all videos/audio.

### CLI Version

1. Run the downloader:

```bash
python downloader.py
```

2. Enter the YouTube URL (video or playlist).
3. Select format: `video` or `audio`.
4. Files will be saved in:

```
downloads/
    video/
    audio/
    playlists/
        video/
        audio/
```

---

## Examples

### Web Version

* Single video → MP3
  Downloads directly to your browser.

* Playlist → MP4
  Downloads as a ZIP containing all MP4 files.

### CLI Version

* Single Video → MP3

```
Enter URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter format: audio
Downloading audio...
45% | 1.2MiB/s | Rick Astley - Never Gonna Give You Up.mp3
Saved to: downloads/audio
```

* Playlist → MP4

```
Enter URL: https://www.youtube.com/playlist?list=PLxxx
Enter format: video
Downloading playlist...
10% | 2.3MiB/s | Video 1.mp4
27% | 1.9MiB/s | Video 2.mp4
Saved to: downloads/playlists/video
```

---

## Project Structure

### Web Version

```
downloader_tube/
├── templates/
│   └── index.html       # Main page with form
├── views.py             # Handles download logic
├── urls.py              # URL routing
├── static/              # (Optional) CSS/JS
├── manage.py
└── README.md
```

### CLI Version

```
Youtube_downloaer/
├─ downloader.py          # CLI script
├─ ffmpeg/
│   └─ bin/
│       ├─ ffmpeg.exe
│       └─ ffprobe.exe
├─ downloads/
└─ README.md
```

---

## How It Works

### Web Version

1. User submits a URL and format on the homepage.
2. Django view receives the POST request.
3. `yt-dlp` downloads the video/audio; FFmpeg converts audio to MP3.
4. Single files are returned directly; playlists are zipped first.
5. User downloads the file(s) from the browser.

### CLI Version

1. User enters a URL and format in terminal.
2. `yt-dlp` downloads content, FFmpeg converts audio if needed.
3. Progress, speed, and current video title are displayed in real-time.
4. Files are organized in `downloads/` folder.

---

## Skills Demonstrated

* Python scripting
* Django web development
* Handling POST requests and forms
* File management and temporary directories
* Using `yt-dlp` for media extraction
* FFmpeg for audio/video processing
* Batch and playlist automation
* CLI and web interface development

---

## Author

Made by **Bilal**

---

## License

Open-source project for learning and portfolio purposes.
Feel free to modify for personal projects.
