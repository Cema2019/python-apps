import yt_dlp
from sys import argv

# Check if a link was passed
if len(argv) < 2:
    print("Missing data: python youtube_downloader.py <YouTube URL>")
    exit()

url = argv[1]

# Download options
ydl_opts = {
    'outtmpl': './downloads/%(title)s.%(ext)s',  # Save to ./downloads folder using yt_dlp's metadata template system
}

print(f"⬇️ Downloading from: {url}")

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("✅ Download completed!")
except Exception as e:
    print("❌ Download failed. Error:", e)
