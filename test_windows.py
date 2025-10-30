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
for p in permutations(vid_dict,2):
    print(f'def {p[0].strip('.')}_to_{p[1].strip('.')}(input_path: Path, output_folder: Path):\n    ...')