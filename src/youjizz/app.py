from dependency.selenium.Selenium import getSeleniumBrowserAutomation
from selenium.webdriver.common.by import By
from time import sleep
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

def upload(browser,title,tags):
    try:
        browser.get("https://www.youjizz.com/profile/upload")
        sleep(5)
        browser.find_element(By.ID,"inputFileUpload").send_keys(f"{BASE_DIR}/tmp/tmp.mp4")
        browser.execute_script('''document.querySelector('[data-ng-i18next="header.filters.straight"]').click()''')
        browser.find_element(By.CSS_SELECTOR,'''[data-ng-model="file.title"]''').send_keys(title)
        browser.find_element(By.CSS_SELECTOR,'''[data-ng-model="file.keywords"]''').send_keys(','.join(tags))
        browser.execute_script('''document.querySelector(".upload_video_button").click()''')
    except:
        pass

def login(browser):
    username="bangobros69"
    password="earning$$"

    browser.get("https://www.youjizz.com/login")
    sleep(5)
    browser.find_element(By.ID,"username").send_keys(username)
    browser.find_element(By.ID,"password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR,".yj-btn").click()
    sleep(5)



def handler(event,context):
    title=event["title"]
    tags=event["tags"]
    browser=getSeleniumBrowserAutomation()
    login(browser)
    upload(browser,title,tags)
    sleep(300)