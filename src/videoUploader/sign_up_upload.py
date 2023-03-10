from videoUploader.dependency.selenium.Selenium import getSeleniumBrowserAutomation
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from string import ascii_letters
import random
from videoUploader.dependency.database.index import getDatabaseWrapperInstance
from videoUploader.dependency.captchaResolver.index import getTextToSpeechCaptchaResolver
import os

BASE_DIR=os.getcwd()

def getRandomString(length):
    return ''.join(random.choice(ascii_letters+"1234567890") for i in range(length))

def getRandomEmail():
    random_string=getRandomString(10)
    return f"{random_string}@gmail.com"

def getRandomPassword():
    return getRandomString(10)    

    
def get_random_user_cred():
    email=getRandomEmail()
    username=email.split("@")[0]
    return [username,email,getRandomPassword()]

def upload(browser,url,video_url,title,tags,username,password):
    try:
        browser.get(f"{url}/users/upload")
        captcha_solver=getTextToSpeechCaptchaResolver(browser)
        sleep(2)
        googleClass=browser.find_elements(By.CSS_SELECTOR,"[title=reCAPTCHA]")
        if len(googleClass)>0:
            captcha_solver.resolve()
            sleep(2)
        
        browser.switch_to.parent_frame()   
        
        browser.find_element(By.ID,"fileInput").send_keys(f"{BASE_DIR}/tmp/tmp.mp4")

        # browser.execute_script('upload_show_url()')
        # sleep(4)
        # browser.find_element(By.CSS_SELECTOR,".url_upload input").send_keys(video_url)
        # sleep(2)
        # browser.execute_script('resumable_check_url()')
        
        sleep(5)

        browser.find_element(By.CSS_SELECTOR,"#name_inp").send_keys(title)
        browser.execute_script(''' 
            document.querySelector(".radio-boxes-orientation");
            document.querySelector(".radio-boxes-orientation label").click();
            ''')

        browser_tags=browser.execute_script('''
                return document.querySelector("#category_list").innerText;
            ''')
        if not tags:
            tags=browser_tags.split("\n")

        for t in tags:
            element=browser.find_element(By.CSS_SELECTOR,"#tag_inp input")
            element.send_keys(t)
            element.send_keys(Keys.ENTER)
        browser.execute_script('''items=document.querySelectorAll("#category_list label");for(var item of items){item.click()};''')

        sleep(10)
        browser.find_element(By.ID,"upload_form_button").click()

        upload_complete=browser.execute_script("return upload_is_completed")
        print(upload_complete)
        sleep(10)
        # while not upload_complete:
        #     try:
        #         print(trys)
        #         if trys>10:
        #             break
        #         sleep(5)
        #         upload_complete=browser.execute_script("return upload_is_completed")
        #     except Exception as e:
        #         trys+=1
        #         print("Error With upload_is_completed not being found")                
        
        sleep(300)
        
        db=getDatabaseWrapperInstance(table_name="spankbang_account")
        db.insert(collection="accounts",data={
            "username":username,
            "password":password,
            "video":video_url,
            "tags":tags
        })
        print("UPLOADD Complete")
    except Exception as e:
        print(e)



def sign_up(video_url,title,tags,username):
    
    # titles=["Fanso.us - Biggest OF Leaks Database","Fanso.us - Find every onlyfans leaks","Fanso.us - Leaked Onlyfans Accounts","Fanso.us - All leaks you need","Fanso.us - Leaked OF's","Fanso.us - Onlyfans Unlocker"]
    # title=random.choice(titles)

    print(video_url,title)
    url="https://spankbang.com"
    browser=getSeleniumBrowserAutomation()
    browser.get(url)
    sleep(2)
    browser.execute_script("accept_warning_modal();")
    browser.find_element(By.CLASS_NAME,"bt_signup").click()
    [username,email,password]=get_random_user_cred()
    print(username,email,password)
    sleep(2)

    browser.find_element(By.ID,"reg_username").send_keys(username)
    browser.find_element(By.ID,"reg_password").send_keys(password)
    browser.find_element(By.ID,"reg_email").send_keys(email)

    browser.find_element(By.CLASS_NAME,"btn").click()
    sleep(2)
    upload(browser,url,video_url,title,tags,username,password)

    browser.close()
