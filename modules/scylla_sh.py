import requests

def scylla_search(email):
    try:
        r = requests.get('https://scylla.so/search?q=email:{}'.format(email))
        if r.status_code == 500 or r.status_code == 502:
            return None
        try:
            response = r.json()
            if len(response) == 0:
                return None
            else:
                total = []
                for i in response[0:10]:
                    leak_name = i['fields']['domain']
                    try:
                        password = i['fields']['password']
                    except:
                        password = i['fields']['passhash']
                    text = {
                        'Name':leak_name,
                        'Password':password
                    }
                    total.append(text)
                return total
        except:
            return None
    except requests.exceptions.ConnectionError:
        return None

# By Lui#6166 from Prism Intelligence Group
