import requests
import os
import shutil
from download_fc import dl_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

dl_path = os.path.join(DOWNLOADS_DIR, '1.jpg')

url = 'https://uploads7.wikiart.org/images/el-greco/st-jerome-penitent.jpg!Large.jpg'

r = requests.get(url, stream=True)
r.raise_for_status()
with open(dl_path, 'wb') as f:
    f.write(r.content)

#dl_filename = os.path.basename(url)
#new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)

#with requests.get(url, stream=True) as req:
#    with open(new_dl_path, 'wb') as f_obj:
#        shutil.copyfileobj(req.raw, f_obj)

dl_file(url, DOWNLOADS_DIR, 'pepe_foto.jpg')