import requests

def verify(mail):
    try:
        response = requests.get("https://isitarealemail.com/api/email/validate",timeout=1.5,params = {'email': mail},headers = {'Authorization': "Bearer " + "21a3f468-1c3a-43d6-bdd6-d5437d6c0252" })
        try:
            data = response.json()
            status = data['status']
            if status == "valid":
                return "True"
            else:
                return None
        except:
            return None
    except:
        return None
