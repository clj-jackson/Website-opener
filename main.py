import webbrowser
import time
import subprocess
import os

url_save = {"DND": ["www.google.com/search?q=d20&rlz=1C1AVFC_enGB845GB846&oq=d20&aqs=chrome..69i57j0i433j0l6j46i175i199j0.2615j0j7&sourceid=chrome&ie=UTF-8", "https://www.dndbeyond.com/", "https://media.wizards.com/2014/downloads/dnd/MM_MonstersCR.pdf", "www.google.com"],
            "SCHOOL": ["brightoncollege.fireflycloud.net/dashboard",
                       "brightoncollege.fireflycloud.net/set-tasks", "outlook.office.com/mail/inbox",
                       "www.onenote.com/notebooks?auth=2&nf=1", "www.replit.com",
                       "my.classoos.com/uk/books/textbooks", "www.google.com"],
            "FUN": ["www.youtube.com", "www.twitch.com", "www.netflix.com", "www.crunchyroll.com", "www.google.com"],
            "CODING": ["www.replit.com", "www.stackoverflow.com", "www.youtube.com", "www.google.com"]}

webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

save_name = input("Which save would you like to access?\n\nInput:\t").upper()


def opentab():
    for i in range(len(url_save[save_name])):
        webbrowser.get('chrome').open_new(url_save[save_name][i])
        time.sleep(0.5)
        
opentab()

print("\n\nTABS HAVE BEEN OPENED, ENJOY...\n\n")
