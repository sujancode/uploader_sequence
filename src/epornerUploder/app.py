from sign_up_upload import login,upload
from dependency.selenium.Selenium import getSeleniumBrowserAutomation
import time
import json

def handler(event,context):
    data=json.loads(event['body'])
    print(data)
    print("Inside Handler")
    video_url=data["url"]
    title=data["title"]
    tags=data["tags"]

    print(video_url,title,tags)
    username="xsggqlfsdthxudy"
    password="earning$$"
    browser=getSeleniumBrowserAutomation()    
    login(browser,username,password)
    upload(browser=browser,url="https://www.eporner.com/upload_do/",video_url=video_url,title=title,tags=tags)
    browser.close()
    time.sleep(100)
    return {
        "statusCode": 200,
        "headers": { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
        "message":"Video Uploder"
    }