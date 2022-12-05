import requests
from bs4 import BeautifulSoup

def last_diplomes_bac(name,pren):
    url = f'https://resultats.etudiant.lefigaro.fr/resultats-bac/recherche?name={pren} {name}&city_label=&city_insee='
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)
    profiles = soup.find_all('td',{'class':'svelte-11did2l'})   
    listt = [] 
    for i in profiles:
        if len(listt) == 1:
            subject = listt[0]
            link = "https://resultats.etudiant.lefigaro.fr"+subject.split('href="')[1].split('">')[0]

            academie = None
            mention  = None
            ville    = None
            diplome  = None

            r        = requests.get(link)
            page     = r.content
            features = "html.parser"
            soup     = BeautifulSoup(page, features)

            mention  = soup.find('span',{'class':'block text-4xl text-red'}).text.split('"')[1].split('"')[0]
            diplome  = soup.find('p',{'class':'text-grey-600 mb-1'}).text.strip()
            academie = soup.find('div',{'class':'flex flex-col items-center sm:flex-row flex-wrap gap-5'}).text.split(',')[1].strip()
            city     = soup.find('a',{'class':'capitalize underline'}).text.strip()

            json_output = {
                'Exists':True,
                'academie':academie,
                'Link':link,
                'mention':mention,
                'ville':city,
                'Diplome':diplome
            }
            return json_output
        elif len(listt) == 0:
            profile = str(i).lower()
            if pren.lower() in profile and name.lower() in profile:
                    listt.append(profile)

                    
def last_diplomes_brevet(name,pren):
    url = f'https://resultats.etudiant.lefigaro.fr/resultats-brevet/recherche?name={pren} {name}&city_label=&city_insee='
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)
    profiles = soup.find_all('div',{'class':'bg-white p-2'})    
    for i in profiles:
        profile = str(i).lower()
        if pren.lower() in profile and name.lower() in profile:
            url = "https://resultats.etudiant.lefigaro.fr"+profile.split('href')[1].split('"')[1]
            r = requests.get(url)
            page = r.content
            features = "html.parser"
            soup = BeautifulSoup(page, features)
            
            profile = soup.find('div',{'class':'box'})
            mention = soup.find('span',{'class':'block text-4xl text-red'})
            diplome = soup.find('p',{'class':'text-grey-600 mb-1'})

            diplome    = str(diplome).split('text-grey-600 mb-1">')[1].split('</p>')[0]
            nom_prenom = str(profile).split('h1>')[1].split('<span')[0]
            ville      = str(profile).split('capitalize">')[1].split('</span>')[0]
            academie   = str(profile).split('(')[1].split(')')[0]
            mention    = str(mention).split('class="block text-4xl text-red">')[1].split('</span>')[0]


            json_output = {
                'Exists':True,
                "Name":nom_prenom.strip(),
                'academie':academie,
                'Link':url,
                'mention':mention,
                'ville':ville,
                'Diplome':diplome
            }
            return json_output
