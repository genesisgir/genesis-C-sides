"""
░██████╗░███████╗███╗░░██╗███████╗░██████╗██╗░██████╗░██████╗░██╗██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝██║██╔════╝██╔════╝░██║██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░██║╚█████╗░██║░░██╗░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗██║░╚═══██╗██║░░╚██╗██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██████╔╝██║██████╔╝╚██████╔╝██║██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝╚═════╝░░╚═════╝░╚═╝╚═╝░░╚═╝


█░░ ▄▀█ ▀▄▀ █▀▀ █ ▀█▀ █▄█
█▄▄ █▀█ █░█ █▄▄ █ ░█░ ░█░

Heres a program i created using the webbrowser function and uses the function call to open up a web page using modules!
the art of coding can be really fun and amazing when things come together, I put the url of my favorite laxcity track by far
GRANTED by Laxcity make sure to follow him on soundcloud!

Laxcity: https://soundcloud.com/laxcity (B-SIDES) / https://soundcloud.com/laxcitymusic (MAIN)

║░█░█░║░█░█░█░║░█░█░║
║░█░█░║░█░█░█░║░█░█░║
║░║░║░║░║░║░║░║░║░║░║
╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝
            Tips: The webbrowser module allows you to open web pages using webbrowser('insert URL')
Program created by tenniswaifu
"""
#Importing modules with the import statement
import webbrowser,time,sys,random

# genesis gir constant
genesis = 'Genesis:'

#creating the function call laxcity with the def statement!
def laxcity(songname):
    print(genesis + 'Here is a song I really like from laxcity!')
    time.sleep(2)
    print(genesis + 'You will be directed to soundcloud!')
    time.sleep(2)
    print('Loading webbrowser...')
    time.sleep(2)
    print('getting things together')
    time.sleep(2)
    print('Enjoy!')
    time.sleep(1)
    webbrowser.open('https://soundcloud.com/laxcity/granted')
    print(songname + ' started playing!')
    
laxcity('Laxcity - GRANTED')


sys.exit()