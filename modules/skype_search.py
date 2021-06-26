import requests, bs4
from bs4 import BeautifulSoup

from modules import mail_check

def skype_searchh(name,pren):
    url = f"https://www.skypli.com/search/{name} {pren}"
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    profiles = soup.find_all('span',{'class':'search-results__block-info-username'})[0:5]

    profiless = []

    for i in profiles:
        profiless.append(i.text)

    profile_dict = []

    for i in profiless:
        r = requests.get('https://www.skypli.com/profile/{}'.format(i))
        page = r.content
        if "Page not found." in r.text:
            full_name = ""
        else:
            features = "html.parser"
            soup = BeautifulSoup(page, features)
            name = soup.find_all('div',{'class':'profile-box__table-value'})[1]
            full_name = (name.text.strip())

        profile_dict.append('{} \t| {}'.format(i,full_name))
    return profile_dict
