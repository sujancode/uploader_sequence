from youjizz.dependency.selenium.Selenium import getSeleniumBrowserAutomation
from selenium.webdriver.common.by import By
from time import sleep
import os
import random
from string import ascii_letters
from youjizz.dependency.database.index import getDatabaseWrapperInstance



BASE_DIR=os.getcwd()

def getRandomString(length):
    return ''.join(random.choice(ascii_letters) for i in range(length))

def getRandomUserName(length):
    return getRandomString(length)

def getRandomPassword():
    return getRandomString(10)

def upload(browser,title,tags):
    try:
        print("uploding")
        browser.get("https://www.youjizz.com/profile/upload")
        sleep(5)
        browser.find_element(By.ID,"inputFileUpload").send_keys(f"{BASE_DIR}/tmp/tmp.mp4")
        browser.execute_script('''document.querySelector('[data-ng-i18next="header.filters.straight"]').click()''')
        browser.find_element(By.CSS_SELECTOR,'''[data-ng-model="file.title"]''').send_keys(title)
        browser.find_element(By.CSS_SELECTOR,'''[data-ng-model="file.keywords"]''').send_keys(','.join(tags))
        browser.execute_script('''document.querySelector(".upload_video_button").click()''')
        print("Uploade")
        sleep(300)
    except Exception as e:
        print(e)

def login(browser):
    print("Logging In")
    username="bangobros69"
    password="earning$$"

    browser.get("https://www.youjizz.com/login")
    sleep(5)
    browser.find_element(By.ID,"username").send_keys(username)
    browser.find_element(By.ID,"password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR,".yj-btn").click()
    sleep(5)


def sign_up(browser,username,password):


    browser.get("https://www.youjizz.com/signup")
    browser.find_element(By.ID,"username").send_keys(username)
    browser.find_element(By.ID,"password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR,".yj-btn").click()
    sleep(5)

def handler(event,context):
    username=getRandomUserName(10)
    password=getRandomPassword()

    title=event["title"]
    tags=event["tags"]

    browser=getSeleniumBrowserAutomation()
    sign_up(browser,username,password)
    # login(browser)
    upload(browser,title,tags)
    browser.close()
    sleep(10)
    db=getDatabaseWrapperInstance(table_name="youjizz")
    db.insert(collection="accounts",data={
        "username":username,
        "password":password
    })
    