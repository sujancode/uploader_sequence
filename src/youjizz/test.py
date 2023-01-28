from app import handler
from dependency.database.index import getDatabaseWrapperInstance
import requests
import random
import subprocess
import os
import youtube_dl

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
db=getDatabaseWrapperInstance("created_video")

while True:
    try:
        video_list=db.find_all(collection="videos")
        rand_index=random.randint(0,len(video_list)-1)
        print(rand_index)
        data=video_list[rand_index]


        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': f"{BASE_DIR}/tmp/tmp.mp4",
                'nooverwrites': True,
                'no_warnings': False,
                'ignoreerrors': True,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([data["url"]])   
            

            event={
                "title":data["title"],
                "tags":data["tags"]
            }
            handler(event,{})
            
            os.unlink(f'{BASE_DIR}/tmp/tmp.mp4')
        except Exception as e:
            print(e)
    except Exception as e:
        result=subprocess.run(["nordvpn","d"])
        print(e)
        print("Most Probably database error")
