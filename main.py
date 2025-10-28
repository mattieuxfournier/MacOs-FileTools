#main logic script
import os
import glob
import shutil
import io
import pathlib
import subprocess
import __future__
from pathlib import *

file_etx = {
    'img': ['.png', '.apng', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.svg', '.webp', '.gif', '.tif', '.tiff', '.bmp', '.eps', '.heic', '.avif', '.ico', '.cur'],
    'doc': ['.asc', '.doc', '.docx', '.rtf', '.msg', '.pdf', '.txt', '.wpd', '.wps', '.csv', '.xlsx', '.json', '.html', '.htm', '.xhtml', '.asp', '.css', '.aspx', '.rss', '.pptx'],
    'aud': ['.mp3', '.wma', '.snd', '.wav', '.ra', '.au', '.aac'],
    'vid': ['.mp4', '.3gp', '.avi', '.mpg', '.mov', '.wmv'],
}

def choose_files():
    #initial file choice:
    file = 'set filePath to POSIX path of (choose file with prompt "Select a file:")'
    result = subprocess.run(["osascript", "-e", file], capture_output=True, text=True)
    filePath = result.stdout.strip()
    file_path_obj = Path(filePath)

    filename = file_path_obj.stem

    ext = file_path_obj.suffix.lower()

    return filename, ext, str(file_path_obj)
#global variable
selected_file = choose_files()

name, etx, path = selected_file

#file detection
def detect(name, etx, path):
    count = 0
    for extensions in file_etx.values():
        if etx in extensions:
            count += 1
    return count == 1
print(detect(name, etx, path))
