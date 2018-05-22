# game.py - AmEn1 demo

import sys, os, textwrap, random, time, ast
import msvcrt as getch
from random import randint
import faces, maps


############################
##   TOOLS/MENUS/STATES   ##
############################

def cls():
    os.system('CLS')


class states():
    lvlState = 0
    pl_hp = 30
    gold = 200
    spellList = {'Healing':1, 'Fireball':2, 'ThunderStrike':1}
    shop_items = {'Sword dam +1':15, 'Minor Amulet':30, 'Magicka +1':10}
    magicka = 18
    swordDam = 2

    companion = ''
    comp_abList = {}
    comp_char = ' '
    
    currentEnemy= ''
    enemyHp = 0
    enemyBaseDam = 0

    #map 1 states

    #map 2 states
    womanTalkedTo = 0
    womanQuest = '!'
    
    #map 3 states
    snakeDef = 0
    tank_char = 'T'

    # map 4 states
    kingDef = 0
    
    #map house states
    anne_char = 'A'
    wizard_char = 'W'


def returnMap():
    if states.lvlState == 0:
        return mapOne()
    elif states.lvlState == 1:
        return mapTwo()
    elif states.lvlState == 2:
        return mapThree()
    elif states.lvlState == 3:
        return houseMap()
    elif states.lvlState == 4:
        return mapFour()


def menu():
    cls()
    print('\n'+'       -MENU-')
    print('    [1] Continue')
    print('    [2] Save/Load')
    print('    [3] Stats/Inventory')
    print('    [4] Exit')
    opt = getch.getch()
    choice = bytes.decode(opt)

    if choice == '1':
        returnMap()
    elif choice == '2':
        Game_Status.save_load()
    elif choice == '3':
        inventory()
    elif choice == '4':
        print('\n'+'Are You Sure?'.center(28, ' '))
        print('Press [enter] to EXIT or'.center(28, ' '))
        print('any other key to continue'.center(28, ' '))
        exitKey = getch.getch()
        key = bytes.decode(exitKey)
        if key == '\r':
            cls()
            sys.exit(0)
        else:
            menu()
    else:
        menu()

    
class mapPos():
    x = 1
    y = 1

    compx = 2
    compy = 1

    walkables = ['.', ' ']
    walls = ['|', '#', 'M', '^', '_',  '-', 'Q', '@', 'A', 'W', 'T', '\\', '/']


def inventory():
    cls()
    print('\n    --INVENTORY:\n    [1] Charge Spells\n    [2] Stats\n    [3] Map\n\n    [4] Back')
    opt = getch.getch() ; choice = bytes.decode(opt)
    if choice == '4':
        menu()
    elif choice == '1':
        charge_spells()
    elif choice == '2':
        cls()
        print('\n    --STATS:')
        print('    COMP:      '+states.companion)
        print('    HP:        '+str(states.pl_hp))
        print('    Gold:      '+str(states.gold))
        print('    Magicka:   '+str(states.magicka))
        print('    Sword Dmg: '+str(states.swordDam))
        print('    Spells: ')
        for key, value in states.spellList.items():
            print('      -'+key+' ('+str(value)+')')
        input('\n    [enter]')
        inventory()
    elif choice == '3':
        cls()
        print('\n    --MAP')
        for i in range(len(maps.worldMap.wMap)):
            print('\n    ', end ='')
            for j in range(len(maps.worldMap.wMap[0])):
                print(maps.worldMap.wMap[i][j], end='')
        input()
        inventory()
    else:
        inventory()
        

def charge_spells(): # take some args
    cls()
    magicka = states.magicka
    spells = states.spellList
    itemList = []
    spellCosts = ['2', '1', '4', '3']
    i = 1
    print('\n    --CHARGE SPELLS'+(' '*7)+'-COST')
    
    for key, value in spells.items():
        print(('    [' +str(i)+ '] ' +key+'('+str(value)+')').ljust(24, ' '), end='')
        print(('-'+spellCosts[i-1]+' mg').rjust(7, ' '))
        itemList.append(key)
        i +=1
    print('\n    ['+str(i)+'] Back' + ('MAGICKA: '+str(magicka)).rjust(19, ' '))
    # Player Input
    magChar = getch.getch()
    choice = bytes.decode(magChar)
    try:
        if choice == str(i):
            menu()
        elif choice == '0':
            charge_spells()
        else:
            if magicka < int(spellCosts[int(choice)-1]):
                print('\n    # NOT ENOUGH MAGICKA #')
                input()
                charge_spells()
            else:
                print('\n    -'+itemList[int(choice)-1]+' Charged +1')
                states.magicka -= int(spellCosts[int(choice)-1])
                states.spellList[itemList[int(choice)-1]] +=1
                input()
                charge_spells()
                    
    except (ValueError,IndexError):
        charge_spells()


