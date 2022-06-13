import requests, bs4, re
from bs4 import BeautifulSoup

def facebook_search(name,pren):
    url = "https://fr-fr.facebook.com/public/{}-{}".format(pren,name)
    page = requests.get(url).content.decode('utf-8')
    nameAccount = re.findall("width=\"72\" height=\"72\" alt=\"([a-zA-Z0-9_ é , ]+)\" />", page)
    total_accounts = []
    for i in nameAccount:
        if name.lower() in i.lower() and pren.lower() in i.lower():
            total_accounts.append(i)
        else:
            pass
    if len(total_accounts) == 0:
        return None
    else:
        return total_accounts

'''
This code cand be found at : 
https://github.com/lulz3xploit/LittleBrother/blob/master/core/facebookSearchTool.py
'''
