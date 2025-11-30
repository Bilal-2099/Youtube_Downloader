import yt_dlp
import os

def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def download_media(url, mode="video"):
    # Output folder based on mode
    folder = "downloads/audio" if mode == "audio" else "downloads/video"
    make_folder(folder)

    ydl_opts = {
        "outtmpl": f"{folder}/%(title)s.%(ext)s",

        # Fix for YouTube new JS signature system
        "extractor_args": {
            "youtube": {
                "player_client": ["default"]
            }
        },

        # Prevents timeout & fragment errors
        "retries": 10,
        "fragment_retries": 10,
        "socket_timeout": 30,
        "retry_sleep_functions": {
            "http": lambda n: 2 ** n,
            "fragment": lambda n: 2 ** n,
        },

        # Use ffmpeg for audio extraction
        "postprocessors": []
    }

    # Audio settings
    if mode == "audio":
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"].append({
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        })
    else:
        # Best video + best audio merge
        ydl_opts["format"] = "bv*+ba/b"

        ydl_opts["postprocessors"].append({
            "key": "FFmpegVideoRemuxer",
            "preferedformat": "mp4",
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"\n✔ Download complete: {info.get('title')}")
            return True
    except Exception as e:
        print("\n❌ Error occurred:", str(e))
        return False


def download_playlist(url, mode="video"):
    folder = "downloads/playlist_audio" if mode == "audio" else "downloads/playlist_video"
    make_folder(folder)

    ydl_opts = {
        "outtmpl": f"{folder}/%(playlist_title)s/%(title)s.%(ext)s",

        "extractor_args": {
            "youtube": {
                "player_client": ["default"]
            }
        },

        "retries": 10,
        "fragment_retries": 10,
        "socket_timeout": 30,
        "retry_sleep_functions": {
            "http": lambda n: 2 ** n,
            "fragment": lambda n: 2 ** n,
        },

        "ignoreerrors": True,
        "postprocessors": []
    }

    if mode == "audio":
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"].append({
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3"
        })
    else:
        ydl_opts["format"] = "bv*+ba/b"
        ydl_opts["postprocessors"].append({
            "key": "FFmpegVideoRemuxer",
            "preferedformat": "mp4",
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("\n✔ Playlist download complete.")
    except Exception as e:
        print("\n❌ Playlist Error:", str(e))

download_media("https://www.youtube.com/watch?v=II2EO3Nw4m0", mode="video")