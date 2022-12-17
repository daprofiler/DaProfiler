from selenium import webdriver
from colorama import Fore
import time

def webdriver_usage(name,pren):
    print("🎧 Searching for soundcloud profiles ...")
    try:
        try:
            options = webdriver.FirefoxOptions()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            driver.get(f"https://soundcloud.com/search/people?q={pren} {name}")
            time.sleep(4.0)
            source_code = str(driver.page_source)
            if "Check the spelling, or try a different search." in source_code or "Sorry we didn't find any results for" in source_code:
                pass
            else:
                print(f'   -> {Fore.GREEN}Found !{Fore.RESET} Visit : https://soundcloud.com/search/people?q={pren}%20{name}')    
        except:
            return None    
    except KeyboardInterrupt:
        return
