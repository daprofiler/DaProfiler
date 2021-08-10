from googlesearch import search

def twitter_search(name,pren):
    dork = 'site:twitter.com intitle:") | Twitter" "{} {}"'.format(pren,name)
    results = search(dork,num_results=1)
    if len(results) > 0:
        return(results)
    else:
        return None