class comp_Anne():

    def healing():
        hp = randint(2, 5)
        states.pl_hp += hp
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f'\n    Anne heals you +{hp} HP')

    def magicka():
        spellList = []
        for key, value in states.spellList.items():
            spellList.append(key)
        spell = random.choice(spellList)
        states.spellList[spell] += 1
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f'\n    Anne charges your {spell} +1!')

    def choice():
        abilities = [comp_Anne.healing, comp_Anne.magicka]
        random.choice(abilities)()
        

class comp_Tank():

    def strike():
        hp = randint(states.swordDam,(states.swordDam+5))
        states.enemyHp -= hp
        if states.enemyHp < 0:
            states.enemyHp = 0
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f'\n    Tank strikes {states.currentEnemy} for -{hp} HP!')

    def slash():
        hp = randint((states.swordDam-2),(states.swordDam+2))
        states.enemyHp -= hp
        if states.enemyHp < 0:
            states.enemyHp = 0
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f'\n    Tank slashes {states.currentEnemy} for -{hp} HP!')

    def choice():
        abilities = [comp_Tank.strike, comp_Tank.slash]
        random.choice(abilities)()


class comp_Wizard():

    def fireball():
        hp = randint(2,8)
        states.enemyHp -= hp
        if states.enemyHp < 0:
            states.enemyHp = 0
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f'\n    Wizard uses fireball on {states.currentEnemy} for -{hp} HP!')

    def healing():
        hp = randint(2, 5)
        states.pl_hp += hp
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f'\n    Wizard heals you +{hp} HP')

    def choice():
        abilities = [comp_Wizard.fireball, comp_Wizard.healing]
        random.choice(abilities)()



## APPEND COMPANION ABILITYIES TO DICT IN STATES
states.comp_abList['Anne'] = comp_Anne.choice
states.comp_abList['Tank'] = comp_Tank.choice
states.comp_abList['Wizard'] = comp_Wizard.choice


def writeMaps(wmap):
    mapx = maps.worldMap.wMap

    #search map for X char and delete it
    for x in range(len(mapx)):
        for y in range(len(mapx[0])):
            if mapx[x][y] == 'X':
                mapx[x][y] = ' '
  
    if wmap == mapOne:
        mapx[0][0] = '['
        mapx[0][1] = 'X'
        mapx[0][2] = ']'
    elif wmap == mapTwo:
        mapx[0][3] = '['
        mapx[0][4] = 'X'
        mapx[0][5] = ']'
    elif wmap == mapThree:
        mapx[0][6] = '['
        mapx[0][7] = 'X'
        mapx[0][8] = ']'
    elif wmap == mapFour:
        mapx[1][6] = '['
        mapx[1][8] = ']'


        

def printMap(mapx):
    print('\n    HP:'+str(states.pl_hp)+'  G:' +str(states.gold))
    for i in range(len(mapx)):
        if i < 1:
            pass
        else:
            print()
        for j in range(len(mapx[0])):
            if j == 0:
                print('    ', end='')
            else:
                pass
            print(mapx[i][j], end='')
    print()

    

########################
##   ACTUAL GAMEPLAY  ##    
########################    

