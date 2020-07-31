import os
import shutil
import requests

def dl_file(url, dir, file_name=None):
    if file_name == None:
        file_name = os.path.basename(url)
    # dl_filename = os.path.basename(url)
    new_dl_path = os.path.join(dir, file_name)

    with requests.get(url, stream=True) as req:
        with open(new_dl_path, 'wb') as f_obj:
            shutil.copyfileobj(req.raw, f_obj)

    return new_dl_path