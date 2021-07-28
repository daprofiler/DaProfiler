import threading, requests, bs4
from tqdm import tqdm
from bs4  import BeautifulSoup
from modules import mail_check

def check(name,pren):
    name = name.lower()
    pren = pren.lower()
    results = [
        "{}.{}@gmail.com".format(name,pren),
        "{}.{}@yahoo.com".format(name,pren),
        "{}{}@yahoo.com".format(name,pren),
        #"{}{}@yahoo.fr".format(name,pren),
        "{}.{}@hotmail.com".format(name,pren),
        "{}{}@hotmail.com".format(name,pren),
        #"{}{}@hotmail.fr".format(name,pren),
        #"{}{}@outlook.fr".format(name,pren),
        "{}.{}@outlook.com".format(name,pren),
        "{}{}@outlook.com".format(name,pren),    
    ]
    valid_mails = []
    bar = tqdm(desc='Checking for emails validity',total=len(results))
    for i in results:
        a = mail_check.verify(mail=i)
        bar.update(1)
        if a is not None:
            valid_mails.append(i)
    return valid_mails

def skype2email(name,pren):
    url = f"https://www.skypli.com/search/{name} {pren}"
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    profiles = soup.find_all('span',{'class':'search-results__block-info-username'})[0:5]

    profiless = []

    for i in profiles:
        if "live:." in i.text:
            pass
        else:
            profiless.append(i.text.replace('live:','').replace('_1',''))

    valid_emails = []

    for i in profiless:
        i = i.lower()
        emails = [
            i+"@aol.com",
            i+"@yahoo.com",
            i+"@gmail.com",
            i+"@hotmail.com",
            i+"@icloud.com",
            i+"@yandex.ru",
            i+"@outlook.com"
        ]
        bar = tqdm(desc="Searching for mail domain on {}".format(i),total=len(emails))
        for i in emails:
            a = mail_check.verify(mail=i)
            bar.update(1)
            if a is not None:
                valid_emails.append(i)
    return valid_emails
