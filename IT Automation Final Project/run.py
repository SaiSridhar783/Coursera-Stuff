#! /usr/bin/env python3

import os
import requests
import json

path = '/home/student-00-7504f86c09ab/supplier-data/descriptions/'
files = os.listdir(path)
keys = ["name", "weight", "description"]
url = "http://35.232.96.187/fruits"

for file in files:
    dic = {}
    with open(os.path.join(path,file)) as work:
        for key,data in zip(keys,work):
            if key =="weight" :
                dic[key] = data.strip()[:-4]
            else:
                dic[key] = data.strip()
        dic["image_name"] = ''.join([file[:3],'.jpeg'])
    dic = json.dumps(dic)
    x = requests.post(url, data = dic)
    print(dic)
