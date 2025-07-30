# 🖼️ Images to PDF Converter

A simple Python script that merges multiple JPG images into a single multi-page PDF.

## 🚀 Features

- Reads all `.jpg` images from a specified folder
- Sorts images numerically by filename (e.g., `1.jpg`, `2.jpg`, `3.jpg`, ...)
- Converts images to RGB format for PDF compatibility
- Saves all images as pages in a single PDF file

## 🛠️ Tech Stack

- Python 3
- Pillow (PIL) library for image processing

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cema2019/python-apps.git
   cd python-apps/merge-images-to-pdf
   ```
2. Install Pillow if you haven't already:
    ```bash
    pip install pillow
    ```
3. Run the script (update the folder paths inside the script accordingly):
    ```bash
    python3 merge_to_pdf.py
    ```

## ⚠️ Important Note
- Filenames must be numeric (e.g., 1.jpg, 2.jpg, 3.jpg, ...) without any prefixes or suffixes for proper sorting and merging.
- The script sorts the images by converting filenames (without .jpg) to integers.
- If filenames are not numeric, the script will raise an error or behave unexpectedly.

## 🧑‍💻 Usage
- Place your JPG images inside the folder specified by image_folder in the script.
- Run the script.
- Your merged PDF will be saved to the path specified by output_pdf.
