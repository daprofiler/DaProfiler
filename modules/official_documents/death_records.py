import profile
import requests,bs4
from bs4 import BeautifulSoup

def death_search(name,pren):
    try:
        url = "https://www.libramemoria.com/avis?nom={}&prenom={}&debut=&fin=&departement=&commune=&communeName=&titre=".format(name,pren)
        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        names  = soup.find_all('div',{'class':'cellule nom alone'})
        ages   = soup.find_all('div',{'class':'cellule age hideXs_tablecell alone'})
        villes = soup.find_all('div',{'class':'cellule ville liste_virgule alone'})

        profile_list = []

        for i in range(len(names)):
            try:
                name = names[i].text.split('(')[0].replace('\r','').replace('\n','').replace('\t','').strip()
                loc  = villes[i].text.replace('\r','').replace('\n','').replace('\t','').replace('(',' (').strip()
                age  = ages[i].text.replace("ans","Years old").strip()
                dictt = {'Name':name,'Age':str(age),'Loc':loc.replace('- ','')}
                profile_list.append(dictt)
            except:
                pass

        if len(names) == 0:
            return None
        else:
            return profile_list

    except KeyboardInterrupt:
        return None
