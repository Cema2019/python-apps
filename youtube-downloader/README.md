# YouTube Video & Playlist Downloader (yt-dlp)

A simple Python script to download YouTube videos and playlists using the [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) library.

## 📦 Features

- Downloads single videos or full playlists from YouTube
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

### Example  

1. Download a single video:

```bash
python yt-downloader.py https://www.youtube.com/watch?v=abc123
```

2. Download a playlist:

```bash
python yt-downloader.py https://www.youtube.com/playlist?list=PLxyz456
```

Output  

The video(s) will be saved in the downloads/ directory with a filename like: 
```text
downloads/downloaded-youtube-video.mp4
```

## 📌 Notes  
- The script uses sys.argv to accept the video or playlist URL as a command-line argument.
- Filenames are generated using yt-dlp's template system (%(title)s.%(ext)s).
- yt-dlp automatically detects and downloads full playlists when a playlist URL is given..
##
© 2025 – Built with ❤️ using Python and yt-dlp
