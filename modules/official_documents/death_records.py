import profile
import requests,bs4
from bs4 import BeautifulSoup

def death_search(name,pren):
    try:
        url = "https://avis-deces.linternaute.com/recherche-avis?q={} {}".format(name,pren)
        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        names  = soup.find_all('h4')
        ages   = soup.find_all('small')
        villes = soup.find_all('div',{'class':'odResultList__details--death'})
        profile_list = []

        for i in range(len(names)):
            try:
                name = names[i].text.split('(')[0].replace('\r','').replace('\n','').replace('\t','').strip()
                loc  = villes[i].text.split('à')[1].replace('\n','').replace('                     ','').strip()
                age  = ages[i].text.strip()
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
