from colorama.initialise import init
from update_check import update

## ------------------------- Update the code  -------------------------
def update_funct():
    print("\nUpdating Modules ...\n")
    update('modules/linkedin_search.py','https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/linkedin_search.py')
    update("modules/visual/logging.py","https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/visual/logging.py")
    update("modules/copainsdavant_search.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/copainsdavant_search.py")
    update("modules/death_records.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/death_records.py")
    update("modules/dirigeants_bfmtv.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/dirigeants_bfmtv.py")
    update("modules/facebook_search.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/facebook_search.py")
    update("modules/mail_check.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/mail_check.py")
    update("modules/mail_gen.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/mail_gen.py")
    update("modules/pagesblanches_search.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/pagesblanches_search.py")
    update("modules/skype_search.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/skype_search.py")
    update("modules/twitter_search.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/twitter_search.py")
    update("modules/report.json","https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/report.json")
    update("profiler.py", "https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/profiler.py")
    update("modules/mail_domain.txt","https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/modules/mail_domain.txt")
    update("requirements.txt","https://raw.githubusercontent.com/TheRealDalunacrobate/DaProfiler/main/requirements.txt")

from json import decoder
import threading, time, colorama, treelib, random, sys, os, argparse, json, requests, webbrowser, socketio, string

from tqdm       import tqdm
from treelib    import Node, Tree
from colorama   import Fore, Back, Style, init
from statistics import mean
init(autoreset=True)
from modules  import skype_search
from modules  import pagesblanches_search
from modules  import copainsdavant_search
from modules  import instagram_search
from modules  import dirigeants_bfmtv
from modules  import death_records
from modules  import twitter_search
from modules  import facebook_search
from modules  import mail_gen
from modules  import scylla_sh
from modules  import mail_check
from modules  import linkedin_search
from modules  import last_diplomes

from modules.visual      import logging
from modules.api_modules import leakcheck_net


banner = False 
# Opening json report template
data_file = open('modules/report.json','r')
data_export = json.load(data_file)
data_file.close()


# Affichage de la banniere 
def banner():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

    print("DaProfiler - Inspired from Profiler CToS #watchdogs")
    print("Github : https://github.com/TheRealDalunacrobate\n\n\n")
banner()

# Get the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Victim name")
parser.add_argument('-ln','--lastname',help="Last name of victim")
parser.add_argument('-u','--update',help="Update DaProfiler")
parser.add_argument('-json','--json',help="Print result in json")
parser.add_argument('-zp','--zp',help="Zip code (Optional)")

args = parser.parse_args()

# Set the vars
name       = (args.lastname)
pren       = (args.name)
do_upgrade = (args.update)
json_print = (args.json)
zip_code   = (args.zp)

