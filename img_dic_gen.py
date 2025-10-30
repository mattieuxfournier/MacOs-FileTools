from itertools import permutations

file_etx = {
    'img': ['.png', '.apng', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.svg', '.webp', '.gif', '.tif', '.tiff', '.bmp', '.eps', '.heic', '.avif', '.ico', '.cur'],
    'doc': ['.asc', '.doc', '.docx', '.rtf', '.msg', '.pdf', '.txt', '.wpd', '.wps', '.csv', '.xlsx', '.json', '.html', '.htm', '.xhtml', '.asp', '.css', '.aspx', '.rss', '.pptx'],
    'aud': ['.mp3', '.wma', '.snd', '.wav', '.ra', '.au', '.aac'],
    'vid': ['.mp4', '.3gp', '.avi', '.mpg', '.mov', '.wmv'],
}

img_dict = list((file_etx).values())[0]
doc_dict = list((file_etx).values())[1]
aud_dict = list((file_etx).values())[2]
vid_dict = list((file_etx).values())[3]
for p in permutations(img_dict,2):
    print(f"def {p[0].strip('.')}_to_{p[1].strip('.')}(input_path: Path, output_folder: Path):\n    output_path = output_folder / f\"{{input_path.stem}}{p[1]}\"\n\n    cmd = [\n        \"ffmpeg\",\n        \"-y\",\n        \"-i\", str(input_path),\n        \"-plays\", \"0\",\n        str(output_path)\n    ]\n\n    try:\n        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n        print(f\"Converted '{{input_path.name}}' -> '{{output_path.name}}'\")\n    except subprocess.CalledProcessError as e:\n        print(f\"Conversion failed: {{e.stderr.decode('utf-8')}}\")")