def mapOne():
    mapx = ''
    states.lvlState = 0

    # add to inv.map
    writeMaps(mapOne) 
    
    while True:
        cls()
        mapx = maps.rewriteMapOne(mapx, states.comp_char)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        printMap(mapx)

       # get player input
        plDir = getch.getch()
        plMove = bytes.decode(plDir)
        if plMove == 'd' and mapx[mapPos.x][mapPos.y+1] == ']':
            mapPos.x = 2
            mapPos.y = 1
            mapTwo()
            
        #elif plMove == 'd' and mapx[mapPos.x][mapPos.y+1] != '|' and mapx[mapPos.x][mapPos.y+1] != 'M':
        elif plMove == 'd' and mapx[mapPos.x][mapPos.y+1] not in mapPos.walls:
            mapPos.y +=2
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] not in mapPos.walls:
            mapPos.y -=2
        elif plMove == 'w' and mapx[mapPos.x-1][mapPos.y] not in mapPos.walls:
            mapPos.x -=1
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] not in mapPos.walls:
            mapPos.x +=1   
        elif plMove == '\r' and (mapx[mapPos.x+1][mapPos.y] == 'M' or mapx[mapPos.x][mapPos.y-1] == 'M' or mapx[mapPos.x][mapPos.y+1] == 'M'):
            talkingPerson(faces.man.face, faces.man.messages)

        #Companion CONVO
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'A' or mapx[mapPos.x][mapPos.y+1] == 'A'):
            talkingPerson(faces.anne.face, faces.anne.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'W' or mapx[mapPos.x][mapPos.y+1] == 'W'):
            talkingPerson(faces.wizard.face, faces.wizard.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'T' or mapx[mapPos.x][mapPos.y+1] == 'T'):
            talkingPerson(faces.tank.face, faces.tank.comp_messages)
        
        # menu
        elif plMove == 'p':
            menu()
        cls()


def mapTwo():
    cls()
    mapx = ''
    states.lvlState = 1

    #write to inv.map
    writeMaps(mapTwo)
    
    while True:
        mapx = maps.rewriteMapTwo(mapx, states.comp_char,states.womanQuest)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        printMap(mapx)

        plDir = getch.getch()
        plMove = bytes.decode(plDir)
        # move to other maps
        if plMove == 'd' and mapx[mapPos.x][mapPos.y+1] == ']':
            mapPos.x = 2
            mapPos.y = 1
            mapThree()
        elif plMove == 'd' and mapx[mapPos.x][mapPos.y+1] == 'I':
            mapPos.x = 2
            mapPos.y = 1
            houseMap()
        elif plMove == 'd' and mapx[mapPos.x][mapPos.y+1] not in mapPos.walls:
            mapPos.y +=2
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] == '[':
            mapPos.x = 2
            mapPos.y = 7
            mapOne()
            
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] not in mapPos.walls:
            mapPos.y -=2
        elif plMove == 'w' and mapx[mapPos.x-1][mapPos.y] not in mapPos.walls:
            mapPos.x -=1
        elif plMove == 's' and mapx[mapPos.x][mapPos.y] == mapx[4][11]:
            cls()
            print('\tAWWW YEAH SECRET SAUCE!')
            if states.gold < 10:
                print('\tHere\'s some dough, boiii!')
                states.gold += 5
            input()
            mapTwo()    
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] not in mapPos.walls:
            mapPos.x +=1

        #Companion CONVO
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'A' or mapx[mapPos.x][mapPos.y+1] == 'A'):
            talkingPerson(faces.anne.face, faces.anne.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'W' or mapx[mapPos.x][mapPos.y+1] == 'W'):
            talkingPerson(faces.wizard.face, faces.wizard.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'T' or mapx[mapPos.x][mapPos.y+1] == 'T'):
            talkingPerson(faces.tank.face, faces.tank.comp_messages)


        elif plMove == '\r' and (mapx[mapPos.x-1][mapPos.y] == ('Q' or 'W' or 'A' or 'T') or mapx[mapPos.x][mapPos.y-1] == ('Q' or 'W' or 'A' or 'T') or mapx[mapPos.x][mapPos.y+1] == ('Q' or 'W' or 'A' or 'T')):
            if states.snakeDef == 1:
                states.womanQuest = '_'
                talkingPerson(faces.girl.face, faces.girl.messages3)
                if states.womanTalkedTo < 2:
                    states.gold += 5
                    states.womanTalkedTo =2   
            elif states.womanTalkedTo == 0:
                talkingPerson(faces.girl.face, faces.girl.messages)
                states.womanTalkedTo = 1
                states.womanQuest = '_'
            elif states.womanTalkedTo == 1 and states.snakeDef == 0:
                states.womanQuest = '_'
                talkingPerson(faces.girl.face, faces.girl.messages2)

        elif plMove == 'p':
            menu()
        cls()

