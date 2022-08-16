import sys, time
from random import random
from math import ceil

def slow_type(t):
    typing_speed = 100 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random()*10.0/typing_speed)
Loot = 0
Health = 10
Monster = False
TotalLoot = 0
PlayerDamadge = 0
WeaponPower = 10
print( '______                                     ______                               __   _____  ' )
print( '|  _  \                                    | ___ \                             /  | |  _  | ' )
print( '| | | |_   _ _ __   __ _  ___  ___  _ __   | |_/ /___   __ _ _ __ ___   __   __`| | | |/| | ' )
print( '| | | | | | |  _ \ / _` |/ _ \/ _ \|  _ \  |    // _ \ / _` |  _ ` _ \  \ \ / / | | |  /| | ' )
print( '| |/ /| |_| | | | | (_| |  __/ (_) | | | | | |\ \ (_) | (_| | | | | | |  \ V / _| |_\ |_/ / ' )
print( '|___/  \__,_|_| |_|\__, |\___|\___/|_| |_| \_| \_\___/ \__,_|_| |_| |_|   \_/  \___(_)___/  ' )
print( '                    __/ |                                                                   ' )
print( '                   |___/                                                                    \n' )
slow_type('A Generic Dungeon Game By Natelolzzz\n' )
slow_type( 'Type "Help" For Help\n' )
    
while True:
    Command = input('> ' )
    if Command == 'Help' :
        slow_type( 'Welcome To The Help Menu!\n' )
        slow_type( 'Here Are Commands The Game Uses:\n' )
        slow_type( '"Restore Health"\n' )
        slow_type( '"To The Next Room!"\n' )
        slow_type( '"Fight"\n' )
        slow_type( '"Show Stats"\n' )
        slow_type( 'If This Is Your First Time, Use "To The Next Room!"\n' )
    
    if Command == 'To The Next Room!' and Monster == True:
        slow_type('You Cant Leave, Theres A Monster!\n' )
    
    if Command == 'To The Next Room!' and Monster != True:
        Walls = ceil(random()*10)
        if Walls == 1 :
            slow_type('The Walls Are Stone\n' )
        if Walls == 2 :
            slow_type('The Walls Are Dirt\n' )
        if Walls == 3 :
            slow_type('The Walls Are Wood\n' )
        if Walls == 4 :
            slow_type('The Walls Are Too Mossy To See\n' )
        if Walls == 5 :
            slow_type('The Walls are Stone, Held Up By Beams\n' )
        if Walls == 6 :
            slow_type('The Walls Are Dirt, Held Up By Beams\n' )
        if Walls == 7 :
            slow_type('The Walls Are Wood, Held Up By Beams\n' )
        if Walls == 8 :
            slow_type('The Walls Are Too Mossy To See But Are Held Up With Beams\n' )
        if Walls == 9 or Walls == 10:
            slow_type('You Arent Paying Attention To The Walls\n' )
        
        MonsterChance = ceil(random()*10)
        Monster = True
        if MonsterChance == 1 or MonsterChance == 2 :
            slow_type('The Monster Is A Skeleton!\n' )
            MonsterHP = 0.1 * WeaponPower
        if MonsterChance == 3 or MonsterChance == 4 :
            slow_type('The Monster Is A Mimic!\n' )
            MonsterHP = 0.4 * WeaponPower
        if MonsterChance == 5 or MonsterChance == 6:
            slow_type('The Monster Is A Dragon!\n' )
            MonsterHP = 1 * WeaponPower
        if MonsterChance == 7 or MonsterChance == 8 :
            slow_type('The Monster Is A Knight\n' )
            MonsterHP = 0.6 * WeaponPower
        if MonsterChance == 9 or MonsterChance == 10:
            slow_type('The Monster Is A Zombie\n' )
            MonsterHP = 0.2 * WeaponPower
        slow_type('Use the "Fight" command')
      
    if Command == 'Fight' and Monster == True :
        if ceil(random()*10) >= 5:
            PlayerDamadge = ceil(random()*WeaponPower)
            print('Do',PlayerDamadge, 'Damage\n' )
            MonsterHP = MonsterHP - PlayerDamadge
            if MonsterHP < 1:
                Monster = False
                slow_type('You Killed It!\n' )
                Loot = ceil(random()*10)
                print('Gain ',Loot,' coins!\n' )
                TotalLoot = TotalLoot + Loot
        else :
            slow_type('You Miss\n' )
        
    if Command == 'Fight' and Monster == True :
        Damage = ceil(random()*4)
        slow_type('The Monster Attacks!\n' )
        print('You Take',Damage, 'Damage\n' )
        Health = Health - Damage
        if Health <= 0:
            break
    
    if Command == 'Show Stats' :
        print('Health is',Health)
        print('All Your Loot Is',Loot)
        if Monster == True :
            print('The Monsters Health is',MonsterHP)
    
    if Command == 'Restore Health' :
        slow_type('Health Up!\n' )
        Health = Health + ceil(random()*10)
        print('Health Is Now:', Health)

slow_type('Game Over!\n' )
