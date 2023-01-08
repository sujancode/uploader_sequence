from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def getSeleniumBrowserAutomation():
    chrome_options = ChromeOptions()

    
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument('--disable-gpu-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument('--ignore-ssl-errors')

    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.binary_location = '/opt/chromium/chrome'
    

    driver = webdriver.Chrome(options=chrome_options,executable_path='/opt/chromedriver/chromedriver')

    print(driver.session_id)


    return driver
