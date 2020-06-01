#!/usr/bin/env python3

from PIL import Image
import PIL
import os

path = '/home/student-00-7504f86c09ab/supplier-data/images'
files = os.listdir(path)
path2 = '/home/student-00-7504f86c09ab/supplier-data/images'

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([file[:3], '.jpeg'])))

files = os.listdir(path)

for img in files:
    k = os.path.join(path,img)
    with Image.open(k,'r') as im:
        im = im.resize((600,400))
        im = im.convert("RGB")
        im.save(k)