def mapThree():
    cls()
    mapx = ''
    states.lvlState = 2

    #write to inv.map
    writeMaps(mapThree)
    
    while True:
        # pick map based on enemy defeated or not
        if states.companion == 'Tank':
            states.tank_char = ' '
        else:
            states.tank_char = 'T'

        if states.snakeDef == 0:
            mapx = maps.rewriteMapThree(mapx, states.comp_char, states.tank_char)
        elif states.snakeDef == 1:
            mapx = maps.rewriteMapThreeVictory(mapx, states.comp_char, states.tank_char)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        printMap(mapx)
    
        # combat initiation by proximity here
        if (mapx[mapPos.x+1][mapPos.y+1] == '@' or mapx[mapPos.x][mapPos.y+1] == '@' or mapx[mapPos.x-1][mapPos.y+1] == '@'
        or mapx[mapPos.x-1][mapPos.y-1] == '@' or mapx[mapPos.x+1][mapPos.y-1] == '@'):
            states.currentEnemy = 'SnakeMan'
            states.enemyHp = 100
            states.enemyBaseDam = 1
            talkingPerson(faces.snakeMan.face, faces.snakeMan.messages)
            states.snakeDef = 1
            combatState()
            mapThree()
        
        #player input
        plDir = getch.getch()
        plMove = bytes.decode(plDir)
        if plMove == 'd' and mapx[mapPos.x][mapPos.y+1] not in mapPos.walls:
            mapPos.y +=2
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] == '[':
            mapPos.x = 2
            mapPos.y = 11
            mapTwo()
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] not in mapPos.walls:
            mapPos.y -=2
        elif plMove == 'w' and mapx[mapPos.x-1][mapPos.y] not in mapPos.walls:
            mapPos.x -=1
        # room 4
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] == '=':
            mapPos.x = 1
            mapPos.y = 7
            mapFour()
            
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] not in mapPos.walls:
            mapPos.x +=1
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == '$' or mapx[mapPos.x][mapPos.y+1] == '$'):
            talkingPerson(faces.shopkeeper.face, faces.shopkeeper.messages)
            shop()

        #Companion CONVO
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'A' or mapx[mapPos.x][mapPos.y+1] == 'A'):
            talkingPerson(faces.anne.face, faces.anne.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'W' or mapx[mapPos.x][mapPos.y+1] == 'W'):
            talkingPerson(faces.wizard.face, faces.wizard.comp_messages)

        ## TANK COMPANION
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'T' or mapx[mapPos.x][mapPos.y+1] == 'T'):
            if states.companion != 'Tank':
                talkingPerson(faces.tank.face, faces.tank.messages)
                print('\n    -Make Tank Your Companion?\n    You Can Only Have One Companion At A Time')
                print('\n    -slash    -strike')
                print('\n    [1] Yes\n    [2] No')
                compAns = getch.getch()
                ans = bytes.decode(compAns)
                if ans == '1':
                    states.companion = 'Tank'
                    states.comp_char = 'T'
                else:
                    pass
            else:
                talkingPerson(faces.tank.face, faces.tank.comp_messages)
        elif plMove == 'p':
            menu()
        cls()



def houseMap():
    cls()
    mapx = ''
    states.lvlState = 3

    while True:
        if states.companion == 'Anne':
            states.anne_char = ' '
            states.wizard_char = 'W'
        elif states.companion == 'Wizard':
            states.wizard_char = ' '
            states.anne_char = 'A'
        elif states.companion == 'Tank':
            states.anne_char = 'A'
            states.wizard_char = 'W'
        mapx = maps.rewriteHouse(mapx, states.comp_char, states.anne_char, states.wizard_char)
        mapx[mapPos.x][mapPos.y] = 'X'


        printMap(mapx)


        plDir = getch.getch()
        plMove = bytes.decode(plDir)
        # pl movement
        if plMove == 'd' and mapx[mapPos.x][mapPos.y+1] != '|' and mapx[mapPos.x][mapPos.y+1] != '#':
            mapPos.y +=2
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] == '[':
            mapPos.x = 4
            mapPos.y = 5
            mapTwo()
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] != '|':
            mapPos.y -=2
        elif plMove == 'w' and mapx[mapPos.x-1][mapPos.y] != '^':
            mapPos.x -=1
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] != '_' and mapx[mapPos.x+1][mapPos.y] != '#':
            mapPos.x +=1
        elif plMove == '\r' and (mapx[mapPos.x-1][mapPos.y] == '#' or mapx[mapPos.x][mapPos.y-1] == '#' or mapx[mapPos.x][mapPos.y+1] == '#'):
            if states.pl_hp < 10:
                states.pl_hp = 10
            talkingPerson(faces.oven.face, faces.oven.messages)

        #Companion CONVO
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'T' or mapx[mapPos.x][mapPos.y+1] == 'T'):
            talkingPerson(faces.tank.face, faces.tank.comp_messages)

        ## ANNE COMPANION
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'A' or mapx[mapPos.x][mapPos.y+1] == 'A'):
            if states.companion != 'Anne':
                talkingPerson(faces.anne.face, faces.anne.messages)
                print('\n    -Make Anne Your Companion?\n    You Can Only Have One Companion At A Time')
                print('\n    -healing    -spell charging')
                print('\n    [1] Yes\n    [2] No')
                compAns = getch.getch()
                ans = bytes.decode(compAns)
                if ans == '1':
                    states.companion = 'Anne'
                    states.comp_char = 'A'
                else:
                    pass
            else:
                talkingPerson(faces.anne.face, faces.anne.comp_messages)

        ## WIZARD COMPANION
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'W' or mapx[mapPos.x][mapPos.y+1] == 'W'):
            if states.companion != 'Wizard':
                talkingPerson(faces.wizard.face, faces.wizard.messages)
                print('\n    -Make Wizard Your Companion?\n    You Can Only Have One Companion At A Time')
                print('\n    -fireball    -healing')
                print('\n    [1] Yes\n    [2] No')
                compAns = getch.getch()
                ans = bytes.decode(compAns)
                if ans == '1':
                    states.companion = 'Wizard'
                    states.comp_char = 'W'
                else:
                    pass
            else:
                talkingPerson(faces.wizard.face, faces.wizard.comp_messages)
        elif plMove == 'p':
            menu()
        cls()



