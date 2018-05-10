import random
import sys
import os
from pygame import mixer
import PyDB as db
import time

#Variable setup

oldname = db.get('name')

class bcolors:

    #text colors

    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    LIGHTBLUE = '\033[36m'
    ENDLINE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    print('[2] Music On or Off')
    print('[3] Credits(Working)')

    optioncontrol = input('')
    if optioncontrol == '1':
        print('^')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('V')
        print('<----------------------------------------------->')
        Exit = input('Hit enter to continue')

    if optioncontrol == '2':
        musicControl = db.get('musicControl')
        if musicControl == 'on':
            db.unset('musicControl')
            db.set('musicControl', 'off')
        else:
            db.unset('musicControl')
            db.set('musicControl', 'on')

    elif optioncontrol == '3':
        os.system('clear')
        print('Made by Lucien Hammond')
        print('I use PyDB which was created by Matthew Gallant on Github')
        print('I used some code to use colored text in the terminal which was taken from Jacob Mealys basegame')
        oof = input('Hit enter to continue')

    elif optioncontrol == 'test':
        os.system('clear')
        bars()
        Exit = input('Hit enter to continue')

def bars():

    health = int(db.get('health'))
    length = 10 - health
    print('[', end='')
    for i in range(health):
        print(bcolors.RED + '>' + bcolors.ENDLINE, end='')
    for e in range(length):
        print(' ', end='')
    print(']')

def music():
    # Note to self: Make menu music last for 20 minutes?
    musicControl = db.get('musicControl')
    if musicControl == 'on':
        music = 'Menu.wav'
        mixer.init()
        mixer.music.load(music)
        mixer.music.play()
    else:
        mixer.init()
        mixer.music.stop()
        pass

def fight():


Exit = 1
#Menu Loop
while True:
    
    music()
    
    oldname = db.get('name')
    oldclass = db.get('class')
    menu()
    print(oldname + ' ' + oldclass)
    menudeci = input('Enter decision here: ')
    if menudeci == '1':
        newgame(oldname)
    elif menudeci == '2':
        # Load game:
        
        print("Hello " + oldname + ". Welcome to your quest.")
        time.sleep(1)
        Exit = input('Hit enter to continue')
        xloc = db.get("xloc")
        yloc = db.get("yloc")
        print('Welcome mostly Matt and Jacob.')
        
        # Main Game loop

        while Exit != 0:

            xloc = int(xloc)
            yloc = int(yloc)

            #All Locations here
            if xloc == 4 and yloc == 20:
                print('You have arrived in a deep wooded grove, there is a deep fog surrounding the area')
                print('After scanning the area a bit, you see some homeless hippies smokin the weed')
                print('You walk up to them asking for to consume the weed')
                print('They ask: How much?')
                print('You say: I want a singular weed')
                print('Your life ends')
                decision = input('Hit enter to continue')
                xloc = xloc * 0
                yloc = yloc * 0
            elif xloc == 0 and yloc == 0:
                print('Welcome to the game!')



            
            decision = input('Command here: ')
            if decision == 'north' or decision == 'n':
                yloc = yloc + 1
            elif decision == 'south' or decision == 's':
                yloc = yloc - 1
            elif decision == 'east' or decision == 'e':
                xloc = xloc + 1
            elif decision == 'west' or decision == 'w':
                xloc = xloc - 1
            elif decision == 'exit':
                db.unset('xloc')
                db.unset('yloc')
                db.set('xloc', xloc)
                db.set('yloc', yloc)
                break
            elif decision == 'look':

                if xloc == 4 and yloc == 20:
                    print('You have arrived in a deep wooded grove, there is a deep fog surrounding the area')
                    print('After scanning the area a bit, you see some homeless hippies smokin the weed')
                    print('You walk up to them asking for to consume the weed')
                    print('They ask: How much?')
                    print('You say: I want a singular weed')
                    print('Your life ends')
                    decision = input('Hit enter to continue')
                    xloc = xloc * 0
                    yloc = yloc * 0

            else:
                print('Invalid command')
            os.system('clear')
            print('You moved ' + decision + '. Your current position is ' + str(xloc) + ", " + str(yloc))
            
                
    elif menudeci == '3':
        options()
    elif menudeci == '4':
        exit()


    
