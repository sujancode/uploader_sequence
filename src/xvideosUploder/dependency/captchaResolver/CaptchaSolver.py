import os
import time
from selenium.webdriver.common.by import By
from .speechToText import get_large_audio_transcription

BASE_DIR="/tmp"

class CaptchaSolver:
    def __init__(self,browserWrapper,requests):
        self.browserWrapper=browserWrapper
        self.requests=requests

    def find_audio_btn(self,driver,allIframes):
        for index in range(len(allIframes)):
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME,'iframe')[index]
            driver.switch_to.frame(iframe)
            driver.implicitly_wait(1)
            try:
                audioBtn = driver.find_element(By.ID,'recaptcha-audio-button') or driver.find_element(By.ID,'recaptcha-anchor')
                audioBtn.click()
                time.sleep(2)
                return index
            except Exception as e:
                pass
        return False

    def download_audio_file(self,driver,filename):
        filepath=f"{BASE_DIR}/{filename}"
        print("downloding audio")
        href = driver.find_element(By.ID,'audio-source').get_attribute('src')
        response = self.requests.get(href, stream=True)
        
        with open(filepath, "wb") as handle:
            for data in response.iter_content():
                handle.write(data)
        return filepath

    def resolve(self):        
        driver=self.browserWrapper
        googleClass=None
        while not googleClass:
            try:
                time.sleep(1)
                print("Pressing Captcha")
                googleClass=driver.find_element(By.CSS_SELECTOR,"[title=reCAPTCHA]")
                print(googleClass)
            
            except:
                print("Error")
        
        googleClass.click()
        time.sleep(2)

        allIframes=driver.find_elements(By.TAG_NAME,"iframe")
        
        audioBtnIndex=self.find_audio_btn(driver=driver,allIframes=allIframes)
        
        if audioBtnIndex:
            try:
                while True:
                    time.sleep(3)
                    audio_path=self.download_audio_file(driver,f"1.mp3")
                    print(audio_path)
                    response = get_large_audio_transcription(audio_path)
                    print(response)
                    driver.switch_to.default_content()
                    iframe = driver.find_elements(By.TAG_NAME,'iframe')[audioBtnIndex]
                    driver.switch_to.frame(iframe)
                    inputbtn = driver.find_element(By.ID,'audio-response')
                    inputbtn.send_keys(response)
                    time.sleep(2)
                    inputbtn.send_keys("\ue007")                    
                    time.sleep(2)
                    errorMsg = driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        driver.switch_to.default_content()
                        return True
            except Exception as e:
                print(e)
                print("Most Probably Change Proxies or Use Proxies")
        return False            

        