def mapFour():
    cls()
    mapx = ''
    states.lvlState = 4

    writeMaps(mapFour)

    while True:
        if states.kingDef == 0:
            mapx = maps.rewriteMapFour(mapx, states.comp_char)
        elif states.kingDef == 1:
            mapx = maps.rewriteMapFourVictory(mapx, states.comp_char)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        printMap(mapx)
    
        # combat initiation by proximity here
        if mapx[mapPos.x-1][mapPos.y] == '@':
            states.currentEnemy = 'the King'
            states.enemyHp = 45
            states.enemyBaseDam = 4
            talkingPerson(faces.king.face, faces.king.messages)
            states.kingDef = 1
            combatState()
            mapFour()
        
        #player input
        plDir = getch.getch()
        plMove = bytes.decode(plDir)
        if plMove == 'd' and mapx[mapPos.x][mapPos.y+1] not in mapPos.walls:
            mapPos.y +=2
        elif plMove == 'a' and mapx[mapPos.x][mapPos.y-1] not in mapPos.walls:
            mapPos.y -=2
        # to map3
        elif plMove == 'w' and mapx[mapPos.x-1][mapPos.y] == '=':
            mapPos.x = 7
            mapPos.y = 7
            mapThree()
        elif plMove == 'w' and (mapPos.x == 8 and mapPos.y == 5): 
            cls()
            print('\n    YOU WIN CONGRATS')
            states.gold += 1000
            input()
            mapFour()
        elif plMove == 'w' and mapx[mapPos.x-1][mapPos.y] not in mapPos.walls:
            mapPos.x -=1
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] not in mapPos.walls:
            mapPos.x +=1

        # SHOP
        elif plMove == '\r' and mapx[mapPos.x][mapPos.y+1] == '$':
            talkingPerson(faces.shopkeeper.face, faces.shopkeeper.messages)
            shop()

        #Companion CONVO
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'A' or mapx[mapPos.x][mapPos.y+1] == 'A'):
            talkingPerson(faces.anne.face, faces.anne.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'W' or mapx[mapPos.x][mapPos.y+1] == 'W'):
            talkingPerson(faces.wizard.face, faces.wizard.comp_messages)
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == 'T' or mapx[mapPos.x][mapPos.y+1] == 'T'):
            talkingPerson(faces.tank.face, faces.tank.comp_messages)

        # menu
        elif plMove == 'p':
            menu()
        cls()



  #########################
 ####  TALKING/SHOPS  ####
########################


def talkingPerson(fc, ms):  #(face, messages)
    cls()
    face = fc
    messages = ms
    for i in range(len(messages)):
        cls()
        print(random.choice(face))
        text = textwrap.wrap(messages[i], 25)
        for j in range(len(text)):
            print(text[j].center(36))
        input('\n'+'[enter]'.center(36))


