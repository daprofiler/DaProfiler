import requests, bs4
from bs4      import BeautifulSoup

def bfmtv_search(name,pren):
    try:
        r = requests.get("https://www.verif.com/dirigeants/recherche/q/{}6+{}5".format(name,pren))
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)
        try:
            full_name = soup.find('a',{'class':'nom'}).text+" "+soup.find('td',{'class':'verif_col2'}).text
            naissance = soup.find('td',{'class':'verif_col3'}).text.replace('Né le ','')
            mandats = soup.find('td',{'class':'verif_col5'}).text
            fonction = soup.find('td',{'class':'verif_col4'}).text
            link = str(soup.find('td',{'class':'verif_col4'})).split('href="')[1].split('"')[0]
            link = str(link).replace('<a class="nom" href="/','')
            r = requests.get(link)
            page = r.content
            features = "html.parser"
            soup = BeautifulSoup(page, features)

            desc = soup.find('p',{'class':'mid hidden-smallDevice'}).text.strip()
            capital = soup.find('span',{'class':'number'}).text.strip()
            entreprise = soup.find('h3',{'class':'subtitle'}).text.strip()
            adresse_full= str(soup.find('a',{'class':'visible-smallDevice link'})).split('"_blank">')[1]
            adresse       = adresse_full.split("<br/>")[0]
            cp            = adresse_full.split("<br/>")[1].split("</a>")[0]
            text = {"Capital":capital,"Desc":desc,"addr":adresse+cp,'company':entreprise,'link':link,'full_name':full_name,'naissance':naissance,'mandats':mandats,'fonction':fonction}            
            return text
        except AttributeError:
            return None
    except:
        return None
