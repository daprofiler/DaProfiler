import requests, bs4
from bs4      import BeautifulSoup

def bfmtv_search(name,pren):
    try:
        r = requests.get("https://dirigeants.bfmtv.com/recherche/q/{}5+{}6".format(name,pren))
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)
        try:
            full_name = soup.find('a',{'class':'nom'}).text+" "+soup.find('td',{'class':'verif_col2'}).text
            naissance = soup.find('td',{'class':'verif_col3'}).text.replace('Né le ','')
            mandats = soup.find('td',{'class':'verif_col5'}).text
            fonction = soup.find('td',{'class':'verif_col4'}).text
            link = soup.find('a',{'class':'nom'})
            link = str(link).replace('<a class="nom" href="/','').split('"')[0]
            link = ("https:/"+link)
            r = requests.get(link)
            page = r.content
            features = "html.parser"
            soup = BeautifulSoup(page, features)
            entreprise = soup.find('h3',{'class':'subtitle'}).text.strip()
            #adresse = soup.find('p',{'class':'mid'}).text.strip()
            adresse_full= str(soup.find('a',{'class':'visible-smallDevice link'})).split('"_blank">')[1]
            adresse       = adresse_full.split("<br/>")[0]
            cp            = adresse_full.split("<br/>")[1].split("</a>")[0]
            text = {"addr":adresse+cp,'company':entreprise,'link':link,'full_name':full_name,'naissance':naissance,'mandats':mandats,'fonction':fonction}
            return text
        except AttributeError:
            return None
    except:
        return None
