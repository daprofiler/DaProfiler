import requests, bs4, json
from bs4 import BeautifulSoup

def check_response(url):
    r = requests.get(url,allow_redirects=False)
    status = r.status_code
    if status == 200:
        return True
    else:
        return None
        
def copains_davant(name,pren):
    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With':'XMLHttpRequest'
    }
    r = requests.get(url='http://copainsdavant.linternaute.com/s/?full=&q={} {}&ty=1&xhr='.format(pren,name),headers=headers)
    try:
        pagephone = r.content.decode().split(',"$data":')[1].split('{"copains":')[1]
        dataa = pagephone[:-2]
        data = json.loads(dataa)
        users_list = data['users']
        user_list = []
        for i in users_list:
            i = str(i).strip()
            if i != "0":
                user_list.append(i)
        new_verified = []
        for i in user_list:
            url = "https://copainsdavant.linternaute.com/p/{}-{}-{}".format(pren,name,i)
            response_code = check_response(url)
            if response_code is not None:
                new_verified.append(url)

        profil_url = new_verified[0]
        r = requests.get(allow_redirects=False,url='{}'.format(profil_url))
        pagephone = r.content
        featuresphone = "html.parser"
        soup = BeautifulSoup(pagephone,featuresphone)
        try:
            localisation = str(soup.find('span',{'class':'locality'}).text)
            naissance = str(soup.find('abbr',{'class':'bday'}).text.strip())
            name_full = str(soup.find('a',{'class':'url'}).text.strip())
            photo = str(soup.find('img',{'itemprop':'logo'})).split('itemprop="logo" src="')[1].split('"')[0]
            locations = soup.find_all('span',{'class':'copains_career__city jCcareerTown'})
            dates     = soup.find_all('span',{'class':'copains_career__date jCareerDate'})

            location_list = []

            for i in range(len(locations)):
                locat = locations[i].text.strip()
                dat   = dates[i].text.replace('maintenant','Now').strip()
                data = dat+" | "+locat
                if data not in location_list:
                    temp_list = []
                    for i in location_list:
                        if locat in i:
                            temp_list.append('.')
                    if len(temp_list) == 0:
                        location_list.append(data)

            if len(location_list) == 0:
                location_list = None
            if "/anonymousL.jpg" in photo:
                photo = "None"
            card = soup.find('section',{'id':'vcard'}).text.strip()
            job = "None"
            nb_kids = "None"
            situation_familiale = "None"
            if "Situation familiale" in card:
                situation_familiale = card.split('Situation familiale :')[1].split(' ')[0].strip()
                situation_familiale = situation_familiale.strip()
            if "Profession" in card:
                job = card.split('Profession :')[1].split(' ')[0]
                job = " ".join(job.split()).split(' ')[0]
            if "Enfant" in card:
                nb_kids = card.split("Enfants :")[1].split(" ")[0]
            text = {'Other_locations':location_list,'url_full':'copainsdavant.linternaute.com{}'.format(profil_url),'familial_situation':str(situation_familiale).replace('Enfants','').replace('Aucune','').strip(),'full_name':str(name_full),'born':str(naissance),'localisation':str(localisation),
                "nb_enfants":str(nb_kids).strip(),"Job":str(job).strip(),'pdp':str(photo),    
            }
            return text
        except AttributeError:
            return None
    except IndexError:
        return None
