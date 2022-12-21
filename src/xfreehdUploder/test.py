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
        data=random.choice(video_list)
        res=requests.get(data["url"])
        with open("./data/tmp.mp4","wb") as video_file:
            video_file.write(res.content)
        del data['_id']
        handler({'body':json.dumps(data),'create_account':True},{})


        index+=1
    except Exception as e:
        print(e)


# handler({'body':json.dumps(data),'create_account':True},{})
