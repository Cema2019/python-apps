from PIL import Image
import os

# Define the path to your thumbnails folder (update this path to your images folder)
image_folder = r'/path/to/your/thumbnails'

# Define the output PDF file path (update as needed)
output_pdf = r'/path/to/save/merged_thumbnails.pdf'

# Get list of .jpg files sorted numerically (e.g., 1.jpg to 45.jpg)
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.endswith('.jpg')],
    key=lambda name: int(name.replace('.jpg', ''))
)

# Open and convert all images to RGB
images = [Image.open(os.path.join(image_folder, f)).convert('RGB') for f in image_files]

# Save to PDF
if images:
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

print(f"PDF created: {output_pdf}")
