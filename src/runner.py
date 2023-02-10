from epornerUploder.test import main as eporner_main
from videoUploader.test import main as spank_main
from youjizz.test import main as youjizz_main

from database.index import getDatabaseWrapperInstance
import random
import os
import youtube_dl
import subprocess

import threading
import time

BASE_DIR=os.getcwd()

def get_list_countries():
    with open('./location.txt',"r") as txt_file:
        countries=txt_file.read().split(",")
        return countries

def main(index):
    result=subprocess.run(["nordvpn","d"])

    db=getDatabaseWrapperInstance("created_video")
    video_list=db.find_all(collection="videos")
    rand_index=random.randint(200,len(video_list))
    data=video_list[rand_index]
    ydl_opts = {
        'format': 'best',
        'outtmpl': f"{BASE_DIR}/tmp/tmp.mp4",
        'nooverwrites': True,
        'no_warnings': False,
        'ignoreerrors': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([data["url"]])   
    countries=get_list_countries()

    coutry=random.choice(countries)
    # result=subprocess.run(["nordvpn","c",coutry])

    ep_task=threading.Thread(target=eporner_main,args=(data,index,))    
    sp_main=threading.Thread(target=spank_main,args=(data,))
    you_main=threading.Thread(target=youjizz_main,args=(index,data,))

    ep_task.start()
    sp_main.start()
    you_main.start()

    
    ep_task.join()
    sp_main.join()
    you_main.join()

    os.unlink(f'{BASE_DIR}/tmp/tmp.mp4')

while True:
    index=0
    main(index)
    index=index+1