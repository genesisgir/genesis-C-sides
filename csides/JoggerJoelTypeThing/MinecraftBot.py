""" 
█▀▀ █▀▀ █▄░█ █▀▀ █▀ █ █▀   █░░ █▀▀ █▀ █▀ █▀█ █▄░█ █▀   █░█ █▀█ █░░ ░ ▄█
█▄█ ██▄ █░▀█ ██▄ ▄█ █ ▄█   █▄▄ ██▄ ▄█ ▄█ █▄█ █░▀█ ▄█   ▀▄▀ █▄█ █▄▄ ▄ ░█ 
Welcome to the genesis gir lesson tutorials Volume 1! This program takes the user into a  minecrafft world heavy inspiration
by joggerJoel with his immense interactive minecraft bots we will be taking user threw minecraft scenarios to dig , build,
and do a wide range of tasks that a minecraft would do! just with the less functions..but creativity is what counts so jump
into this diverse world and start collecting items and building your home and finish the program! This program is not an
actual bot but used for inspiration to create more vast programs and to get practice in when I can since this is a c side
Thanks for downloading~ 
⼕ㄖᗪ🝗ᗪ & 山尺讠セセ🝗𝓝 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂 Ꮆ讠尺
"""

#Modules
import sys # A  module that terminates program early
import time # using for the loaidng screen
import random # generates random number integers fun right?!

# enemies (foes that you can kill within this program)
creep = 'Creeper (Enemy)'
zombie = 'Zombie (Enemy)'

# enemies kill counters (Kill Track)
creep_killcount = 0
zombie_killcount = 0


# weapons
wood_sword = 'Wood Sword (Weapon)'
iron_sword = 'Iron Sword (Weapon)'
silver_sword = 'Silver Sword (Weapon)'
gold_sword = 'Gold Sword (Weapon)'
diamond_sword = 'Diamond Sword (Weapon)'

# weapon amounts
wood_sword_amount = 0
iron_sword_amount = 0
silver_sword_amount = 0
gold_sword_amount = 0
diamond_sword_amount = 0 

#  items
work_bench = 'Work Bench (Crafting)'

# items amounts
work_bench_amount = 0

# blocks
wood_block = 'Wood block (Material)'# block can be picked up
stone_block = 'Stone block  (Material)'# block can be picked up
coal_block = 'Coal block (Material)' # only farmable
dirt_block = 'Dirt block (Material)'# block can be picked up
redstone_block = 'Redstone block (Material)' # only farmable
diamond_block = 'Diamond block (Material)' # only farmable
water_block = 'Water block (Material)'# block can be picked up
lava_block = 'Lava block (Material)' # block can be picked up
iron_block = 'Iron block (Material)' # only farmable
silver_block = 'Silver block (Material)' # only farmable
obsidian_block = 'Obsidian block (Material)'# block can be picked up
lapis_lazuli_block = 'Lapis Lazuli block (Material)' # only farmable
gold_block = 'Gold block (Material)' # only farmable

# block amounts (The blocks that can be picked up are shown here)
wood_block_amount = 0
stone_block_amount = 0
dirt_block_amount = 0
water_block_amount = 0
obsidian_block_amount = 0
lava_block_amount = 0

# ores (ores that been farmed from blocks are shown here)
iron_ore = 'Iron (Ore)'
silver_ore = 'Silver (Ore)'
gold_ore = 'gold (Ore)'
diamond_ore = 'Diamond (Ore)'
redstone_ore = 'Redstone (Ore)'
lapis_lazuli_ore = 'Lapis Lazuli (ore)'

# ore amounts ( the amounts for the ores collceted as shown here)
iron_ore_amount = 0
silver_ore_amount = 0
gold_ore_amount = 0
diamond_ore_amount = 0
redstone_ore_amount = 0
lapis_lazuli_ore_amount = 0

