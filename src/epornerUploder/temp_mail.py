import requests
import time
import json
import bs4


def get_email():
    res=requests.post('https://api.internal.temp-mail.io/api/v3/email/new',json={"min_name_length":10,"max_name_length":10})
    data=json.loads(res.text) 
    return data["email"]

def get_activation_link(email):
    activation_link=""
    while not activation_link:
        try:
            message=requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages')
            message=json.loads(message.text)
            msg_html=message[0]['body_html']
            soup=bs4.BeautifulSoup(msg_html,'html.parser')
            activation_link=soup.select_one('[href^="https://www.eporner.com/login/verify/"]')['href']
            time.sleep(2)
        except Exception as e:
            print(e)
    return activation_link