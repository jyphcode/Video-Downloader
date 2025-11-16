# Video-Downloader
This is a simple script designed to download videos using yt-dlp.

Things to fix: 
1.) more video support (need more testing)
2.) error when video requires login (ex. age restricted)
3.) add ability download with different settings (atm, only has best quality available)

notes:
11/15/2025
I'm still having issues with permissions. I think the issue is the OS itself, since I've only recently
upgraded to Windows 11. I can run script fine through VS Code terminal. I can give permissions, but
this might not be practical and I think we can find a better solution. Will look into it some more.

10/24/2025
I was able to find the solution to downloading from websites that actively block yt-dlp. 
However, I ran into an issue in which Windows 11 is not giving us permission to download.

10/18/2025
I noticed that yt-dlp doesn't allow us to download videos from certain websites. After some research,
I believe the issue is due to some websites actively blocking yt-dlp by identifying these requests as coming
from an automated script (and not browser itself) and then denying access. More investigation is needed.

My goal next is to try and circumvent this issue by allowing my script to download from any website.
I will continue to research how this can be done. Hopefully I can find a solution in the coming days.

10/13/2025
Added simple video downloader script