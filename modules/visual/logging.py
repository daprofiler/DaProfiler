def speculos_lotus():
    try:
        with open("modules/mail_domain.txt","r") as file:
            lines = file.readlines()
            file.close()
        print("""
* NOTE *: 
    + You can update DaProfiler using : py profiler.py -u True
    
    + You can add by yourself some others mail domains (ex @mail.mail) 
    to search for target emails using that domain.
        HOW :
        . Go to /modules
        . Add your domains ({} Detected) 
        """.format(str(len(lines))))
    except:
        pass
