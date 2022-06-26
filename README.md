> Depreciated for the moment, please wait Daprofiler v2, thx

> Any update ? create a branch named `added-YOUUPDATE` and open a pull request. Your code will be checked

![alt text](./files/logo.png)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/TheRealDalunacrobate/daprofiler)
![](https://visitor-badge.laobi.icu/badge?page_id=TheRealDalunacrobate.daprofiler)


DaProfiler is an OSINT tool allowing you to collect certain information about yourself in order to rectify by rgpd requests the traces you may have left on the net.
DaProfiler is indeed able to recover: Addresses, Social media accounts, e-mail addresses, mobile / landline number, jobs. On a specified subject in a limited time.
DaProfiler is designed for Educational Purposes only, We accept no responsibility for the use you make of it.

# DaProfiler

DaProfiler allows you to create a profile on your **target** based in France only.
The particularity of this program is its ability to find the e-mail addresses of a target via searches on [Skype](https://www.skype.com/), [Pinterest](https://www.pinterest.com) and tests of combining e-mail addresses followed by a check to know if the email address exists or not (Beware of false negatives, the results displayed do not necessarily relate to the target you are looking for if another person has the same name - first name). DaProfiler is also able to check the words of a an instagram bio to find interesting information such as : **Email addresses**, **Paypal.me profiles**,**Sexual Orientation**,**City**,**School**,**Age**,**Ethnicity**,**Religions**,**Hobbies** and more ...

Official website [www.cnil.me/daprofiler/](https://www.cnil.me/daprofiler/)

## Install

Python 3.8 required
```bash
git clone https://github.com/TheRealDalunacrobate/DaProfiler.git
cd DaProfiler
pip install -r requirements.txt
```
## Use

```bash
usage: profiler.py [-h] [-n NAME] [-ln LASTNAME] [-u UPDATE]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Victim name
  -ln LASTNAME, --lastname LASTNAME
                        Last name of victim
  -u true, --update true
                        Update DaProfiler
  -json true, --json true
                        Print result in json
```

## Demo
![alt text](https://i.ibb.co/XSzG90S/Capture-censored.jpg)

## Api
| Source | Service type | Subscription | Key in code |
| :---: | :---: | :---: | :---: |
| Leakcheck.net | Breach Search | Premium | No | 
| apilayer.net | Phone infos | Free (In code) | Yes |

Add your premium api keys :
+ Go to [modules\api_modules](https://github.com/TheRealDalunacrobate/DaProfiler/tree/main/modules/api_modules) then open your API module (ex Leakcheck), replace "YOUR_KEY" to your key, save and quit your text editor.

> educational propose only


# Contact
Mail : _daluna_pro@protonmail.ch_. <br>
Discord : `Dalunacrobate#9010` <br>


## Contributions
All suggestions are welcome.

## Code parts used under license and authors
+ [Palenath - Instagram Advanced Lookup Function](https://github.com/megadose/toutatis)
