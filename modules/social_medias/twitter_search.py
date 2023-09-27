import requests, bs4
from bs4 import BeautifulSoup

def twitter_search(name,pren):
    url = "https://twstalker.com/search/?q={} {}".format(pren,name)
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    usernames = []

    username = soup.find_all('div',{'class':'user-request-dt'})
    
    for i in username:
        i = str(i).split('@')[1].split('</span')[0].replace('\'','')
        usernames.append('@'+i.strip())

    return usernames

