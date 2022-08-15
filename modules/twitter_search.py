import requests, bs4
from bs4 import BeautifulSoup

def twitter_search(name,pren):
    url = "https://www.sotwe.com/search/{} {}".format(pren,name)
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    usernames = []

    username = soup.find_all('div',{'class':'v-list-item__subtitle caption'})
    
    for i in username:
        usernames.append(i.text.strip())

    return usernames

