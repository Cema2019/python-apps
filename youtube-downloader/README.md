# YouTube Video Downloader (yt-dlp)

A simple Python script to download YouTube videos using the [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) library.

## 📦 Features

- Downloads videos from YouTube
- Automatically saves them into a local `downloads/` folder
- Uses video title and extension as filename
- Gracefully handles errors

## 🔧 Requirements

- Python 3.7+
- `yt-dlp` Python package
- [ffmpeg](https://ffmpeg.org/download.html) (optional but recommended for best format compatibility)

## 🚀 Installation

1. Install `yt-dlp`:

```bash
pip install yt-dlp
```

2. (Optional) Install ffmpeg for best quality downloads:
   
- Download ffmpeg
- Add it to your system PATH

## ▶️ Usage
```bash
python yt-downloader.py <YouTube URL>
```

Example
```bash
python yt-downloader.py https://www.youtube.com/shorts/abc123#@$
```
Output  

The video will be saved in the downloads/ directory with a filename like: 
```text
downloads/downloaded-youtube-video.mp4
```

## 📌 Notes  
The script uses sys.argv to accept the video URL as a command-line argument.

Filenames are generated using yt-dlp's template system.
##
© 2025 – Built with ❤️ using Python and yt-dlp
