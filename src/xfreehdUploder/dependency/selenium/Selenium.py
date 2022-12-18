from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random

import os
import shutil
import tempfile


def get_proxies():
    ips=[    
        '161.77.116.22',
        '161.77.116.70',
        '161.77.117.249',
        '161.77.116.217',
        '161.77.118.75',
        '161.77.117.16',
        '161.77.119.225',
        '161.77.118.55',
        '161.77.119.33',
        '161.77.118.98']
    ip=random.choice(ips)
    return (ip, 12323, "14a49f98146a6", "360a6e122f")

def getSeleniumBrowserAutomation():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("start-maximized")
    
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)

    
    # chrome_options.add_argument('--headless')
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



    # proxy =  get_proxies()
    # proxy_extension = ProxyExtension(*proxy)

    # chrome_options.add_argument(f"--load-extension={proxy_extension.directory}")

    driver = webdriver.Chrome(options=chrome_options,executable_path='/opt/chromedriver/chromedriver')

    print(driver.session_id)


    return driver




class ProxyExtension:
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {"scripts": ["background.js"]},
        "minimum_chrome_version": "76.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: %d
            },
            bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        { urls: ["<all_urls>"] },
        ['blocking']
    );
    """

    def __init__(self, host, port, user, password):
        self._dir = os.path.normpath(tempfile.mkdtemp())

        manifest_file = os.path.join(self._dir, "manifest.json")
        with open(manifest_file, mode="w") as f:
            f.write(self.manifest_json)

        background_js = self.background_js % (host, port, user, password)
        background_file = os.path.join(self._dir, "background.js")
        with open(background_file, mode="w") as f:
            f.write(background_js)

    @property
    def directory(self):
        return self._dir

    def __del__(self):
        shutil.rmtree(self._dir)