def shop():
    cls()
    gold = states.gold
    shop_items = states.shop_items
    itemList = []
    i = 1
    print(faces.shopkeeper.face[0])
    print('    SHOP INVENTORY'+(' '*6)+'G: '+str(gold)+'g')
    
    for key, value in shop_items.items():
        print(('    [' +str(i)+ '] ' +key).ljust(20, ' '), end='')
        print(('-'+str(value)+'g').rjust(11, ' '))
        itemList.append(key)
        i +=1
    print('\n    ['+str(i)+'] Back')

    # Player Input
    shopChar = getch.getch()
    choice = bytes.decode(shopChar)
    try:
        if choice == str(i):
            pass
        elif choice == '0':
            shop()
        else:
            itemCost = shop_items.get(itemList[int(choice)-1])
            if gold < itemCost:
                print('\n    # YOU DON\'T HAVE ENOUGH GOLD#')
                input()
                shop()
            else:
                cls()
                print(faces.shopkeeper.face[0])
                print('\n'+('Purchase '+itemList[int(choice)-1]+'?').center(34, ' '))
                print('\n    [1] Yes\n    [2] No')
                confirmChar = getch.getch()
                confirm = bytes.decode(confirmChar)

                if confirm == '2':
                    shop()
                elif confirm == '1':
                    if itemList[int(choice)-1] == 'Sword dam +1':
                        states.gold -= itemCost
                        states.swordDam += 1
                    elif itemList[int(choice)-1] == 'Minor Amulet':
                        states.gold -= itemCost
                        states.spellList['Minor Amulet']= 1
                        del states.shop_items['Minor Amulet']
                    elif itemList[int(choice)-1] == 'Magicka +1':
                        states.gold -= itemCost
                        states.magicka += 1
                    cls()
                    print(faces.shopkeeper.face[1])
                    print('\n          Item Purchased')
                    input()
                    shop()
                else:
                    shop()
    except (ValueError, IndexError):
        shop()        

        

##################
##    COMBAT    ##   
##################
    
def combatState():
    sDmg = states.swordDam
    while (states.enemyHp > 0 and states.pl_hp > 0):
        cls()
        if states.companion != '':
            print(maps.battleZone[2])
        else:
            print(maps.battleZone[0])
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f"\n    [1] Sword Attack\n    [2] Spells")

        ansChar = getch.getch()
        ans = bytes.decode(ansChar)

        if (ans == '1'):
            enemy_dam = randint(sDmg,sDmg+3)
            states.enemyHp -= enemy_dam
            if states.enemyHp < 0:
                states.enemyHp = 0
            cls()
            if states.companion != '':
                print(maps.battleZone[2])
            else:
                print(maps.battleZone[0])
            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
            print("\n    -", enemy_dam, " hp to "+states.currentEnemy+"!")
            input()

            if (states.enemyHp <= 0):
                victory()
            elif states.companion != '':
                companionAttack()
            else:
                enemyAttack()

        elif (ans == '2'):
            cls()
            if states.companion != '':
                print(maps.battleZone[2])
            else:
                print(maps.battleZone[0])
            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
            print('\n'+'--SPELLS--'.center(28, ' ')+'\n')
            i = 1
            spellList = []
            for key, value in states.spellList.items():
                print('    ['+str(i)+'] '+key+' ('+str(value)+')')
                spellList.append(key)
                i+=1
            print('    ['+str(i)+'] Back') ; spellList.append('Back')
            try:
                spellChar = getch.getch()
                spell = bytes.decode(spellChar)
                if spellList[int(spell)-1] == 'Back':
                    continue
                else:
                    # check if player is out of spell
                    num = states.spellList.get(spellList[int(spell)-1])
                    if num == 0:
                        print('    You Don\'t Have Anymore of that Spell!')
                        input()
                    else:
                        cls()
                        if states.companion != '':
                            print(maps.battleZone[2])
                        else:
                            print(maps.battleZone[0])
                        # Healing
                        if spellList[int(spell)-1] == 'Healing':
                            healing = randint(2,6)
                            states.pl_hp += healing
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use Healing! +{healing}HP')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.companion != '':
                                companionAttack()
                            else:
                                enemyAttack()
                        # Damage Spells
                        else:
                            damage = 0
                            if spellList[int(spell)-1] == 'Fireball':
                                damage = randint(3,7)
                            elif spellList[int(spell)-1] == 'ThunderStrike':
                                damage = 10
                            elif spellList[int(spell)-1] == 'Minor Amulet':
                                damage = randint(5,10)
                            states.enemyHp -= damage
                            if states.enemyHp < 0:
                                states.enemyHp = 0
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use {spellList[int(spell)-1]}! -{damage} HP to {states.currentEnemy}')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.enemyHp <= 0:
                                victory()
                            elif states.companion != '':
                                companionAttack()
                            else:
                                enemyAttack()
                                
                                                
            except ValueError:
                print('\n'+'    -Invalid Option-')
                input()


                
