import random
import sys
import os
from pygame import mixer
import PyDB as db
import time

#Variable setup
oldname = db.get('name')

#Menu screen

def menu():
    os.system('clear')
    print('        _.-"\ ')
    print('    _.-"     \ ')
    print(' ,-"          \ ')
    print('( \            \ ')
    print(' \ \            \ ')
    print('  \ \            \ ')
    print('   \ \         _.-;')
    print('    \ \    _.-"   :')
    print('     \ \,-"    _.-"')
    print('      \(   _.-"  ')
    print('       `--"')
    print('')
    print('[1] Start New Game')
    print('[2] Load Game')
    print('[3] Options')
    print('[4] Exit')

#Making a new game

def newgame(oldname):
    os.system('clear')
    print('        _.-"\ ')
    print('    _.-"     \ ')
    print(' ,-"          \ ')
    print('( \            \ ')
    print(' \ \            \ ')
    print('  \ \            \ ')
    print('   \ \         _.-;')
    print('    \ \    _.-"   :')
    print('     \ \,-"    _.-"')
    print('      \(   _.-"  ')
    print('       `--"')
    print('')
    failsafe = input("This will delete your current file: " + oldname + ". Are you sure? Y or N: ")
    if failsafe == 'Y':
        name = input('What is your name?: ')
        db.unset("name")
        db.set("name", name)
        print("Your name is: " + name)
        passe = input('Hit enter to continue')
        
        os.system('clear')
        print('      _____   ')
        print('     /     \ ')
        print('    ( @  @  ) ')
        print('    |  ___  | ')
        print('     |     | ')
        print('   ==       ==')
        print('  |           | ')
        print('  |  |     |  | ')
        print('  |  |     |  | ')
        print('This is ' + name)
        print('Pick your class: ')
        print('[1] Warrior')
        print('[2] Cleric')
        print('[3] Sorcerer')
        print('[4] Rouge')
        print('[5] Ranger')
        playerclass = input('')
        if playerclass == '1':
            confirm = input('Your name is ' + name + ' and your class is Warrior is this correct? Y or N: ')
            db.unset("class")
            db.set("class", "Warrior")
            return name
            pass
            
        if playerclass == '2':
            confirm = input('Your name is ' + name + ' and your class is Cleric is this correct? Y or N: ')
            db.unset("class")
            db.set("class", "Cleric")
            return name
            pass
        if playerclass == '3':
            confirm = input('Your name is ' + name + ' and your class is Sorcerer is this correct? Y or N: ')
            db.unset("class")
            db.set("class", "Sorcerer")
            return name
            pass
        if playerclass == '4':
            confirm = input('Your name is ' + name + ' and your class is Rouge is this correct? Y or N: ')
            db.unset("class")
            db.set("class", "Rouge")
            return name
            pass
        if playerclass == '5':
            db.unset("class")
            db.set("class", "Ranger")
            confirm = input('Your name is ' + name + ' and your class is Ranger is this correct? Y or N: ')
            return name
            pass
    else:
        pass
    
    
    
'''
get location
get name
get class
get inventory
get Entitys and heakth
get health and other de/buffs
get armor
get ability scores

'''
def options():
    os.system('clear')
    print('   _   _')
    print('  ( \_/ )')
    print(' __)o_o(__')
    print('(__o(_)o__)')
    print('   )o_o(')
    print('  (_/ \_)')
    print(' ')
    print('[1] Make sure terminal is resized correctlly(Not working)')
    print('[2] Music On or Off(Not working)')
    print('[3] Credits(Working)')
    optioncontrol = input('')
    if optioncontrol == '3':
        os.system('clear')
        print('Made by Lucien Hammond')
        print('I use PyDB which was created by Matthew Gallant on Github')
        oof = input('Hit enter to continue')

    


Exit = 1
#Menu Loop
while True:
    # Note to self: Make menu music last for 20 minutes?
    file = 'Menu.wav'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    oldname = db.get('name')
    oldclass = db.get('class')
    menu()
    print(oldname + ' ' + oldclass)
    menudeci = input('Enter decision here: ')
    if menudeci == '1':
        newgame(oldname)
    elif menudeci == '2':
        # Load game:
        print("Its not ready yet")
        time.sleep(3)
        print('Get out of here Matt')
        time.sleep(5)
        Exit = input('Hit enter to continue')
        xloc = db.get("xloc")
        yloc = db.get("yloc")
        print('Welcome mostly Matt and Jacob.')
        
        # Main Game loop
        while Exit != 0:
            
            xloc = int(xloc)
            yloc = int(yloc)
            decision = input('Command here: ')
            if decision == 'north':
                yloc = yloc + 1
            elif decision == 'south':
                yloc = yloc - 1
            elif decision == 'east':
                xloc = xloc + 1
            elif decision == 'west':
                xloc = xloc - 1
            elif decision == 'exit':
                break
            else:
                print('Invalid command')
            print('You moved ' + decision + '. Your current position is ' + str(xloc) + ", " + str(yloc))
                
    elif menudeci == '3':
        options()
    elif menudeci == '4':
        exit()


    
