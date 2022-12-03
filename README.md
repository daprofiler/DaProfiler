![alt text](https://github.com/daprofiler/DaProfiler/blob/main/files/DaProfiler_Logo.png?raw=true)


![](https://visitor-badge.laobi.icu/badge?page_id=TheRealDalunacrobate.daprofiler)

DaProfiler is an OSINT tool allowing you to collect certain information about yourself in order to rectify by rgpd requests the traces you may have left on the net.
DaProfiler is indeed able to recover: Addresses, Social media accounts, e-mail addresses, mobile / landline number, jobs. On a specified subject in a limited time.
DaProfiler is designed for Educational Purposes only, We accept no responsibility for the use you make of it.

## Install

Python 3.8 & Mozilla Firefox required
```bash
git clone https://github.com/TheRealDalunacrobate/DaProfiler.git
cd DaProfiler
pip install -r requirements.txt
```
## Use

```bash

usage: profiler.py [-h] [-n NAME] [-ln LASTNAME] [-json JSON] [-zp ZP]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Victim name
  -ln LASTNAME, --lastname LASTNAME
                        Last name of victim
  -json JSON, --json JSON
                        Print result in json
  -zp ZP, --zp ZP       Zip code (Optional)
```
## Exemple
```
py profiler.py -n john -ln doe -zp 75012 -json true
```
## Demo
![alt text](https://i.ibb.co/XSzG90S/Capture-censored.jpg)

## Api

| Source | Service type | Subscription |
| :----: | :----------: | :----------: |
| Leakcheck.net | Breach Search | Premium | 

+ Go to [modules\api_modules](https://github.com/TheRealDalunacrobate/DaProfiler/tree/main/modules/api_modules) then open your API module (ex Leakcheck), replace "YOUR_KEY" to your key, save and quit your text editor.


# Connect to LinkedIN API
+ Go to [modules\linkedin_search](https://github.com/daprofiler/DaProfiler/blob/main/modules/linkedin_search.py) then add your creditentials.

# Contact
Mail : _daluna_pro@protonmail.ch_. <br>

## Contributions
All suggestions are welcome.

## Code parts used under license and authors
+ [Palenath - Instagram Advanced Lookup Function](https://github.com/megadose/toutatis)
