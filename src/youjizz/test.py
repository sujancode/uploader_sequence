from .app import handler
import os

BASE_DIR=os.getcwd()

def main(index,data):
    try:
        event={}
        if index%10==0:
            event={
                "title":data["title"],
                "tags":data["tags"],
                'create_account':True
            }
        else:
            event={
                "title":data["title"],
                "tags":data["tags"],
                'create_account':False
            }
        handler(event,{})            
    except Exception as e:
        print(e)

