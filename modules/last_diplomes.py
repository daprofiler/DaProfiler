import requests
from bs4 import BeautifulSoup

def last_diplomes(name,pren):
    try:
        url = f'https://resultats.etudiant.lefigaro.fr/resultats-brevet/recherche?name={pren} {name}&city_label=&city_insee='
        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)
        profiles = soup.find_all('div',{'class':'candidate'})    
        for i in profiles:
            profile = str(i).lower()
            if pren.lower() in profile and name.lower() in profile:
                url = "https://resultats.etudiant.lefigaro.fr"+profile.split('href')[1].split('"')[1]
                r = requests.get(url)
                page = r.content
                features = "html.parser"
                soup = BeautifulSoup(page, features)
                academie = str(soup.find('span',{'class':'subtitle'})).split('">')[1].split('</')[0]
                mention  = str(soup.find('p',{'class':'mention'})).split('">')[1].split('<')[0].strip()
                ville    = str(soup.find('div',{'class':'infos'})).split('href')[1].split('</a>')[0].split('">')[1]
                diplome  = str(soup.find('div',{'class':'infos'})).split('<p>')[1].split('</p>')[0]
                
                json_output = {
                    'academie':academie,
                    'mention':mention,
                    'ville':ville,
                    'Diplome':diplome
                }
                return json_output
            else:
                return None
    except:
        return None