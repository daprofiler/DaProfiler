#trouvé sur "https://docs.isitarealemail.com/how-to-validate-email-addresses-in-python"
# modifié (un peu) par eupone
import requests

def verify(mail):
    response = requests.get("https://isitarealemail.com/api/email/validate?email={}".format(mail),params = {'Authorization':'fa86a707-750e-485c-8ec3-86eddd7ec4d0'},headers = {'Authorization': "Bearer fa86a707-750e-485c-8ec3-86eddd7ec4d0"})
    try:
        data = response.json()
        status = data['status']
        if status == "valid":
            return True
        elif status == "invalid":
            return None
        else:
            return None
    except:
        return None