def companionAttack():
    cls()
    print(maps.battleZone[3])
    states.comp_abList[states.companion]()
    input()
    if states.enemyHp == 0:
        victory()
    else:
        enemyAttack()

                                  

def enemyAttack():
    cls()
    play_dam = randint(states.enemyBaseDam, states.enemyBaseDam+4)
    states.pl_hp -= play_dam
    if states.pl_hp < 0:
        states.pl_hp = 0
    if states.companion != '':
        print(maps.battleZone[4])
    else:
        print(maps.battleZone[1])
    print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
    print(f'\n    {states.currentEnemy} attacks! -{play_dam} HP')
    input()

    if (states.pl_hp <= 0):
        print('    You died!') #gamestatus.death
        input()
        sys.exit(0)
    else:
        combatState()


def victory():
    cls()
    if states.companion != '':
        print(maps.battleZone[4])
    else:
        print(maps.battleZone[1])
    print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
    print('\n        ---You Won!---')
    input()
    


############################
##    SAVE/LOAD SYSTEM    ##
############################


class Game_Status(object):


    def save_load():
        cls()
        print('\n    --SAVE/LOAD')
        print('    [1] Save\n    [2] Load\n\n    [3] Back')

        opt = getch.getch()
        choice = bytes.decode(opt)

        if choice == '3':
            menu()
        elif choice == '1':
            Game_Status.save()
        elif choice == '2':
            Game_Status.load()
        else:
            Game_Status.save_load()
    
    def save():
        # SAVE ORDER: xpos, ypos, map, hp, gold, magicka, map, swordDam, companionN, compchar,
        #             spells, shopitems, compAnne, comptank, compwizard woman state, womanQuest snakedef, kingdef
        save_xpos = str(mapPos.x) ; save_ypos = str(mapPos.y) ; save_Map = str(states.lvlState)
        save_hp = str(states.pl_hp) ; save_gold = str(states.gold) ; save_magicka = str(states.magicka)
        save_map = str(maps.worldMap.wMap) ; save_swordDam = str(states.swordDam)
        save_companionName = states.companion ; save_compChar = states.comp_char
        save_spells = str(states.spellList) ; save_shopItems = str(states.shop_items)
        save_anne = states.anne_char ; save_tank = states.tank_char ; save_wizard = states.wizard_char
        save_womanState = str(states.womanTalkedTo) ; save_womanQuest = states.womanQuest
        save_snakeDef = str(states.snakeDef) ; save_kingDef = str(states.kingDef)

        cls()
        saveFiles = []
        for filename in os.listdir('.'):
            if filename.startswith('savegame'):
                saveFiles.append(filename)
        print('\n    --SAVE AS:')
        print('    [1] New Save')
        i = 2
        for file in saveFiles:
            print('    ['+str(i)+'] '+file)
            i +=1
        print('\n    ['+str(i)+'] Back')

        fileChoice = getch.getch()
        file = bytes.decode(fileChoice)

        #name new file
        invalidChars = ['?', '\\', '/', ':', '"', '<', '>', '*']
        if file == str(i):
            menu()
        else:
            if file == '0':
                Game_Status.save() 
            elif file == '1':
                cls()
                print('    ENTER A NAME FOR FILE:')
                name = input('    > ')
                for i in invalidChars:
                    if i in name:
                        print('\n    #INVALID CHARACTERS IN NAME#')
                        input()
                        Game_Status.save()
                openfile = open('savegame_'+name+'.txt', 'w+')
                
            # choose save file
            else:
                try:
                    openfile = open(saveFiles[int(file)-2], 'w+')
                except (ValueError, IndexError):
                    Game_Status.save()            
            # do tha savin
            # SAVE ORDER: xpos, ypos, map, hp, gold, magicka, map, swordDam, companionN, compchar,
        #             spells, shopitems, compAnne, comptank, compwizard woman state, womanQuest snakedef, kingdef
            openfile.truncate()
            openfile.write(save_xpos); openfile.write("\n"); openfile.write(save_ypos)
            openfile.write("\n"); openfile.write(save_Map) ; openfile.write("\n")
            openfile.write(save_hp) ; openfile.write("\n") ; openfile.write(save_gold)
            openfile.write("\n") ; openfile.write(save_magicka) ; openfile.write("\n")
            openfile.write(save_map) ; openfile.write('\n') ; openfile.write(save_swordDam)
            openfile.write('\n') ; openfile.write(save_companionName)
            openfile.write('\n') ; openfile.write(save_compChar)
            openfile.write("\n") ; openfile.write(save_spells)
            openfile.write("\n") ; openfile.write(save_shopItems); openfile.write("\n")
            openfile.write(save_anne) ; openfile.write("\n") ; openfile.write(save_tank)
            openfile.write("\n") ; openfile.write(save_wizard) ; openfile.write("\n")
            openfile.write(save_womanState) ; openfile.write("\n") ; openfile.write(save_womanQuest)
            openfile.write("\n") ; openfile.write(save_snakeDef) ; openfile.write("\n")
            openfile.write(save_kingDef) ; openfile.write("\n") ; openfile.close()

            print('\n    Game Saved')
            input('\n    [enter]')


    def load():
        cls()
        saveFiles = []
        for filename in os.listdir('.'):
            if filename.startswith('savegame'):
                saveFiles.append(filename)
        print('\n    --SAVED GAMES:')
        i = 1
        for file in saveFiles:
            print('    ['+str(i)+'] '+file)#.strip('.txt'))
            i +=1
        print('\n    ['+str(i)+'] Back')
        fileChoice = getch.getch()
        file = bytes.decode(fileChoice)

        if file == str(i):
            menu()
        elif file == '0':
            Game_Status.load()
        else:
            try:
                load_file = open(saveFiles[int(file)-1])
            except (ValueError, IndexError):
                Game_Status.load()
            
            try:
                # SAVE ORDER: xpos, ypos, map, hp, gold, magicka, map, swordDam, companionN, compchar,
        #             spells, shopitems, compAnne, comptank, compwizard woman state, womanQuest snakedef, kingdef
                load_xpos = int(load_file.readline()) ; load_ypos = int(load_file.readline())
                load_Map = int(load_file.readline()) ; load_hp = int(load_file.readline())
                load_gold = int(load_file.readline()) ; load_magicka = int(load_file.readline())
                load_map = load_file.readline() ; load_swordDam = int(load_file.readline())
                load_companion = load_file.readline() 
                load_compChar = load_file.readline() ; load_spells = load_file.readline()
                load_shopItems = load_file.readline() ; load_anne = load_file.readline()
                load_tank = load_file.readline() ; load_wizard = load_file.readline()
                load_womanState = int(load_file.readline()) ; load_womanQuest = load_file.readline()
                load_snakedef = int(load_file.readline()) ; load_kingDef = int(load_file.readline())
                load_file.close()
                
                #World_Stats.pl_name = load_name.rstrip('\n')    #rstrip to remove 'n' so that player name isnt indented a line when they load the game
                mapPos.x = load_xpos
                mapPos.y = load_ypos
                states.lvlState = load_Map
                states.pl_hp = load_hp
                states.gold = load_gold
                states.magicka = load_magicka
                maps.worldMap.wMap = ast.literal_eval(load_map)
                states.swordDam = load_swordDam
                #companion name
                if load_companion == '\n':
                    states.companion = ''
                else:
                    states.companion = load_companion.rstrip('\n')
                states.comp_char = load_compChar.rstrip('\n')
                states.spellList = ast.literal_eval(load_spells)
                states.shop_items = ast.literal_eval(load_shopItems)
                states.anne_char = load_anne.rstrip('\n')
                states.tank_char = load_tank.rstrip('\n')
                states.wizard_char = load_wizard.rstrip('\n')
                states.womanTalkedTo = load_womanState
                states.womanQuest = load_womanQuest.rstrip('\n')
                states.snakeDef = load_snakedef
                states.kingDef = load_kingDef
                
                print("\n    Game Loaded.\n")
                input('    [enter]')
                returnMap()
                    

            except ValueError:
                cls()
                print('\n\n    #  SAVE FILE CORRUPTED OR EMPTY  #')
                print('    # PLEASE SELECT A DIFFERENT FILE #')
                print('\n    [enter]')
                input()
                Game_Status.load()


mapOne()