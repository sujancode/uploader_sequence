from sign_up_upload import sign_up
from dependency.database.index import getDatabaseWrapperInstance
import requests
import random
import subprocess
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

def get_list_countries():
    with open('./location.txt',"r") as txt_file:
        countries=txt_file.read().split(",")
        return countries

db=getDatabaseWrapperInstance("created_video")
video_list=db.find_all(collection="videos")

# for index in range(0,len(video_list)):
#     try:
#         data=video_list[index]
#         countries=get_list_countries()
#         coutry=random.choice(countries)
#         result=subprocess.run(["nordvpn","c",coutry])
#         print(result) 
#         # res=requests.get(data["url"])
#         # with open("/tmp/tmp.mp4","wb") as video_file:
#         #     video_file.write(res.content)
#         sign_up(video_url=data["url"],title=data['title'],tags=data['tags'],username=data.get('username',""))

#     except Exception as e:
#         print(e)

while True:
    rand_index=random.randint(0,len(video_list)-1)
    
    data=video_list[rand_index]
    try:

        countries=get_list_countries()
        vpn_index=random.randint(0,len(countries)-1)
        coutry=countries[vpn_index]
        
        result=subprocess.run(["nordvpn","c",coutry])
        print(result) 
        res=requests.get(data["url"])
        with open(f"{BASE_DIR}/tmp/tmp.mp4","wb") as video_file:
            video_file.write(res.content)
        sign_up(video_url=data["url"],title=data['title'],tags=data['tags'],username=data.get('username',""))
        
    except Exception as e:
        print(e)

