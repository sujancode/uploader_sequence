from app import handler
from dependency.database.index import getDatabaseWrapperInstance
import json
import requests
import random
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
        handler(
            {'body':json.dumps(data)},
            {}
            )
    except Exception as e:
        print(e)
