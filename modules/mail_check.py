import requests

def verify(mail):
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': mail},headers = {'Authorization': "Bearer " + "21000771-6911-402d-9d32-7697238803e8" })
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
