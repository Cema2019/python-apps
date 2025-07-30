import os
import requests

# Define folder path
folder_path = os.path.join("downloads", "thumbnails")
os.makedirs(folder_path, exist_ok=True)  # Create directories if they don't exist

# Base URL - Change to your image URL prefix
base_url = "https://example.com/path/to/images/"

# Loop through the end
i = 1
while True:
    url = f"{base_url}{i}.jpg"
    filename = os.path.join(folder_path, f"{i}.jpg")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Downloaded: {filename}")
        i += 1
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Reached end of files at {url} (404 Not Found). Stopping.")
            break
        else:
            print(f"HTTP error at {url}: {e}. Continuing.")
    except Exception as e:
        print(f"Error downloading {url}: {e}. Continuing.")

print(f"\n✅ Files saved to: {folder_path}")
