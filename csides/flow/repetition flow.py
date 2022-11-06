"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂

░██████╗░███████╗███╗░░██╗███████╗░██████╗██╗░██████╗
██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝██║██╔════╝
██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░██║╚█████╗░
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗██║░╚═══██╗
╚██████╔╝███████╗██║░╚███║███████╗██████╔╝██║██████╔╝
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝╚═════╝░


█▀█ █▀▀ █▀█ █▀▀ ▀█▀ █ ▀█▀ █ █▀█ █▄░█   █▀▀ █░░ █▀█ █░█░█
█▀▄ ██▄ █▀▀ ██▄ ░█░ █ ░█░ █ █▄█ █░▀█   █▀░ █▄▄ █▄█ ▀▄▀▄▀.py


This programs lets the user choose how many times they would like to call the number set by users input
the program uses the various functions set out. The use of importing modules are used as well and is being 
used to choose when the program should end with the sys.exit() function call that calls to the sys module
its really amazing what you can do with string concatanation and converters like str() that converts anything you enter 
within it into the string data type! check out this seaside its short and simple but ultimately we are using for
loops and functions to make this porject breathe life into the program. Parameters are being implemented also
its being used within the print line on line 30 to insert the phone_number constant into its parenthesis () and the
use of  functions are used in lines 24/31 to store the data and source code to be used anywhere in the code later on
this helps to have to copy/paste code over and over again!


丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂 Ꮆ讠尺

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
"""

# define con()
def con():
    global phone_number
    # constants
    phone_number = str(3546453425)

import sys

def phone(num):
    call = input('How many times would you like to call? ')
    for ring in range(int(call)):
        print('called ' 
              + num 
              + ' (' 
              + str(ring) 
              + ') times!'
              )

"""
█▀▄ █▀▀ █▀▀   █▀ ▀█▀ ▄▀█ ▀█▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▄▀ ██▄ █▀░   ▄█ ░█░ █▀█ ░█░ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█

def statements create functions to use later in your programs to store source code so it can be reused later in your 
scripts and can be very useful for alot of things to declutter code and remove the problem of copy/paste novices
run into and can be used anywhere in code and these functions are excuted with function calls! 

follow the steps below to create a def statement

eg. def genesis():
        print('Hello genesis!')

what this indicates is that we created a function and we can now call those functions with the function call
genesis() while we can name our function calls basically anything its good practice to keep it short and simple for
cleaner code in the long run!
"""
# phone() is the function calling to the function phone(num)                    
phone(phone_number)

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠉⠉⠉⠉⠉⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⡇⠀⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠘⠋⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠿⢦⠤⠤⣤⠤⠤⡤⠤⢼⡧⠤⢼⠀⠀⠿⠤⡄⡠⠤⠴⠿⡇⠀⠀⠧⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢸⠀⠀⣿⠀⠀⡇⠀⢸⡇⠀⢸⠀⠀⠀⠀⡏⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠿⢿⠀⠀⠿⠀⠀⠇⠀⢸⡇⠀⢸⠀⠀⠿⠿⡇⠀⠸⠿⠿⡇⠀⠀⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⢸⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⢸⣄⠀⠀⠀⣧⡀⠀⠀⠀⡇⠀⠀⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢿⣿⣿⡿⢿⣿⣿⣿⢿⣿⡿⢿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀

 
Thank you for downloading this .py find more sea sides at my githu and learn something new everyday and rememeber
to not give up on coding! its an artform and anbody can be skileld enough to achieve greatness in your code
make sure to check out my twitch streams below!

Twitch: https://www.twitch.tv/tenniswaifu 
Github: https://github.com/tenniswaifu

thank you to everyone on twitch who participated in the making of this .py!
"""