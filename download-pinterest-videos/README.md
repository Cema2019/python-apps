# Pinterest Video Downloader

This Python script allows you to download videos from Pinterest using the [`pinterest-downloader`](https://pypi.org/project/pinterest-downloader/) library.  
It supports downloading a single video or multiple videos by entering a comma-separated list of Pinterest video URLs.

## Features

- Download a single video by providing its URL.
- Download multiple videos at once by entering URLs separated by commas.
- Saves videos to a specified output directory.

## Requirements

- Python 3.7+
- [`pinterest-downloader`](https://pypi.org/project/pinterest-downloader/) Python package

Install dependencies with:

```bash
pip install pinterest-downloader
```

## Usage

1. Clone this repository or download the script.
2. Run the script:

```bash
python pinterest_video_downloader.py
```

3. When prompted, enter one video URL or multiple URLs separated by commas.

Example input:

```
https://pin.it/abcdefg, https://pin.it/hijklmn, https://pin.it/opqrstu
```

4. The videos will be downloaded to the default output directory (current working directory) or a specified folder.

## Customizing Output Directory

Edit the `output_dir` parameter in the script to change where videos are saved.

Example:

```python
output_dir = r"C:\Users\yourname\Downloads\PinterestVideos"
```

## Notes

- The script handles invalid or broken links gracefully and continues downloading remaining videos.
- Progress for each downloaded video and success/failure messages are printed to the console.

---

Feel free to contribute or open issues if you encounter problems!
