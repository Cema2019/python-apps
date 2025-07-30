# 📥 Sequential Image Downloader

A Python script to download images from any URL pattern that ends with a **number** followed by `.jpg`. It downloads images starting from `1.jpg`, `2.jpg`, and continues until no more images are found (detecting a 404 error).

## 🚀 Features

- Downloads sequentially numbered `.jpg` images from a base URL
- Automatically stops when no more images exist (HTTP 404)
- Creates target folder if it doesn’t exist
- Handles HTTP errors gracefully and continues for non-404 errors

## 🛠️ Tech Stack

- Python 3
- `requests` library for HTTP downloads

## 📦 Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/Cema2019/python-apps.git
 cd python-apps/image-downloader-from-url
  ```
2. Install requests if you don’t have it:
  ```bash
  pip install requests
  ```

3. Customize and run the script:
  ```bash
  python3 download_thumbnails.py
  ```

## ⚙️ Configuration
Inside the script, update the base_url variable to the URL pattern for your images. For example:

  ```python
  base_url = "https://example.com/path/to/images/"
  ```
The script will append numbers starting at 1 and the .jpg extension automatically:

  ```text
  https://example.com/path/to/images/1.jpg
  https://example.com/path/to/images/2.jpg
  https://example.com/path/to/images/3.jpg
  ```

## ⚠️ Important Notes
The script assumes images are named sequentially with numbers only, no prefixes or suffixes before the .jpg.<br>
You can change the file extension in the code if you need to download .png or other formats.<br>
The script will stop downloading when it receives a 404 error (file not found).<br>

## 🧑‍💻 Usage
- Place your customized base_url in the script.
- Run the script.
- Images will be saved in the downloads/thumbnails folder by default.
- The script will print download progress and a final saved folder message.

