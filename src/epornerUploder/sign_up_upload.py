from time import sleep
from selenium.webdriver.common.by import By
from string import ascii_letters
import random
from epornerUploder.dependency.faker.Faker import getFakerInstance
import time
import os
from selenium.webdriver.common.keys import Keys
from epornerUploder.temp_mail import get_activation_link,get_email

BASE_DIR=os.getcwd()

def getRandomString(length):
    return ''.join(random.choice(ascii_letters) for i in range(length))

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
        
        browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(f"{BASE_DIR}/tmp/tmp.mp4")
        time.sleep(2)
        browser.execute_script(''' document.querySelector("#typehome").click()''')
        time.sleep(1)
        browser.execute_script('''document.querySelector("#upformsubmitbtn").click() ''')
        print("UPLOADED")
        
        time.sleep(300)
    except Exception as e:
        print(e)

def get_temp_email():
    return get_email()

def email_activation(email):
    try:
        link=get_activation_link(email)
        return link
    except Exception as e:
        print(e)

def login(browser,username,password):
    browser.get("https://www.eporner.com/login")
    browser.set_window_size(955, 1095)

    browser.execute_script('''EP.footer.closeAgeVerif();''')
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(username)
    browser.find_element(By.CSS_SELECTOR, '[name="haslo"]').click()
    browser.find_element(By.CSS_SELECTOR, '[name="haslo"]').send_keys(password)
    browser.find_element(By.ID, "rememberme").click()
    browser.find_element(By.CSS_SELECTOR, '[name="Submit"]').click()

def sign_up(browser):

    email=get_temp_email()

    [username,password]=get_random_user_cred()
    print(username,email,password)
    sleep(2)
    
    browser.get("https://www.eporner.com/")
    browser.find_element(By.CSS_SELECTOR, "#headmenu > a:nth-child(2)").click()
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR, "#createform > input:nth-child(4)").click()
    browser.find_element(By.CSS_SELECTOR, "#createform > input:nth-child(4)").send_keys(username.lower())
    browser.find_element(By.CSS_SELECTOR, "#createform-passwords > input:nth-child(3)").send_keys(password)
    browser.find_element(By.NAME, "haslo2").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "#createform > input:nth-child(10)").click()
    browser.find_element(By.CSS_SELECTOR, "#createform > input:nth-child(10)").send_keys(email)

    browser.execute_script('''EP.account.create.postModal();''')
    time.sleep(5)
    link=email_activation(email)
    browser.get(link)

    return [username,password]

