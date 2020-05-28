from PIL import Image
import PIL
import os

path = '/home/sridhar/venv/images'
files = os.listdir(path)
path2 = '/home/sridhar/venv/icons'

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([file, '.jpeg'])))

files = os.listdir(path)

for img in files:
    k = os.path.join(path,img)
    with Image.open(k,'r') as im:
        im = im.resize((128,128))
        im = im.rotate(270)
        im = im.convert("RGB")
        im.save(os.path.join(path2,img))
