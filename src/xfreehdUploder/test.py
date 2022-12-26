from app import handler
from dependency.database.index import getDatabaseWrapperInstance
import json
import requests
import random
import subprocess



def get_list_countries():
    with open('./location.txt',"r") as txt_file:
        countries=txt_file.read().split(",")
        return countries

db=getDatabaseWrapperInstance("created_video")
video_list=db.find_all(collection="videos")

for data in video_list:
    try:
        countries=get_list_countries()
        coutry=random.choice(countries)
        result=subprocess.run(["nordvpn","c",coutry])
        res=requests.get(data["url"])
        with open("./data/tmp.mp4","wb") as video_file:
            video_file.write(res.content)
        del data['_id']
        handler({'body':json.dumps(data),'create_account':True},{})

    except Exception as e:
        print(e)


# handler({'body':json.dumps(data),'create_account':True},{})
