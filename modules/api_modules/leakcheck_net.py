import leakcheck
from leakcheck import LeakCheckAPI

from colorama import Fore

def leak_check_api(mail):
    full_results = []
    api = LeakCheckAPI()
    """
    GET YOUR KEY AT https://leakcheck.net/ 
    """
    keyy = "YOUR_KEY" # PUT YOUR KEY HERE ONLY
    if keyy == "YOUR_KEY":
        return None
    else:
        try:
            api.set_key(keyy)
            api.set_type("email")
            api.set_query(mail)
            result = api.lookup(with_sources=1)[0:10] # LIMIT OF RESULTS == 10 YOU CAN CHANGE THIS VALUE TO PRINT MORE RESULTS
            for i in result:
                try:
                    password  = i['line']
                except IndexError:
                    password = None
                try:
                    leak_name = i['sources']
                except IndexError:
                    leak_name = None
                try:
                    leak_date = i['last_breach']
                except IndexError:
                    leak_date = None
                dict_res = {
                    'password':password,
                    'leak_name':str(leak_name).replace("'","").replace("[","").replace("]",""),
                    'leak_date':leak_date
                }
                full_results.append(dict_res)
            if len(full_results) == 0:
                return None
            return full_results
        except:
            return None
