from googlesearch import search
from linkedin_api import Linkedin

def linkedin_search(name,pren):
    try:
        a = search('"{} {}" -intitle:"profiles" -inurl:"dir/ " site:fr.linkedin.com/in/ OR site:fr.linkedin.com/pub/'.format(pren,name), lang="fr")
        if len(a) > 0:
            if name.lower() in a[0] and pren.lower() in a[0]:
                return a[0]
        else:
            return None
    except:
        pass

def official_linkedin_search(name,pren):
    username = ""
    password = ""

    if len(username) == 0:
        return None
    else:
        api = Linkedin(username=username,password=password)

        profile_data = api.search_people(keyword_first_name=pren,keyword_last_name=name)

        if len(profile_data) == 0:
            return None
        else:
            public_id       = profile_data[0]['public_id']
            urn_id          = profile_data[0]['urn_id']
            profile_infos   = api.get_profile(urn_id=urn_id,public_id=public_id)
            profile_contact = api.get_profile_contact_info(urn_id=urn_id,public_id=public_id)
            email_adress    = profile_contact['email_address']
            twitters        = profile_contact['twitter']
            birthdate       = profile_contact['birthdate']
            phone_numbers   = profile_contact['phone_numbers']
            try:
                job = (profile_infos['headline'])
            except:
                job = None

            data = {
                'Job':job,
                'email':email_adress,
                'urnid':urn_id,
                'url':'https://www.linkedin.com/in/'+public_id,
                'twitters':twitters,
                'birthdate':birthdate,
                'phone_numbers':phone_numbers
            }
            return data


