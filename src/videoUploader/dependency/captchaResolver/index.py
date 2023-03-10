
from .CaptchaSolver import CaptchaSolver
from videoUploader.dependency.selenium.Selenium import getSeleniumBrowserAutomation
import requests
 
def getTextToSpeechCaptchaResolver(browserWrapper)-> CaptchaSolver:
    if not browserWrapper:
        browserWrapper=getSeleniumBrowserAutomation()
        
    return CaptchaSolver(browserWrapper=browserWrapper,requests=requests)