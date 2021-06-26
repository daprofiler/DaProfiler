import requests
import json

url = 'https://cnil.me/api/osint/daprofiler/ui'
myobj = json.dumps({
    "Name": "philippe",
    "LastName": "semelier",
    "UI": {
        "Pie": {
            "PersonnalLife": 3,
            "SocialMedias": 4
        },
        "Bar": {
            "TwitterFounds": 2,
            "InstagramFounds": 5,
            "FacebookFounds": 5,
            "SkypeFounds": 4
        }
    },
    "AdressPhone": {
        "Exists": True,
        "FullName": "Semelier Philippe",
        "Adress": "4 IMPASSE DES PLATANES49400 Rou Marson",
        "Phone": "02 41 50 42 13",
        "PhoneLocation": "Saumur"
    },
    "Work": {
        "Exists": True,
        "FullName": "SEMELIER Philippe",
        "BornDate": "08/08/1970",
        "Company": "SARL SP AUTOMOBILES",
        "Function": "Gérant",
        "Warrant": "1 mandat",
        "Link": "dirigeants.bfmtv.com/Philippe-SEMELIER-1204273/"
    },
    "DeathRecords": {
        "Exists": True,
        "Records": [
            {
                "Name": "Monsieur René  SEMELIER",
                "Loc": " 79410 Échiré"
            },
            {
                "Name": "Madame Chantale  SEMELIER née GABORIT",
                "Loc": " 79410 Échiré"
            },
            {
                "Name": "Madame Marcelle SEMELIER née TOUCHE",
                "Loc": " 37270 Athée-sur-Cher"
            },
            {
                "Name": "Monsieur Raoul SEMELIER",
                "Loc": " 79410 Échiré"
            },
            {
                "Name": "Madame Liliane SEMELIER née RUSSEIL",
                "Loc": " 79310 Mazières-en-Gâtine"
            }
        ]
    },
    "Emails": {
        "HighProbEmails": [
            "philippe.semelier@yahoo.com",
            "philippe.semelier@gmail.com",
            "philippe.semelier@hotmail.fr",
            "philippe.semelier@outlook.fr",
            "philippe.semelier@outlook.com",
            "philippesemelier@gmail.com",
            "philippesemelier@hotmail.com",
            "philippesemelier@hotmail.fr"
        ],
        "PermutatedMailbox": [
            "semelier.philippe@gmail.com"
        ]
    },
    "Facebook": {
        "Exists": True,
        "AccountList": [
            "Philippe Semelier",
            "Philippe Semelier",
            "Philippe Semelier",
            "Philippe Semelier",
            "Philippe Semelier"
        ]
    },
    "Skype": {
        "Exists": True,
        "AccountList": [
            "live:.cid.d9fbcf33436c9ba1 \t| Philippe Semelier",
            "live:philippe.semelier \t| philippe semelier",
            "live:philippe.semelier_1 \t| philippe semelier",
            "live:philippesemelier_1 \t| PHILIPPE ANNE MARIE SEMELIER"
        ]
    },
    "Instagram": {
        "Exists": True,
        "AccountList": [
            {
                "Username": "philippesemelier",
                "obfuscated_phone": False,
                "obfuscated_email": "p*******r@o*****.fr"
            },
            {
                "Username": "semelierphilippe",
                "obfuscated_phone": False,
                "obfuscated_email": False
            },
            {
                "Username": "semelierphilippe7658",
                "obfuscated_phone": False,
                "obfuscated_email": False
            },
            {
                "Username": "psemelier",
                "obfuscated_phone": "+33 * ** ** ** 79",
                "obfuscated_email": False
            },
            {
                "Username": "semelierp",
                "obfuscated_phone": False,
                "obfuscated_email": False
            }
        ]
    },
    "Twitter": {
        "Exists": True,
        "AccountList": False,
        "Accounts": [
            "@SemelierP\t|semelier philippe",
            "@SemelierTintin\t|semelier philippe"
        ]
    },
    "CopainsDavant": {
        "Exists": True,
        "Job": False,
        "NbKids": False,
        "FullName": "Philippe SEMELIER",
        "BornDate": "1959",
        "Location": "ROU-MARSON",
        "FSituation": False,
        "ProfilePicUrl": "image-uniservice.linternaute.com/image/450/1989294738/11664774.jpg",
        "ProfileUrl": "copainsdavant.linternaute.com/p/philippe-semelier-20147555",
        "OtherLocations": [
            "1973 - Now | Thouars"
        ]
    }
})

x = requests.post(url, data = myobj)
y = json.loads(x.text) 

print("Website Done")

f = open("index.html", "w")
f.write(y['content']["webpage"])
f.close()

f = open("./cg/data.json", "w")
f.write(y['content']["arbre"])
f.close()

import http.server
import http.server, socketserver, webbrowser
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

webbrowser.open('http://127.0.0.1:8000', new=2)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


