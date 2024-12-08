import os
from yt_dlp import YoutubeDL


def download_youtube_video(url, output_path="."):
    try:
        # Define download options
        ydl_opts = {
            # Download 1080p with audio
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            # Save file as video title
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Ensure combined format is MP4
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video

        print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
video_url = input("Enter YouTube video URL: ")
download_youtube_video(video_url, output_path=".")
