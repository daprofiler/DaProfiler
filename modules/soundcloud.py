from selenium import webdriver
from colorama import Fore

def webdriver_usage(name,pren):
    print("🎧 Searching for soundcloud profiles ...")
    try:
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(f"https://soundcloud.com/search/people?q={pren} {name}")
        source_code = str(driver.page_source)
        if "Check the spelling, or try a different search." in source_code:
            print(f'   -> {Fore.RED}No soundcloud profile matching ! {Fore.RESET}')
        else:
            print(f'   -> {Fore.GREEN}Found !{Fore.RESET} Visit : https://soundcloud.com/search/people?q={pren}%20{name}')        
    except KeyboardInterrupt:
        return
