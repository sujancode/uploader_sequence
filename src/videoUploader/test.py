from sign_up_upload import sign_up
from dependency.database.index import getDatabaseWrapperInstance
import requests
import random
while True:
    db=getDatabaseWrapperInstance("created_video")
    video_list=db.find_all(collection="videos")
    data=random.choice(video_list)

    try:
        res=requests.get(data["url"])
        with open("/tmp/tmp.mp4","wb") as video_file:
            video_file.write(res.content)
        sign_up(video_url=data["url"],title=data['title'],tags=data['tags'])
    except Exception as e:
        print(e)

# sign_up(video_url="",title="",tags=["Amature","Gangbang"])
