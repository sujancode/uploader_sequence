from sign_up_upload import sign_up
from dependency.database.index import getDatabaseWrapperInstance
import requests
import random
import subprocess

while True:
    db=getDatabaseWrapperInstance("created_video")
    video_list=db.find_all(collection="videos")
    rand_index=random.randint(0,len(video_list))
    data=video_list[rand_index]
    print(data,rand_index)
    try:
        res=requests.get(data["url"])
        with open("/tmp/tmp.mp4","wb") as video_file:
            video_file.write(res.content)
        sign_up(video_url=data["url"],title=data['title'],tags=data['tags'])
        result=subprocess.run(["nordvpn","c","united_states"])
        print(result)
    except Exception as e:
        print(e)

