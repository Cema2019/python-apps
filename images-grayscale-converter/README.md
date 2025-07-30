# Batch Grayscale Image Converter

This is a simple Python script that converts all images in a folder to grayscale and applies a sharpening filter.

## Features

- Converts `.jpg`, `.jpeg`, and `.png` images to grayscale
- Applies a sharpening filter using Pillow
- Saves the edited images to a separate output folder
- Automatically creates the output folder if it doesn't exist

## Requirements

- Python 3.x
- Pillow (`pip install pillow`)

## Usage

1. Place all your images in the input folder.
2. Run the script:

```bash
python batch_grayscale_converter.py
```
3. Grayscale images will be saved to the output folder with '_edited' suffix.

### Example  
An image named photo1.jpg will be saved as photo1_edited.jpg in the output folder.
