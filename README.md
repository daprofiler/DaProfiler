[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/TheRealDalunacrobate/daprofiler)
![](https://visitor-badge.laobi.icu/badge?page_id=TheRealDalunacrobate.daprofiler)

For educational purposes only.

![alt text](https://i.ibb.co/1vbRgZm/banner.png)
# DaProfiler

DaProfiler allows you to create a profile on your **target** based in France only.
The particularity of this program is its ability to find the e-mail addresses of a target via searches on [Skype](https://www.skype.com/) and tests of combining e-mail addresses followed by a check to know if the email address exists or not (Beware of false negatives, the results displayed do not necessarily relate to the target you are looking for if another person has the same name - first name). DaProfiler is also able to check the words of a an instagram bio to find interesting information such as : **Email addresses**, **Paypal.me profiles**,**Sexual Orientation**,**City**,**School**,**Age**,**Ethnicity**,**Religions**,**Hobbies** and more ...

## 🛠 Installation - Linux

Python 3.8 required
```bash
git clone https://github.com/TheRealDalunacrobate/DaProfiler.git
cd DaProfiler
pip install -r requirements.txt
```
## 💻 Use
```bash
profiler.py -n [NAME] -ln [LAST NAME] -l True -O txt_file.txt
(Target Name) (Target Last Name) (Enable Terminal Logging) (Output to txt_file.txt)

=====================================================================

usage: profiler.py [-h] [-n NAME] [-l LOGGING] [-ln LASTNAME] [-O OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Victim name
  -l LOGGING, --logging LOGGING
                        Enable terminal logging (Optional)
  -ln LASTNAME, --lastname LASTNAME
                        Last name of victim
  -O OUTPUT, --output OUTPUT
                        ( -O output.txt )
```

## 📷 Demo
![alt text](https://i.ibb.co/YPHwv39/hh.png)

## 🛠 Api
| Source | Service type | Subscription | Key in code |
| :---: | :---: | :---: | :---: |
| Leakcheck.net | Breach Search | Premium 🔑 | ❌ | 
| apilayer.net | Phone infos | Free ✅ | ✅ |

Add your premium api keys :
+ Go to [modules\api_modules](https://github.com/TheRealDalunacrobate/DaProfiler/tree/main/modules/api_modules) then open your API module (ex Leakcheck), replace "YOUR_KEY" to your key, save and quit your text editor.

##  📝 Contact
Mail : _daluna_pro@protonmail.ch_. <br>
Discord : `Dalunacrobate#6166` <br>
Discord server : [Here](https://discord.gg/4h57QSsEYa)


## 📚 Contributions
All suggestions are welcome.

![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)

