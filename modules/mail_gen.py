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
    bar = tqdm(desc='Mail permutation',total=len(results))
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
        emails = []
        i = i.lower()
        with open('modules/mail_domain.txt','r') as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            if "@" in line and "." in line:
                emails.append(i+line)
        bar = tqdm(desc="Searching for target emails on each domains".format(line.split('@')[1]),total=len(emails))
        for i in emails:
            a = mail_check.verify(mail=i)
            bar.update(1)
            if a is not None:
                valid_emails.append(i)
    return valid_emails
