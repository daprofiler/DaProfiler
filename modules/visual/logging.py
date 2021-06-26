from datetime import datetime
import time

def terminal_loggin(log,text):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    text = (current_time, text)
    try:
        if log.lower() == "true":
            print ("\033[A                             \033[A")
            for i in text: 
                print(i, end ='\r')
                time.sleep(0.01)
    except:
        pass
