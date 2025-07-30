from PIL import Image, ImageFilter
import os

# Set your image folder paths
INPUT_FOLDER = "input-images"
OUTPUT_FOLDER = "output-images"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(f"{INPUT_FOLDER}/{filename}")
        edit = img.filter(ImageFilter.SHARPEN).convert('L')  # Convert to grayscale
        clean_name = os.path.splitext(filename)[0]
        edit.save(f"{OUTPUT_FOLDER}/{clean_name}_edited.jpg")

print("✅ All images converted to grayscale and saved to 'output-images'")
