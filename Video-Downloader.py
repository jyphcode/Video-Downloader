# Simple Video Downloader
# Author: JYPH
# Date: 10/14/2025
#
# Description: 
# This is a simple script designed to download videos using yt_dlp. The script should
# request a link, then download the video onto the folder in which the script
# is located. Since this is limited to the yt_dlp library, only sites similar to YouTube
# can be downloaded. I plan to mess around and see if I can add additional
# website support in the future.
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
    }

    print(f"Attempting to download video from: {url}")

    try:
        with yt_dlp.YoutubeDL(vd_settings) as ydl:
            ydl.download([url])
        print("\nDownload finished\nVideo saved in the same directory as script.")

    except yt_dlp.utils.DownloadError as e:
        print(f"\nAn error occurred during download: {e}")
        print("Check URL and internet connection.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    print("###### Video Downloader by JYPH ######\nA simple script designed to download videos using yt_dlp.\n")
    
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter video URL to download: ")

    video_downloader(video_url)

    # Add more content here later for error handling later