def randomString(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

thisIsATmpTokenListener = randomString(25);


# Def var
logging.speculos_lotus()
possible_usernames = []
folder_name = "{}_{}".format(pren,name)

personnal_life = []
social_medias  = []

# Crraeate the folder for the reports
try:
    os.mkdir('Reports')
except FileExistsError:
    pass
try:
    os.mkdir('Reports/{}'.format(folder_name))
except FileExistsError:
    pass

# Main
try:
    if pren and name is not None:
        bar = tqdm(desc="Searching over the world",total=12,leave=True)
        try:
            copainsdavant_results = copainsdavant_search.copains_davant(name=name,pren=pren)
        except:
            copainsdavant_results = None
        bar.update(1)
        bar.get_lock()

        try:
            facebook_results = facebook_search.facebook_search(name=name,pren=pren)
        except:
            facebook_results = None

        bar.update(1)

        try:
            twitter_results = twitter_search.twitter_search(name=name,pren=pren)
        except:
            twitter_results = None

        bar.update(1)

        try:
            official_linkedin_search_results = linkedin_search.official_linkedin_search(pren=pren,name=name)
        except:
            official_linkedin_search_results = None
        bar.update(1)
        try:
            avis_deces_results = death_records.death_search(name=name,pren=pren)
        except:
            avis_deces_results = None
        
        bar.update(1)
        try:
            bfmtv_results = dirigeants_bfmtv.bfmtv_search(name=name,pren=pren)
        except:
            bfmtv_results = None
        bar.update(1)


        try:
            instagram_results = instagram_search.ig_search(name=name,pren=pren)
        except:
            instagram_results = None
        bar.update(1)

        try:
            skype_results = skype_search.skype_searchh(name=name,pren=pren)
        except:
            skype_results = None

        bar.update(1)
        try:
            diplomess = last_diplomes.last_diplomes_brevet(name=name,pren=pren)
        except :
            diplomess = None

        bar.update(1)
        try:
            diplome_bac = last_diplomes.last_diplomes_bac(name=name,pren=pren)
        except:
            diplome_bac = None

        bar.update(1)
        try:
            if zip_code is not None:
                pagesblanche = pagesblanches_search.adresse_search(name=name,pren=pren,zipc=str(zip_code))
            else:
                pagesblanche = pagesblanches_search.adresse_search(name=name,pren=pren,zipc=None)
        except:
            pagesblanche = None

        bar.update(1)

        try:
            linkedin_results = linkedin_search.linkedin_search(name=name,pren=pren)
        except:
            linkedin_results = None

        bar.update(1)
        bar.close()
        possible_mail = mail_gen.check(name=name,pren=pren)
        skype2mail = mail_gen.skype2email(name=name,pren=pren)
        pin2mail = mail_gen.pinterest2email(name=name,pren=pren)
    elif len(pren) and len(name) == 0:
        linkedin_results = None
        facebook_results = None
        twitter_results = None
        avis_deces_results = None
        bfmtv_results = None
        instagram_results = None
        copainsdavant_results = None
        skype_results = None
        pagesblanche = None
        possible_mail = None
        skype2mail = None
        pren = ""
        name = ""
    else:
        linkedin_results = None
        facebook_results = None
        twitter_results = None
        avis_deces_results = None
        bfmtv_results = None
        instagram_results = None
        copainsdavant_results = None
        skype_results = None
        pagesblanche = None
        possible_mail = None
        skype2mail = None
        pren = ""
        name = ""
except TypeError:
    linkedin_results = None
    facebook_results = None
    twitter_results = None
    avis_deces_results = None
    bfmtv_results = None
    instagram_results = None
    copainsdavant_results = None
    skype_results = None
    pagesblanche = None
    possible_mail = None
    skype2mail = None
    pren = ""
    name = ""  

average_age = []


tree = Tree()
tree.create_node(f"{pren} {name}", 1)
data_export['Name'] = pren
data_export['LastName'] = name

try:
    diplome_bac = last_diplomes.last_diplomes_bac(name=name,pren=pren)
except:
    diplome_bac = None

# Daprofiler check les deces
if avis_deces_results is not None:
    tree.create_node("Death Records",41518181871541514778,parent=1)
    for i in avis_deces_results[:5]:
        tree.create_node('{} | {}\t| {}'.format(i['Age'],i['Name'],i['Loc'][1:]),parent=41518181871541514778)
    data_export['DeathRecords']['Exists'] = True
    data_export['DeathRecords']['Records'] = avis_deces_results[:5]
    try:
        average_age.append(int(i['Age']))
    except ValueError:
        pass

# Daprofiler check les linkedin
if linkedin_results is not None:
    tree.create_node('LinkedIN Profile',15418911611515145145,parent=1)
    tree.create_node(linkedin_results,parent=15418911611515145145)

# Daprofiler check les pages blanches
if official_linkedin_search_results is not None:
    job           = official_linkedin_search_results['Job']
    email         = official_linkedin_search_results['email']
    urnid         = official_linkedin_search_results['urnid']
    url           = official_linkedin_search_results['url']
    twitters      = official_linkedin_search_results['twitters']
    birthdate     = official_linkedin_search_results['birthdate']
    phone_numbers = official_linkedin_search_results['phone_numbers']

    tree.create_node('LinkedIN (Via API)',15458156411556562162,parent=1)
    tree.create_node(f'UrnID : {urnid}',5151515155,parent=15458156411556562162)
    tree.create_node(f'Url   : {url}',55185514542335,parent=15458156411556562162)
    if len(twitters) > 0:
        tree.create_node('Twitters',25848145481514,parent=15458156411556562162)
        for i in twitters:
            tree.create_node(i,parent=25848145481514)
    else:
        pass
    if len(phone_numbers) > 0:
        tree.create_node('Phone Numbers',28945181781,parent=15458156411556562162)
        for i in phone_numbers:
            tree.create_node(i,parent=28945181781)
    else:
        pass
    if job is not None:
        tree.create_node(f'Job : {job}',511515,parent=15458156411556562162)
    if birthdate is not None:
        tree.create_node(f'Birth Date : {birthdate}',5881981648,parent=1058151514851)
    if email is not None:
        tree.create_node(f'Email : {str(email)}',parent=15458156411556562162)
    data_export['LinkedIN']['Exist']        = True
    data_export['LinkedIN']['Job']          = job
    data_export['LinkedIN']['urnid'       ] = urnid
    data_export['LinkedIN']['Url']          = url
    data_export['LinkedIN']['Twitters']     = twitters
    data_export['LinkedIN']['Birthdate']    = birthdate
    data_export['LinkedIN']['PhoneNumbers'] = phone_numbers

if pagesblanche is not None:
    personnal_life.append('.')
    full_name = pagesblanche['Name']
    adress = pagesblanche['Adress']
    phone = pagesblanche['Phone']
    sure_status = pagesblanche['Not_Sure']
    
    data_export['AdressPhone']['Not_Sure'] = sure_status
    data_export['AdressPhone']['Exists'] = True    
    data_export['AdressPhone']['FullName'] = full_name
    data_export['AdressPhone']['Phone'] = phone
    data_export['AdressPhone']['Adress'] = adress
    if sure_status == True:
        tree.create_node("Adress - Phone",2,parent=1)
    else:
        tree.create_node("Adress - Phone (You must verify this information)",2,parent=1)
    tree.create_node("Full Name : {}".format(full_name),22,parent=2)
    tree.create_node("Adress    : {}".format(adress),33,parent=2)
    tree.create_node("Phone     : {}".format(phone),44,parent=2)
    if pagesblanche['carrier'] is not None:
        tree.create_node('Carrier : {}'.format(pagesblanche['carrier']),894,parent=44)
    if pagesblanche['Loc_phone'] is not None:
        tree.create_node('Localisation : {}'.format(pagesblanche['Loc_phone']),55,parent=44)
        data_export['AdressPhone']['PhoneLocation'] = pagesblanche['Loc_phone']
    if pagesblanche['Type_tel'] is not None:
        tree.create_node('Type  : {}'.format(pagesblanche['Type_tel']),66,parent=44)

if diplome_bac is not None:
    if diplome_bac['Exists'] == True:
        tree.create_node('DIPLOME BAC',58,parent=1)
        tree.create_node('Bac     : '+diplome_bac['Diplome'],848151541514,parent=58)
        tree.create_node('Academy : '+diplome_bac['academie'],848151241514,parent=58)
        tree.create_node('Mention : '+diplome_bac['mention'],848151341514,parent=58)
        tree.create_node('City    : '+diplome_bac['ville'],848151641514,parent=58)
        tree.create_node('Source  : '+diplome_bac['Link'],45994851726,parent=58)

        data_export['Diploma_Bac']['Exists']   = True
        data_export['Diploma_Bac']['Academie'] = diplome_bac['academie']
        data_export['Diploma_Bac']['Mention']  = diplome_bac['mention']
        data_export['Diploma_Bac']['City']     = diplome_bac['ville']
        data_export['Diploma_Bac']['Diplome']  = diplome_bac['Diplome']
        data_export['Diploma_Bac']['Link']     = diplome_bac['Link']  

# Daprofiler check les copains davant
if copainsdavant_results is not None:
    personnal_life.append('.')
    data_export['CopainsDavant']['Exists'] = True
    try:
        tree.create_node("Copains d'avant",3,parent=1)
        tree.create_node('Full Name    : {}'.format(copainsdavant_results['full_name']),77,parent=3)
        tree.create_node('Born Date    : {}'.format(copainsdavant_results['born']),88,parent=3)
        tree.create_node('Location : {}'.format(copainsdavant_results['localisation']),99,parent=3)
        tree.create_node('Url          : {}'.format(copainsdavant_results['url_full']),111,parent=3)
        
        data_export['CopainsDavant']['FullName']   = copainsdavant_results['full_name']
        data_export['CopainsDavant']['BornDate']   = copainsdavant_results['born']
        data_export['CopainsDavant']['ProfileUrl'] = copainsdavant_results['url_full'].replace('https://','')
        data_export['CopainsDavant']['Location']   = copainsdavant_results['localisation']
            
        if copainsdavant_results['Other_locations'] is not None:
            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
            tree.create_node('Other Locations',number_sk,parent=3)
            for i in copainsdavant_results['Other_locations']:
                if i != copainsdavant_results['localisation']:
                    tree.create_node(i,parent=number_sk)
            data_export['CopainsDavant']['OtherLocations'] = copainsdavant_results['Other_locations']
        if copainsdavant_results['pdp'] != "None":
            try:
                tree.create_node('Profile Picture : {}'.format(copainsdavant_results['pdp']),151515454545,parent=3)
                data_export['CopainsDavant']['ProfilePicUrl'] = copainsdavant_results['pdp'].replace('https://','')
            except:
                pass
        if copainsdavant_results['Job'] != "None":
            try:
                tree.create_node('Job : {}'.format(copainsdavant_results['Job']),154156132489411,parent=3)
                data_export['CopainsDavant']['Job'] = copainsdavant_results['Job']
            except:
                pass
        if copainsdavant_results['familial_situation'] != "None":
            try:
                tree.create_node('Familial Situation : {}'.format(copainsdavant_results['familial_situation'].strip()),44984154114515,parent=3)
                data_export['CopainsDavant']['FSituation'] = copainsdavant_results['familial_situation']
            except:
                pass
        if copainsdavant_results['nb_enfants'] != "None":
            try:
                tree.create_node('Number of kids : {}'.format(copainsdavant_results['nb_enfants']),1654518948741,parent=3)
                data_export['CopainsDavant']['NbKids'] = copainsdavant_results['nb_enfants']
            except:
                pass
    except TypeError:
        pass

# Daprofiler check BFMtv
if bfmtv_results is not None:
    personnal_life.append('.')
    data_export['Work']['Exists'] = True
    data_export['Work']['FullName'] = bfmtv_results['full_name']
    data_export['Work']['BornDate'] = bfmtv_results['naissance']
    data_export['Work']['Company']  = bfmtv_results['company']
    data_export['Work']['Function'] = bfmtv_results['fonction']
    data_export['Work']['Warrant']  = bfmtv_results['mandats']
    data_export['Work']['Link']     = bfmtv_results['link'].replace('https://','')
    data_export['Work']['Capital']  = bfmtv_results['Capital']
    data_export['Work']['Desc']     = bfmtv_results['Desc']

    tree.create_node("Work - Job",4,parent=1)
    tree.create_node('Full Name : {}'.format(bfmtv_results['full_name']),222,parent=4)
    tree.create_node('Born Date : {}'.format(bfmtv_results['naissance']),333,parent=4)
    tree.create_node('Adress    : {}'.format(bfmtv_results['addr']),888,parent=4)
    tree.create_node('Company   : {}'.format(bfmtv_results['company']),777,parent=4)
    tree.create_node('Desc      : {}'.format(bfmtv_results['Desc']),78285,parent=4)
    tree.create_node('Capital   : {}'.format(bfmtv_results['Capital']),84566,parent=4)
    tree.create_node('Link      : {}'.format(bfmtv_results['link']),666,parent=4)
    tree.create_node('Function  : {}'.format(bfmtv_results['fonction']),444,parent=4)
    tree.create_node('Warrant   : {}'.format(bfmtv_results['mandats']),555,parent=4)

# Daprofiler check twitter
if twitter_results is not None:
    social_medias.append('.')
    data_export['Twitter']['Exists'] = True
    data_export['Twitter']['Accounts'] = twitter_results
    tree.create_node('Twitters',665847555858,parent=1)
    for i in twitter_results:
        chars = "abcdefghijklmnopqrstuvwxyz1234567890"
        number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)        
        tree.create_node(i,number_sk,parent=665847555858)

