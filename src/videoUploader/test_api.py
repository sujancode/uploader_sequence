from dependency.database.index import getDatabaseWrapperInstance
import requests

db=getDatabaseWrapperInstance("created_video")
video_list=db.find_all(collection="videos")

for index in range(100,len(video_list)):
    data = video_list[index]
    print(data)
    requests.post(url='https://7sve4dxax3.execute-api.us-east-1.amazonaws.com/prod/send',json={
            "url":data["url"],
            "title":"",
            "tags":data["tags"]
        })