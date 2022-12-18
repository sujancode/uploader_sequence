from dependency.selenium.Selenium import getSeleniumBrowserAutomation
from time import sleep
from selenium.webdriver.common.by import By
from string import ascii_letters
import random
from dependency.faker.Faker import getFakerInstance
from dependency.database.index import getDatabaseWrapperInstance
from dependency.captchaResolver.index import getTextToSpeechCaptchaResolver
import time
from dependency.captchaResolver.index import getTextToSpeechCaptchaResolver
import os
BASE_DIR=os.path.dirname(os.path.realpath(__file__))

def getRandomString(length):
    return ''.join(random.choice(ascii_letters+"1234567890") for i in range(length))

def getRandomEmail():
    faker=getFakerInstance()
    name=faker.name()
    name=name.replace(" ","")
    random_string=getRandomString(4)
    return f"{name}{random_string}@gmail.com"

def getRandomUserName(length):
    return getRandomString(length)

def getRandomPassword():
    return getRandomString(10)    

    
def get_random_user_cred():
    username=getRandomUserName(10)
    return [username,getRandomPassword()]

def upload(browser,url,video_url,title,tags):
    try:
        print(title,tags)
        browser.get(url)
        browser.find_element(By.ID, "videoTitleText").click()
        browser.find_element(By.ID, "videoTitleText").send_keys(title)

        browser.execute_script(''' items=document.querySelectorAll(".uptabcatinp input");for(var i=0;i<items.length;i++){if(i>4)break;items[i].click()}''')
        
        browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(f"{BASE_DIR}/data/tmp.mp4")
        time.sleep(2)
        browser.execute_script(''' document.querySelector("#typehome").click()''')
        time.sleep(1)
        browser.execute_script('''document.querySelector("#upformsubmitbtn").click() ''')
        time.sleep(60)
    except Exception as e:
        print(e)

def get_temp_email(browser):
    browser.get("https://mail.tm/en/")
    time.sleep(2)
    # captcha_solver=getTextToSpeechCaptchaResolver(browserWrapper=browser)
    # googleClass=browser.find_elements(By.CSS_SELECTOR,"[title=reCAPTCHA]")

    # if len(googleClass)>0:
    #     captcha_solver.resolve()
    #     sleep(2)
    #     browser.switch_to.parent_frame()   
    email=browser.execute_script(''' return document.querySelector("#DontUseWEBuseAPI").value ''')
    return email

def email_activation(browser):
    try:
        browser.get("https://mail.tm/en/")
        time.sleep(4)
        browser.execute_script(''' document.querySelector(".divide-y a").click() ''')
        time.sleep(4)
        iframe=browser.find_element(By.CSS_SELECTOR,"main iframe")
        browser.switch_to.frame(iframe)
        time.sleep(1)
        browser.execute_script('''document.querySelector('[href^="https://www.xfreehd.com/confirm?"]').click()''')
        time.sleep(2)

        browser.switch_to.default_content()
    except Exception as e:
        print(e)

def login(browser,username,password):
    browser.get("https://www.eporner.com/login")
    browser.set_window_size(955, 1095)

    browser.find_element(By.CSS_SELECTOR, '[name="login"]').click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(username)
    browser.find_element(By.CSS_SELECTOR, '[name="haslo"]').click()
    browser.find_element(By.CSS_SELECTOR, '[name="haslo"]').send_keys(password)
    browser.find_element(By.ID, "rememberme").click()
    browser.find_element(By.CSS_SELECTOR, '[name="Submit"]').click()

def sign_up(video_url,title,tags):
    browser=getSeleniumBrowserAutomation()
    email=get_temp_email(browser)
    title=f"** NEW ** {title}"
    print(video_url,title)

    [username,password]=get_random_user_cred()
    print(username,email,password)
    sleep(2)
    
    browser.get("https://www.xfreehd.com/")

    browser.find_element(By.CSS_SELECTOR, ".modal-content > .modal-footer > .btn").click()
    browser.find_element(By.LINK_TEXT, "Sign Up").click()
    browser.find_element(By.ID, "signup_username").click()
    browser.find_element(By.ID, "signup_username").send_keys(username)
    browser.find_element(By.ID, "signup_password").send_keys(password)
    browser.find_element(By.ID, "signup_password_confirm").send_keys(password)
    browser.find_element(By.ID, "signup_email").send_keys(email)
    browser.find_element(By.ID, "signup_gender_male").click()
    googleClass=browser.find_elements(By.CSS_SELECTOR,"[title=reCAPTCHA]")
    captcha_solver=getTextToSpeechCaptchaResolver(browserWrapper=browser)
    if len(googleClass)>0:
        captcha_solver.resolve()
        sleep(2)
        browser.switch_to.parent_frame()   

    browser.find_element(By.ID, "signup_age").click()
    browser.find_element(By.ID, "signup_certify").click()

    browser.find_element(By.NAME, "submit_signup").click()
    email_activation(browser)
    time.sleep(5)
    login(browser,username,password)
    upload(browser=browser,url="https://www.xfreehd.com/upload/video",video_url=video_url,title=title,tags=tags)
    return


    db=getDatabaseWrapperInstance(table_name="spankbang_account")
    db.insert(collection="accounts",data={
        "username":username,
        "email":email,
        "password":password,
        "video":video_url,
        "tags":tags
    })

