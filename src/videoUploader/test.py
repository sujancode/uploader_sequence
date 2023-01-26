from sign_up_upload import sign_up
from dependency.database.index import getDatabaseWrapperInstance
import requests
import random
import subprocess
import os
from dependency.storage_bucket.index import getS3StorageInstance
import urllib
import youtube_dl

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

def get_list_countries():
    with open('./location.txt',"r") as txt_file:
        countries=txt_file.read().split(",")
        return countries

db=getDatabaseWrapperInstance("created_video")

# for index in range(0,len(video_list)):
#     try:
#         data=video_list[index]
        
#         countries=get_list_countries()
#         coutry=random.choice(countries)
#         result=subprocess.run(["nordvpn","c",coutry])
#         print(result) 

#         res=requests.get(data["url"])
#         with open("./tmp/tmp.mp4","wb") as video_file:
#             video_file.write(res.content)
#         sign_up(video_url=data["url"],title=data['title'],tags=data['tags'],username=data.get('username',""))

#     except Exception as e:
#         print(e)

while True:
    try:
        video_list=db.find_all(collection="videos")
        rand_index=random.randint(0,len(video_list)-1)
        print(rand_index)
        data=video_list[rand_index]

        # result=subprocess.run(["nordvpn","d"])

        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': f"{BASE_DIR}/tmp/tmp.mp4",
                'nooverwrites': True,
                'no_warnings': False,
                'ignoreerrors': True,
            }

            filename=data["url"].split("/")[-1]
            filename=filename.replace("+","")
            print(data['url'])
            print(filename)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([data["url"]])   
            # res=requests.get(data["url"])
            # with open(f"{BASE_DIR}/tmp/tmp.mp4","wb") as video_file:
            #     video_file.write(res.content)
            
            bucket_name="new-data-source"
            url=f"https://{bucket_name}.s3.amazonaws.com/{filename}"
            print(url)
            storage_bucket=getS3StorageInstance()
            storage_bucket.upload_file(path=f'{BASE_DIR}/tmp/tmp.mp4',bucket_name=bucket_name,upload_location=filename)

            # countries=get_list_countries()
            # coutry=random.choice(countries)
            # result=subprocess.run(["nordvpn","c",coutry])

            print(result) 
            sign_up(video_url=url,title=data['title'],tags=data['tags'],username=data.get('username',""))
            
            os.unlink(f'{BASE_DIR}/tmp/tmp.mp4')
        except Exception as e:
            print(e)
    except Exception as e:
        result=subprocess.run(["nordvpn","d"])
        print(e)
        print("Most Probably database error")