import requests,bs4
from bs4 import BeautifulSoup

def death_search(name,pren):
    try:
        url = "https://www.avis-de-deces.net/avis-de-deces/?nomprenomdefunt={}".format(name)
        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        names   = soup.find_all('h2')
        villes  = soup.find_all('span',{'class':'ville'})
        ages    = soup.find_all('p',{'class':'list-item__adress'})
        links   = soup.find_all('a',{'class':'list__link'})

        profile_list = []

        for i in range(len(names)):
            name = names[i].text.strip()
            loc  = villes[i].text.strip()
            age  = ages[i].text.strip()
            link = links[i]
            link = (str(link).split('" title="')[0])
            link = str(link).replace('<a class="list__link" href="','').replace('https://www.','')
            profile_list.append({'Name':name,'Link':link,'Age':str(age)[0:2].replace('ans','').strip(),'Loc':loc.replace('- ','')})

        if len(profile_list) == 0:
            return None
        else:
            return profile_list
    except KeyboardInterrupt:
        return None
