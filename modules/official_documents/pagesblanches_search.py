import requests, bs4
from bs4      import BeautifulSoup

def adresse_search(name,pren,zipc):
    if zipc is not None:
        r = requests.get('https://www.118000.fr/search?part=1&label={}&who={} {}'.format(zipc,name,pren))
    else:
        r = requests.get('https://www.118000.fr/search?part=1&who={} {}'.format(name,pren))
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    target_name = soup.find("h2", {"class": "name title inbl"}).text.strip()
    target_addr = soup.find("div", {"class": "h4 address mtreset"}).text.strip()
    target_phon = soup.find('a',{'class':'clickable atel'}).text.strip()
    if target_name is not None:
        return  {'Not_Sure':True,'Phone':target_phon,'Name':target_name,'Adress':target_addr,'Type_tel':None,"Loc_phone":None,'carrier':None}
    elif target_name is None:
        try:
            r = requests.get('https://www.118000.fr/search?part=1&label={}&who={}'.format(zipc,name))
            page = r.content
            features = "html.parser"
            soup = BeautifulSoup(page, features)

            name_full = soup.find("h2", {"class": "name title inbl"}).text.strip()
            addr_full = soup.find("div", {"class": "h4 address mtreset"}).text.replace(', voir sur la carte','').replace('\n',' ').strip()
            try:
                phon_full = soup.find('a',{'class':'clickable atel'}).text.strip()
            except:
                phon_full = None
            return  {'Not_Sure':False,'Phone':phon_full,'Name':name_full,'Adress':addr_full,'Type_tel':None,"Loc_phone":None,'carrier':None}
        except AttributeError:
            return None