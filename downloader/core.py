import yt_dlp
import os

def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path) 

def download_with_ytdlp(url, mode="video"):
    # Sanitize mode input just in case
    mode = mode.lower()
    
    # Define folder paths
    folder = os.path.join("downloads", "audio") if mode == "audio" else os.path.join("downloads", "video")
    make_folder(folder)
    
    # Common options
    common_opts = {
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    if mode == "audio":
        ydl_opts = {
            **common_opts, # Merges with common options
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        # DEFAULT TO VIDEO (Even if typo)
        ydl_opts = {
            **common_opts,
            # IMPROVEMENT: This grabs 1080p/4K by downloading separate streams
            'format': 'bestvideo+bestaudio/best', 
            'merge_output_format': 'mp4',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading {mode}...")
            ydl.download([url])
            print(f"Download complete! Saved to {folder}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ")
    # defaulting to video if the user just hits enter
    format_mode = input("Enter format (video/audio) [default: video]: ").strip().lower() or "video"
    
    download_with_ytdlp(video_url, format_mode)