# Daprofiler check skype
if skype_results is not None:
    social_medias.append('.')
    data_export['Skype']['Exists'] = True
    data_export['Skype']['AccountList'] = skype_results
    if len(skype_results) == 0:
        pass
    else:
        tree.create_node("Skype",6,parent=1)
        tree.create_node("Accounts : {}".format(str(len(skype_results))),12,parent=6)
        for i in skype_results:
            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            number_sk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
            tree.create_node(i,number_sk,parent=12)

# Diploma printing

if diplomess is not None:
    tree.create_node('BREVET DES COLLEGES',452,parent=1)
    tree.create_node('Name     : {}'.format(diplomess['Name']),1816864648,parent=452)
    tree.create_node('Diploma  : {}'.format(diplomess['Diplome']),45855887,parent=452)
    tree.create_node('Details  : {}'.format(diplomess['mention']),45855847,parent=452)
    tree.create_node('Academy  : {}'.format(diplomess['academie']),45855687,parent=452)
    tree.create_node('Location : {}'.format(diplomess['ville']),45855881,parent=452)
    tree.create_node('Source   : {}'.format(diplomess['Link']),45896472,parent=452)

    data_export['Diploma_Brevet']['Name']     = diplomess['Name']
    data_export['Diploma_Brevet']['Exists']   = True
    data_export['Diploma_Brevet']['Academie'] = diplomess['academie']
    data_export['Diploma_Brevet']['Mention']  = diplomess['mention']
    data_export['Diploma_Brevet']['City']     = diplomess['ville']
    data_export['Diploma_Brevet']['Link']     = diplomess['Link']
