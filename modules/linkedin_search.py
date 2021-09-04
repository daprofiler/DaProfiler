from googlesearch import search

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
