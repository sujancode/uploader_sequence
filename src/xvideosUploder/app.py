from dependency.selenium.Selenium import getSeleniumBrowserAutomation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

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

def get_temp_email(browser):
    browser.get("https://mail.tm/en/")
    time.sleep(10)
    # captcha_solver=getTextToSpeechCaptchaResolver(browserWrapper=browser)
    # googleClass=browser.find_elements(By.CSS_SELECTOR,"[title=reCAPTCHA]")

    # if len(googleClass)>0:
    #     captcha_solver.resolve()
    #     sleep(2)
    #     browser.switch_to.parent_frame()   
    email=browser.execute_script(''' return document.querySelector("#DontUseWEBuseAPI").value ''')
    return email

def sign_up():
    try:
        browser=getSeleniumBrowserAutomation()
        email=get_temp_email(browser)
        username=email.split("@")[0]
        browser.get("https://www.xvideos.com/account/create")
        time.sleep(5)

        browser.find_element(By.ID, "signup-form_details_login").send_keys(email)
        browser.find_element(By.ID, "signup-form_details_profile_name").send_keys(username)
        browser.find_element(By.ID, "signup-form_details_password").send_keys("earning$$")
        browser.find_element(By.ID,"signup-form_details_tos_pp").click()

        browser.find_element(By.ID, "btn-signup2next").click()
    except Exception as e:
        print(e)
    time.sleep(10)
sign_up()