# Daprofiler check instagram

if instagram_results is not None:
    if len(instagram_results) ==  0:
        pass
    else:
        social_medias.append('.')
        data_export['Instagram']['Exists'] = True
        tree.create_node("Instagram",7,parent=1)
        tree.create_node('Accounts : {}'.format(str(len(instagram_results))),13,parent=7)
        acc_json_list = []
        for i in instagram_results:
            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            username = i
            number_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
            bio_infos = instagram_search.getInstagramEmailFromBio(username)
            tree.create_node(i,number_ski,parent=13)
            try: 
                data = instagram_search.get_extra_data(username)
                if data is None: 
                    ob_phone = False
                    ob_mail  = False
                    pass
                else:
                    if data != {}:
                        if data['obfuscated_email'] is not None:
                            ob_mail = data['obfuscated_email']
                            tree.create_node("Obfuscated Email -> "+ob_mail,parent=number_ski)
                        else:
                            ob_mail = False
                        if data['obfuscated_phone'] is not None:
                            ob_phone = data['obfuscated_phone']
                            tree.create_node("Obfuscated Phone -> "+ob_phone,parent=number_ski)
                        else:
                            ob_phone = False
                    else:
                        ob_phone = False
                        ob_mail  = False
            finally:
                pass

            acc_json_list.append({"Username":username,'obfuscated_phone':ob_phone,'obfuscated_email':ob_mail})

            bio_emails = bio_infos['emails']
            paypal_bio = bio_infos['paypal']
            city_loc   = bio_infos['city_list']
            is_lgbt    = bio_infos['lgbt_points']
            schoolname = bio_infos['school']
            bestfriend = bio_infos['best_friend']
            love_date  = bio_infos['love_date']
            age_bio    = bio_infos['age']
            ethnicity  = bio_infos['origins']
            facebook_l = bio_infos['fb_list']
            twitter_l  = bio_infos['twitter_list']
            hobbies    = bio_infos['Hobbies']
            love_situa = bio_infos['love_situation']
            religions  = bio_infos['religions']
            astrologys = bio_infos['astrology']
            if love_situa is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Love Situation',nnumber_ski,parent=number_ski)
                for i in love_situa:
                    tree.create_node(i,parent=nnumber_ski)
            if astrologys is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Astrologic sign',nnumber_ski,parent=number_ski)
                for i in astrologys:
                    tree.create_node(i,parent=nnumber_ski)
            if religions is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Religion(s)',nnumber_ski,parent=number_ski)
                for i in religions:
                    tree.create_node(i,parent=nnumber_ski)
            if hobbies is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Hobbies',nnumber_ski,parent=number_ski)
                for i in hobbies:
                    tree.create_node(i,parent=nnumber_ski)
            if bestfriend is not None:
                nnumber_ski = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                tree.create_node('Good relationship with',nnumber_ski,parent=number_ski)
                for i in bestfriend:
                    tree.create_node('{}'.format(i),parent=nnumber_ski)
            if is_lgbt is not None:
                lgbt_flag = (Fore.RED+"█"+Fore.YELLOW+"█"+Fore.GREEN+"█"+Fore.BLUE+"█"+Fore.MAGENTA+"█"+Fore.RESET)
                tree.create_node('{} LGBT Member'.format(lgbt_flag),parent=number_ski)
            if ethnicity is not None:
                tree.create_node('Ethnicity : {}'.format(str(ethnicity).replace('[','').replace(']','').replace("'","")),parent=number_ski)
            if facebook_l is not None:
                tree.create_node('Facebook : {}'.format(str(facebook_l).replace('[','').replace(']','').replace("'","")),parent=number_ski)
            if twitter_l is not None:
                tree.create('Twitter : {}'.format(str(twitter_l).replace('[','').replace(']','').replace("'","")),parent=number_ski)
            if schoolname is not None:
                tree.create_node('School Name : {}'.format(schoolname),parent=number_ski)
            if city_loc is not None:
                tree.create_node('City : {}'.format(city_loc[0]),parent=number_ski)
            if paypal_bio is not None:
                for i in paypal_bio:
                    tree.create_node('Paypal in bio -> '+i,parent=number_ski)
            if bio_emails is not None:
                for i in bio_emails:
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    number_skkk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                    number_skk = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                    tree.create_node('Email from bio -> '+Fore.CYAN+i+Fore.RESET,number_skkk,parent=number_ski)
        data_export['Instagram']['AccountList'] = acc_json_list

