from sign_up_upload import login,upload,sign_up
from dependency.selenium.Selenium import getSeleniumBrowserAutomation
import time
import json
from dependency.database.index import getDatabaseWrapperInstance


def handler(event,context):
    global username,password
    data=json.loads(event['body'])
    print(data)
    print("Inside Handler")
    video_url=data["url"]
    title=data["title"]
    tags=data["tags"]
    browser=getSeleniumBrowserAutomation()    

    create_account=event['create_account']

    if create_account:
        [username,password]=sign_up(browser)
        db=getDatabaseWrapperInstance(table_name="xfreehd")
        db.insert(collection="accounts",data={
            "username":username,
            "password":password,
            "video":video_url,
            "tags":tags
        })
    print(video_url,title,tags)

    username="xefil86176"
    password="earning$$"
    login(browser,username,password)
    upload(browser=browser,url="https://www.xfreehd.com/upload/video",video_url=video_url,title=title,tags=tags)
    browser.close()


    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
        "message":"Video Uploder"
    }