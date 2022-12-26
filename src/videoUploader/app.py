from sign_up_upload import sign_up
import json
import requests

def handler(event,context):
    data=json.loads(event['body'])
    print(data)
    video_url=data["url"]
    title=data["title"]
    tags=data["tags"]
    username=""
    res=requests.get(data["url"])
    with open("/tmp/tmp.mp4","wb") as video_file:
        video_file.write(res.content)
    sign_up(video_url,title,tags,username)
    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
        "message":"Video Uploder"
    }