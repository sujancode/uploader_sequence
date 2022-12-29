from app import handler
from dependency.database.index import getDatabaseWrapperInstance
import json
import requests
import random

index=0
while True:
    try:
        
        db=getDatabaseWrapperInstance("created_video")
        video_list=db.find_all(collection="videos")
        rand_index=random.randint(0,len(video_list))
        data=video_list[rand_index]
        print(data,rand_index)
        res=requests.get(data["url"])
        with open("./data/tmp.mp4","wb") as video_file:
            video_file.write(res.content)
        del data['_id']
        if index%10==0:
            handler(
                {'body':json.dumps(data),'create_account':True},
                {}
                )
            index=0
        else:
            handler(
                {'body':json.dumps(data),'create_account':False},
                {}
                )
        index+=1
    except Exception as e:
        print(e)
