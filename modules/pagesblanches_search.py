import requests, bs4, colorama
from colorama import Fore
from bs4      import BeautifulSoup

def adresse_search(name,pren,zipc):
    if zipc is not None:
        r = requests.get('https://www.118000.fr/search?part=1&label={}&who={} {}'.format(zipc,name,pren))
    else:
        r = requests.get('https://www.118000.fr/search?part=1&who={} {}'.format(name,pren))
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    target_name = soup.find("h2", {"class": "name title inbl"})
    target_addr = soup.find("div", {"class": "h4 address mtreset"})
    target_phon = soup.find('a',{'class':'clickable atel'})
    if target_name is not None:
        return  {'Not_Sure':False,'Phone':phon_full,'Name':name_full,'Adress':addr_full,'Type_tel':None,"Loc_phone":None,'carrier':None}
    elif target_name is None:
        try:
            r = requests.get('https://www.118000.fr/search?part=1&label={}&who={}'.format(zipc,name))
            page = r.content
            features = "html.parser"
            soup = BeautifulSoup(page, features)

            name_full = soup.find("h2", {"class": "name title inbl"}).text.strip()
            addr_full = soup.find("div", {"class": "h4 address mtreset"}).text.replace(', voir sur la carte','').replace('\n',' ').strip()
            phon_full = soup.find('a',{'class':'clickable atel'}).text.strip()

            return  {'Not_Sure':True,'Phone':phon_full,'Name':name_full,'Adress':addr_full,'Type_tel':None,"Loc_phone":None,'carrier':None}
        except AttributeError:
            return None
