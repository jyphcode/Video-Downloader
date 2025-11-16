# Simple Video Downloader
# Author: Joe
# Date: 10/14/2025
#
# Description: 
# This is a simple script designed to download videos using yt_dlp. The script should
# request a link, then download the video onto the folder in which the script
# is located. Since this is limited to the yt_dlp library, only sites similar to YouTube
# can be downloaded.
#
# NOTE: To run this code, you must have yt-dlp installed. You can install this with the
# command: pip install yt-dlp or pip install --user yt-dlp (if permissions is an issue)

import yt_dlp
import sys

def video_downloader(url):
   
    vd_settings = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s', 
        'noplaylist': True, 
        # This uses a HTTP header to attempt to trick web browsers
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        },
    }

    print(f"Attempting to download video from: {url}")

    try:
        with yt_dlp.YoutubeDL(vd_settings) as ydl:
            ydl.download([url])
        print("\nDownload finished\nVideo saved in the same directory as script.")

    except yt_dlp.utils.DownloadError as e:
        print(f"\nAn error occurred during download: {e}")
        print("Check Permissions, URL, and internet connection.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    print("###### Video Downloader by Joe ######")
    print("A simple script designed to download videos using yt_dlp.\n")

    while True:
        video_url = input("Enter video URL to download (or type 'quit' to exit): ")

        if video_url.lower() in ['quit', 'exit']:
            print("Exiting downloader. Goodbye!")

        if not video_url.strip():
            print("URL cannot be empty. Please enter a URL.")

        success = video_downloader(video_url)

        if success:
            another = input("\nDownload another video? (yes/no): ").lower()
            if another not in ['yes', 'y']:
                print("Exiting downloader. Goodbye!")
                break