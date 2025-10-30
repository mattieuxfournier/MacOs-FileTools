# generate_files_to_pwd.py
from pathlib import Path
import os

# Save generated scripts to the current working directory
output_dir = Path(os.getcwd())

file_etx = {
    'img': ['.png', '.apng', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.svg', '.webp', '.gif', '.tif', '.tiff', '.bmp', '.eps', '.heic', '.avif', '.ico', '.cur'],
    'doc': ['.asc', '.doc', '.docx', '.rtf', '.msg', '.pdf', '.txt', '.wpd', '.wps', '.csv', '.xlsx', '.json', '.html', '.htm', '.xhtml', '.asp', '.css', '.aspx', '.rss', '.pptx'],
    'aud': ['.mp3', '.wma', '.snd', '.wav', '.ra', '.au', '.aac'],
    'vid': ['.mp4', '.3gp', '.avi', '.mpg', '.mov', '.wmv'],
}

# Template for each generated script
template = """\"\"\"
Auto-generated script for handling {ext} files in category '{category}'
\"\"\"

from pathlib import Path

def process_file(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        print("File not found:", file_path)
        return
    print("Processing {ext} file:", file_path)

if __name__ == "__main__":
    sample_file = input("Enter path to a {ext} file: ")
    process_file(sample_file)
"""

# Generate one .py file per extension
for category, extensions in file_etx.items():
    for ext in extensions:
        # Remove the leading dot for filename
        safe_ext = ext.lstrip('.')
        file_name = f"{category}_{safe_ext}.py"
        file_path = output_dir / file_name

        with open(file_path, "w") as f:
            f.write(template.format(category=category, ext=ext))

        print(f"Generated: {file_path}")
