# Video-Downloader
This is a simple script designed to download videos using yt-dlp.

Things to fix: 
1.) more video support (need more testing)
2.) error when video requires login (ex. age restricted)
3.) add ability download with different settings (atm, only has best quality available)

notes:
I noticed that yt-dlp doesn't allow us to download videos from certain websites. After some research,
I believe the issue is due to some websites actively blocking yt-dlp by identifying these requests as coming
from an automated script (and not browser itself) and then denying access. More investigation is needed.

My goal next is to try and circumvent this issue by allowing my script to download from any website.
I will continue to research how this can be done. Hopefully I can find a solution in the coming days.

version 1.1
Added simple video downloader script