# Daprofiler check facebook
if facebook_results is not None:
    social_medias.append('.')
    data_export['Facebook']['Exists'] = True
    nb = str(len(facebook_results))
    tree.create_node("Facebook",9,parent=1)
    tree.create_node('Accounts : {}'.format(nb),10,parent=9)
    data_export['Facebook']['AccountList'] = facebook_results
    for i in facebook_results:
        tree.create_node(i,parent=10)

# Daprofiler generate Possible Email
if possible_mail is not None:
    if len(possible_mail) != 0 or len(skype2mail) != 0 or pin2mail is not None:
        tree.create_node('Emails extracted',146,parent=1)
        if skype2mail is not None:
            tree.create_node('[++] High probability',142,parent=146)
            no_doubles = []
            for i in skype2mail:
                if i not in no_doubles:
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    number = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                    no_doubles.append(i)
                    tree.create_node(i,number,parent=142)
                    # GETTING LEAKED PASSWORDS FROM SCYLLA.SH -> \modules\scylla_sh.py
                    scylla_results = scylla_sh.scylla_search(email=i)
                    if scylla_results is not None:
                        tree.create_node('Leaked From : Scylla.sh',1518451,parent=number)
                        for i in scylla_results:
                            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                            number = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                            tree.create_node('Leak Name : {}'.format(i['Name']),parent=1518451)
                            tree.create_node('Password  : {}'.format(i['Password']),parent=1518451)
                    # GET LEAKED PASSWORDS FROM LEAKCHET.NET API -> \api_modules\leakcheck_net.py
                    a = leakcheck_net.leak_check_api(mail=i)
                    if a is not None:
                        chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                        number_pass = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
                        tree.create_node("Leaked Creditentials",number_pass,parent=number)
                        for i in a:
                            password  = i['password']
                            leak_name = i['leak_name']
                            leak_date = i['leak_date']
                            tree.create_node('Password  : {}'.format(password),parent=number_pass)
                            tree.create_node('Leak Name : {}'.format(leak_name),parent=number_pass)
                            tree.create_node('Leak Date : {}'.format(leak_date),parent=number_pass)
            data_export['Emails']['HighProbEmails'] = no_doubles
        nb= str((len(possible_mail)))
        if pin2mail is not None:
            tree.create_node('[+++] Very high probability',45451451545545155154,parent=146)
            for i in pin2mail:
                tree.create_node('-> '+Fore.RED+i+Fore.RESET+" (Scraped from pinterest profile)",parent=45451451545545155154)
        if int(nb) != 0:
            tree.create_node("("+nb+") Possible Mailbox",8,parent=146)
            data_export['Emails']['PermutatedMailbox'] = possible_mail
            for i in possible_mail:
                tree.create_node(i,parent=8)

