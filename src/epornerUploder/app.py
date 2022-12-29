from sign_up_upload import login,upload,sign_up
from dependency.selenium.Selenium import getSeleniumBrowserAutomation
import time
import json
from dependency.database.index import getDatabaseWrapperInstance

username=""
password=""

def handler(event,context):
    global username,password
    data=json.loads(event['body'])
    print(data)
    print("Inside Handler")
    video_url=data["url"]
    title=data["title"]
    tags=data["tags"]
    create_account=event['create_account']
    print(create_account)
    print(video_url,title,tags)
    browser=getSeleniumBrowserAutomation()
    if create_account:
        print("Create Account")
        [username,password]=sign_up(browser)
        db=getDatabaseWrapperInstance(table_name="eporner")
        db.insert(collection="eporner_accounts",data={
            "username":username,
            "password":password,
            "video":video_url,
            "tags":tags
        })
    print("Uploading")
    login(browser,username,password)
    upload(browser=browser,url="https://www.eporner.com/upload_do/",video_url=video_url,title=title,tags=tags)
    browser.close()
    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
        "message":"Video Uploder"
    }