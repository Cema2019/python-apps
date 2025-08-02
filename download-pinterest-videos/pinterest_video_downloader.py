import asyncio
from pinterest_downloader import *

async def main():
    video_list = input("Enter list of Pinterest video links: ")
    links = [link.strip() for link in video_list.split(",")]

    print("Starting download... Please wait")

    for link in links:
        result = await download_pinterest_media(link, output_dir=r"C:\Users\yourname\Downloads\PinterestVideos")  
        if result.get('success'):
            print(f"Downloaded: {result.get('file_path', 'Unknown file path')}")
        else:
            print(f"Download failed for {link}")

    print("Download is now complete")

if __name__ == "__main__":
    asyncio.run(main())