#banner()
if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')

# For data analyse
data_export['UI']['Pie']['PersonnalLife']   = len(personnal_life)
data_export['UI']['Pie']['SocialMedias']    = len(social_medias)
try:
    data_export['UI']['Bar']['TwitterFounds']   = len(twitter_results)
except TypeError:
    data_export['UI']['Bar']['TwitterFounds']   = 0
try:
    data_export['UI']['Bar']['InstagramFounds'] = len(instagram_results)
except TypeError:
    data_export['UI']['Bar']['InstagramFounds'] = 0
try:
    data_export['UI']['Bar']['FacebookFounds']  = len(facebook_results)
except TypeError:
    data_export['UI']['Bar']['FacebookFounds']  = 0
try:
    data_export['UI']['Bar']['SkypeFounds']     = len(skype_results)
except TypeError:
    data_export['UI']['Bar']['SkypeFounds']     = 0

if json_print == "true" or json_print == "yes" or json_print == "oui":
    print('-- JSON START --')
    print(data_export)
    print('-- JSON END --')
else:    
    tree.show()
    
data_file.close()
try:
    with open(f'Reports/{folder_name}/{name}_{pren}.json','w',encoding='utf8') as f:
        json.dump(data_export,f,indent=4,ensure_ascii=False)
        f.close()
except FileNotFoundError:
    os.mkdir('Reports')
    with open(f'Reports/{folder_name}/{name}_{pren}.json','w',encoding='utf8') as f:
        json.dump(data_export,f,indent=4,ensure_ascii=False)
        f.close()

try:
    if do_upgrade.lower() == "true":
        update_funct()
except:
    pass
