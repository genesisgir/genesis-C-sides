""" 
█▀▀ █▀▀ █▄░█ █▀▀ █▀ █ █▀   █░░ █▀▀ █▀ █▀ █▀█ █▄░█ █▀   █░█ █▀█ █░░ ░ ▄█
█▄█ ██▄ █░▀█ ██▄ ▄█ █ ▄█   █▄▄ ██▄ ▄█ ▄█ █▄█ █░▀█ ▄█   ▀▄▀ █▄█ █▄▄ ▄ ░█ 
Welcome to the genesis gir lesson tutorials Volume 1! Robotic Syndrome takes the user to a room with a manic robot 
that makes them guess they right number 10 times if not user will end up perishing from the gigantic lazer that the robot
has in store for them! Guess the right number to survive if you guessed wrong you will know and find yourself out the
room filled with mechanical parts from the future met for your demiseThanks for downloading~ 
⼕ㄖᗪ🝗ᗪ & 山尺讠セセ🝗𝓝 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂 Ꮆ讠尺
"""
# This program takes the user on a hostage situation with a robot that has user trapped in a room met for death!

#Modules
import sys

# Character variable/constants
robo = 'Machine TM97:'

print()
print('-Your in a white room and something opens the door slowly -')
print()
print(f'{robo}Wake up! BUZZ Brrr')
print('(press enter to wake up)')
input()
print('-The robotic dictator splashes water against your face and you see a tall mechanical strong humanoid-')
print('(press enter)')
input()
print(f'{robo} Whats the number Im thinking of? Guess its between 1-10')
print()
print('-The robot leans over the table clenching his fists in such a anger manner and the oil dripping out of his eyes')
print('its clear that your in trouble and need to give the robot his desired answer or who knows what it will..do to you')
print('(guess a number between 1 and 10)')

guess = input()

if guess =='6': # answer to the manic robot is '6'
    print(f'{robo} Yes. .Yes BRRr')
    print('(press enter)')
    input()
    print(f'{robo} The number was 6. . Lets play again?')
    response = input('(y/n?)')
    
    if response == 'y': # answer to the manic robot is 'y'
        print(f'{robo} Great lets play again shall we')
        print('(press enter to play again)')
        input()
        print(f'{robo} I wan-ntt you to guess the number inside my data mainframe between 1-10')
        print()
        print('-The robots voice gets deeper and less angry but you can tell the voice has calmed-')
        print('(guess a number between 1 and 10)')
        
        guess = input()
        
        if guess == '8': # answer to the manic robot is '8'
            print(f'{robo} Did not know humans were smart. yes correct!')
            print('(press enter)')
            input()
            print(f'{robo} Lets play the game again cause your brain intrigues me.')
            print('(press enter to play the game again)')
            input()
            print('-You sit and think to yourself how unjustified and creepy this game is-')
            print('(press enter)')
            input()
            print(f'{robo} Okay! BRRrrrr Buuzzzz')
            print('(press enter to stare)')
            input()
            print(f'{robo} What number am I thinking between 1-6?')
            print('(guess a number between 1-6 than press enter)')
            
            guess = input()
            
            if guess == '2': # answer to the manic robot is '2'
                print(f'{robo} Yes yes! it was 2! Brrr Buzz')
                print('(press enter)')
                input()
                print('-As the blood flows faster and faster the strong feeling that this robot might want to kill you as')
                print('you notice the humanoid is holding a huge knife that can contract with their robotic parts and suit-')
                print('(press enter)')
                input()
                print(f'{robo} Lets play one more time this one will be hard! Guess the number Im thinking of its between')
                print('1-15')
                print('(press enter)')
                input()
                print('-He bumped up the odds to my life. . -')
                print('(press enter)')
                input()
                print('(guess a number between 1-15 than press enter)')
                
                guess = input()
                
                if guess == '11': # answer to the manic robot is '11'
                    print(f'{robo} 11 was the right answer! you...')
                    print('(press enter)')
                    input()
                    print(f'{robo} win! you may leave this room.')
                    print('(press enter to exit the room safe and sound)')
                    input()
                    print('(YOU WIN!)')
                    sys.exit()
                else:
                    print(f'{robo} You will die and it was your last chance too..')
                    print('(press enter to brace yourself for death)')
                    input()
                    print('-Stabby Stab Stab -')
                    print('(GAME OVER)')
                    sys.exit()
                    
                
                
                
                
            else:
                print('-The robot gets up and starts to choke you to death!-')
                print('(GAME OVER)')
                sys.exit()
            
            
            
        else:
            print('-The robot stands up-')
            print('(press enter)')
            input()
            print('-You have been stabbed and are bleeding to your death-')
            print('(GAME OVER)')
            sys.exit()
        
        
        
    elif response == 'n':
        print('-The robot picks you up and rips you to shreds..you bleed out-')
        print('(GAME OVER)')
        sys.exit()
else:
    print('-The robot starts to tear you to shreds and you die in a pool of your own blood-')
    print('(GAME OVER)')
    sys.exit()
    