# This program takes user into a minecraft world called Gen
print()
print()
print('Welcome to Minecraft! v1.0.5')
print()
print('This program was inspired by JoggerJoel!')
print()
print('>Create new world [c]')
print('>exit game [x]')
resp = input()
if resp == 'c':
    print('(create world name)')
    world_name = input()
    
    # loading screen for world! 
    print(world_name+' is being generated. .')
    time.sleep(1)
    print('Building the terrain for '+world_name+'!. .')
    time.sleep(5)
    print('Building the mountains for '+world_name+'. . ')
    time.sleep(1)
    print('Letting the water settle in. . ')
    time.sleep(2)
    print('Clouds being generated. . ')
    time.sleep(1)
    print(world_name+' ores being grounded. . ')
    time.sleep(5)
    print('Enemies being generated in caves. . ')
    time.sleep(5)
    print('Biomes being generated. . ')
    time.sleep(1)
    print('Ravines being implemented. . .')
    time.sleep(6)
    print('Chunky blocks being scanned. .')
    time.sleep(4)
    print(world_name+' has been created!. .')
    print()
    print('Your world has been created!')
    
    # asking user if they want to play world (infinite loop only breaks if yes is selected)
    while True:
        print('(play '+world_name+' y/n?)')    
        response = input()
        if response == 'y':
            break
        elif response == 'n':
            print('You must play the world press y next time!')
            continue
        else:
            print('You must play your world Try again')
            continue
    
    # character creation
    print('Notification: Before you can play your world you must make your username!')
    
    # creating username
    user = input('>create username than press enter! ')
    print()
    print('Notification: username has been created!')
    print('(press enter)')
    input()
    print('Notification:Your username is now '+user+'!')
    print('(press enter to play!)')
    input()
    
    # program loading
    print('Minecraft is loading. . ')
    time.sleep(10)
    print('Minecraft is loading the blocks. .')
    time.sleep(1)
    print('inserting the waterfalls. . ')
    time.sleep(5)
    print('creating the fluffy wolves. .')
    time.sleep(3)
    print('Creepers being laced with TNT. . ')
    time.sleep(1)
    print('Diamond ore being stashed. . ')
    time.sleep(1)
    print('Entering '+world_name+'!')
    
    print(user+' has been generated!')
    print('-You find yourself standing near the sand biome-')
    time.sleep(2)
    print('(press enter)')
    input()
    print('Welcome to minecraft '+user+' start off by cutting some trees down for '+wood_block)
    print('(press enter)')
    input()
    print('-You run out of the sand biome and see a tall tree!-')
    print('(press enter)')
    input()
    
    # cutting tree down process
    while wood_block_amount != 20:
        print('(Punch the tree down to collect wood)')
        print('(press enter to punch)')
        input()
        wood_block_amount = wood_block_amount + 5
        print('The tree falls down and you collected 5 wood!')
        print()
    print('('+user+' collected 20 wood'+')')
    print('(press enter to read tutorial info)')
    input()
    print('Notification: Great you collected enough wood to craft a work bench! with work benches you are able')
    print('to craft items with the resources you have to kill enemies! Lets craft a work bench.')
    print('(press enter)')
    input()
    
    # crafting work bench
    while True:
        resp = input('(Craft a work bench y/n?) ')
        if resp == 'y':
            print('Notification:Work bench has been created!')
            wood_block_amount = wood_block_amount - 10
            work_bench_amount = work_bench_amount + 1
            time.sleep(1)
            print('You have '+'('+str(wood_block_amount)+') '+wood_block+' left in your inventory')
            print('(press enter)')
            input()
            break
            
        elif resp == 'n':
            print('Notification: your going to need a work bench to craft things!')
            time.sleep(5)
            print('(okay and press enter)')
            input()
            continue
    
    # program continues
    print('Notification:Nice '+user+' you have crafted a '+work_bench+'!')
    print('(press enter)')
    input()
    print('Notification: place your '+work_bench+' down to get started!')
    time.sleep(1)
    print('(press enter)')
    input()
    print('-You walk under a shallow tree and decide to place the work bench down and as you start to build and craft')
    print('the beautiful sun is gazing down at you..The moon is closing in and the cool midnight air is hitting your skin')
    print('the feeling of being enveloped by the world '+world_name+' is exhilerating yet calm.-')
    time.sleep(5)
    print('You finally finish the work bench and the wood is glossy and a soft tampered cloth quilted lay over it-')
    print('(press enter)')
    input()
    print('Notification: Great you have crafted the most common item in the game but did you know..')
    time.sleep(2)
    print('Notification: That with this work bench you can craft other items as well? lets give it a try')
    print('(press enter)')
    input()
    print('Notification: Enemy like the '+creep+' will try to halt you in your tracks')
    print('maybe crafting a '+wood_sword+' would be choice!')
    time.sleep(1)
    print('Notification: Your going to need some more wood you only have '+'('+str(wood_block_amount)+') currently')
    print('(press enter to start looking for wood)')
    input()
    print(user+' begins to run around!')
    time.sleep(1)
    print('-punching into the air while they look for a tree. . -')
    time.sleep(1)
    print('-You find the perfect Tree in all of its glory-')
    print('(press enter)')
    input()
    
    # cutting tree down process
    while wood_block_amount != 20:
        print('(Punch the tree down to collect wood)')
        print('(press enter to punch)')
        input()
        broken_wood = str(random.randint(4,11))
        wood_block_amount = wood_block_amount + broken_wood 
        print('The tree falls down and you collected '+broken_wood+' wood!')
        print()
    print('('+user+' collected 20+ wood'+')')
    print('(press enter to read tutorial info)')
    input()
    print('Notification: Nice you have collected enough to make a '+wood_sword+'!')
    print('(press enter)')
    input()    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
        
    
    
elif resp == 'x': # if user decides to not play minecraft do this
    print('Thank you for trying out the program JoggerJoel will thank you!')
    print('(shutting down Minecraft. . .)')
    sys.exit()
    