# game.py - simple game test

### CH LOG:
###  - IN Iventory screen, make map and make map acquisition in game


import sys, os, textwrap, random, time, ast
import msvcrt as getch
from random import randint
import faces, maps


def cls():
    os.system('CLS')


class states():
    lvlState = 0
    pl_hp = 15
    gold = 200
    spellList = {'Fireball':2, 'Healing':1, 'ThunderStrike':1}
    shop_items = {'Sword dam +2':15, 'Minor Amulet':30, 'Magicka +1':10}
    magicka = 18
    swordDam = 2
    
    currentEnemy= ''
    enemyHp = 0

    #map 1 states

    #map 2 states
    womanTalkedTo = 0
    
    #map 3 states
    snakeDef = 0
    


def returnMap():
    if states.lvlState == 0:
        return mapOne()
    elif states.lvlState == 1:
        return mapTwo()
    elif states.lvlState == 2:
        return mapThree()
    elif states.lvlState == 3:
        return houseMap()


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

    walkables = ['.', ' ']
    walls = ['|', '#', 'M', '^', '_',  '-', 'Q', '@']


def inventory():
    cls()
    print('\n    --INVENTORY:\n    [1] Charge Spells\n    [2] Stats\n\n    [3] Back')
    opt = getch.getch() ; choice = bytes.decode(opt)
    if choice == '3':
        menu()
    elif choice == '1':
        charge_spells()
    elif choice == '2':
        cls()
        print('\n    --STATS:')
        print('    HP:        '+str(states.pl_hp))
        print('    Gold:      '+str(states.gold))
        print('    Magicka:   '+str(states.magicka))
        print('    Sword Dmg: '+str(states.swordDam))
        print('    Spells: ')
        for key, value in states.spellList.items():
            print('      -'+key+' ('+str(value)+')')
        input('\n    [enter]')
        inventory()
    else:
        inventory()
        

def charge_spells():
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
    print('\n    ['+str(i)+'] Back' + ('MAGICKA: '+str(magicka)).rjust(19, ' ')
)
    # Player Input
    magChar = getch.getch()
    choice = bytes.decode(magChar)
    try:
        if choice == str(i):
            pass
        elif choice == '0':
            charge_spells()
        else:
            # FIREBALL
            if itemList[int(choice)-1] == 'Fireball':
                if magicka < 2:
                    print('\n    # NOT ENOUGH MAGICKA #')
                    input()
                    charge_spells()
                else:
                    print('\n    -Fireball Charged +1')
                    states.magicka -= 2
                    states.spellList['Fireball'] += 1
                    input()
                    charge_spells()
            # HEALING
            if itemList[int(choice)-1] == 'Healing':
                if magicka < 1:
                    print('\n    # NOT ENOUGH MAGICKA #')
                    input()
                    charge_spells()
                else:
                    print('\n    -Healing Charged +1')
                    states.magicka -= 1
                    states.spellList['Healing']+=1
                    input()
                    charge_spells()
            # THUNDER STRIKE
            if itemList[int(choice)-1] == 'ThunderStrike':
                if magicka < 4:
                    print('\n    # NOT ENOUGH MAGICKA #')
                    input()
                    charge_spells()
                else:
                    print('\n    -ThunderStrike Charged +1')
                    states.magicka -= 4
                    states.spellList['ThunderStrike'] +=1
                    input()
                    charge_spells()
            # MINOR AMULET
            if itemList[int(choice)-1] == 'Minor Amulet':
                if magicka < 3:
                    print('\n    # NOT ENOUGH MAGICKA #')
                    input()
                    charge_spells()
                else:
                    print('\n    -Minor Amulet Charged +1')
                    states.magicka -= 3
                    states.spellList['Minor Amulet'] +=1
                    input()
                    charge_spells()
                    
    except (ValueError,IndexError):
        charge_spells()

        

def printMap(mapx):
    for i in range(len(mapx)):
        print()
        for j in range(len(mapx[0])):
            print(mapx[i][j], end='')
    print('\n HP:'+str(states.pl_hp)+'  G:' +str(states.gold))
    
    

def mapOne():
    mapx = ''
    states.lvlState = 0
    
    while True:
        cls()
        mapx = maps.rewriteMapOne(mapx)
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
        elif plMove == 'p':
            menu()
        cls()


def mapTwo():
    cls()
    mapx = ''
    states.lvlState = 1
    
    while True:
        if states.womanTalkedTo == 0 and states.snakeDef == 0:
            mapx = maps.rewriteMapTwoQuest(mapx)
        else: # states.womanTalkedTo == 1:
            mapx = maps.rewriteMapTwo(mapx)
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
        elif plMove == '\r' and (mapx[mapPos.x-1][mapPos.y] == 'Q' or mapx[mapPos.x][mapPos.y-1] == 'Q' or mapx[mapPos.x][mapPos.y+1] == 'Q'):
            if states.snakeDef == 1:
                talkingPerson(faces.girl.face, faces.girl.messages3)
                if states.womanTalkedTo < 2:
                    states.gold += 5
                    states.womanTalkedTo =2    
            elif states.womanTalkedTo == 0:
                talkingPerson(faces.girl.face, faces.girl.messages)
                states.womanTalkedTo = 1
            elif states.womanTalkedTo == 1 and states.snakeDef == 0:
                talkingPerson(faces.girl.face, faces.girl.messages2)

        elif plMove == 'p':
            menu()
        cls()

def mapThree():
    cls()
    mapx = ''
    states.lvlState = 2
    
    while True:
        # pick map based on enemy defeated or not
        if states.snakeDef == 0:
            mapx = maps.rewriteMapThree(mapx)
        elif states.snakeDef == 1:
            mapx = maps.rewriteMapThreeVictory(mapx)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        printMap(mapx)
    
        # combat initiation by proximity here
        if (mapx[mapPos.x+1][mapPos.y+1] == '@' or mapx[mapPos.x][mapPos.y+1] == '@' or mapx[mapPos.x-1][mapPos.y+1] == '@'
        or mapx[mapPos.x-1][mapPos.y-1] == '@' or mapx[mapPos.x+1][mapPos.y-1] == '@'):
            states.currentEnemy = 'SnakeMan'
            states.enemyHp = 10
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
        # secret room
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] == '-':
            cls()
            print('SECRET ROOM YEAH BOIIII')
            input()
            mapPos.x = 7
            mapPos.y = 7
            mapThree()
            
        elif plMove == 's' and mapx[mapPos.x+1][mapPos.y] not in mapPos.walls:
            mapPos.x +=1
        elif plMove == '\r' and (mapx[mapPos.x][mapPos.y-1] == '$' or mapx[mapPos.x][mapPos.y+1] == '$'):
            talkingPerson(faces.shopkeeper.face, faces.shopkeeper.messages)
            shop()
        elif plMove == 'p':
            menu()
        cls()

def houseMap():
    cls()
    mapx = ''
    states.lvlState = 3

    while True:
        mapx = maps.rewriteHouse(mapx)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        printMap(mapx)

        plDir = getch.getch()
        plMove = bytes.decode(plDir)
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
        elif plMove == 'p':
            menu()
        cls()


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
                    if itemList[int(choice)-1] == 'Sword dam +2':
                        states.gold -= itemCost
                        states.swordDam += 2
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
            print(maps.battleZone[0])
            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
            print("\n    -", enemy_dam, " hp to "+states.currentEnemy+"!")
            input()

            if (states.enemyHp <= 0):
                victory()
            else:
                enemyAttack()

        elif (ans == '2'):
            cls()
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
                    victory()
                else:
                    # check if player is out of spell
                    num = states.spellList.get(spellList[int(spell)-1])
                    if num == 0:
                        print('    You Don\'t Have Anymore of that Spell!')
                        input()
                    else:
                        cls()
                        print(maps.battleZone[0])

                        # Fireball
                        if spellList[int(spell)-1] == 'Fireball':
                            fireDam = randint(3,7)
                            states.enemyHp -= fireDam
                            if states.enemyHp < 0:
                                states.enemyHp = 0
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use {spellList[int(spell)-1]}! -{fireDam} HP to {states.currentEnemy}')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.enemyHp > 0:
                                enemyAttack()
                            else:
                                victory()
                                
                        # Healing
                        elif spellList[int(spell)-1] == 'Healing':
                            healing = randint(2,6)
                            states.pl_hp += healing
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use Healing! +{healing}HP')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            enemyAttack()

                        # Thunder Strike
                        elif spellList[int(spell)-1] == 'ThunderStrike':
                            states.enemyHp -= 10
                            if states.enemyHp < 0:
                                states.enemyHp = 0
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use ThunderStrike! -10 HP to {states.currentEnemy}')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.enemyHp > 0:
                                enemyAttack()
                            else:
                                victory()

                        # Minor Amulet
                        elif spellList[int(spell)-1] == 'Minor Amulet':
                            amuletDam = randint(5, 10)
                            states.enemyHp -= amuletDam
                            if states.enemyHp < 0:
                                states.enemyHp = 0
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use Minor Amulet!\n     -'+str(amuletDam)+f' HP to {states.currentEnemy}')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.enemyHp > 0:
                                enemyAttack()
                            else:
                                victory()

                        
            except ValueError:
                print('\n'+'    -Invalid Option-')
                input()

        
def enemyAttack():
    cls()
    play_dam = randint(1,3)
    states.pl_hp -= play_dam
    if states.pl_hp < 0:
        states.pl_hp = 0
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
    print(maps.battleZone[0])
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
        # SAVE ORDER: xpos, ypos, map, hp, gold, magicka, swordDam, spells, shopitems, woman state, snakedef
        save_xpos = str(mapPos.x) ; save_ypos = str(mapPos.y) ; save_Map = str(states.lvlState)
        save_hp = str(states.pl_hp) ; save_gold = str(states.gold) ; save_magicka = str(states.magicka)
        save_swordDam = str(states.swordDam) ; save_spells = str(states.spellList)
        save_shopItems = str(states.shop_items) ; save_womanState = str(states.womanTalkedTo)
        save_snakeDef = str(states.snakeDef)

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
                    #print('\n    NOT A VALID OPTION')
                    #print('\n    [enter]')
                    #input()
                    Game_Status.save()            
            # do tha savin
            # SAVE ORDER: xpos, ypos, map, hp, gold, magicka, swordDam, spells, shopitems, woman state, snakedef
            openfile.truncate()
            openfile.write(save_xpos); openfile.write("\n"); openfile.write(save_ypos)
            openfile.write("\n"); openfile.write(save_Map) ; openfile.write("\n")
            openfile.write(save_hp) ; openfile.write("\n") ; openfile.write(save_gold)
            openfile.write("\n") ; openfile.write(save_magicka) ; openfile.write("\n")
            openfile.write(save_swordDam) ; openfile.write("\n") ; openfile.write(save_spells)
            openfile.write("\n") ; openfile.write(save_shopItems); openfile.write("\n")
            openfile.write(save_womanState) ; openfile.write("\n") ; openfile.write(save_snakeDef)
            openfile.write("\n") ; openfile.close()

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
                #print('\n    NOT A VALID OPTION')
                #print('\n    [enter]')
                #input()
                Game_Status.load()
            
            try:
                # SAVE ORDER: xpos, ypos, map, hp, gold, magicka, swordDam, spells, shopitems, woman state, snakedef
                load_xpos = int(load_file.readline()) ; load_ypos = int(load_file.readline())
                load_Map = int(load_file.readline()) ; load_hp = int(load_file.readline())
                load_gold = int(load_file.readline()) ; load_magicka = int(load_file.readline())
                load_swordDam = int(load_file.readline()) ; load_spells = load_file.readline()
                load_shopItems = load_file.readline() ; load_womanState = int(load_file.readline())
                load_snakedef = int(load_file.readline()) ; load_file.close()
                
                #World_Stats.pl_name = load_name.rstrip('\n')    #rstrip to remove 'n' so that player name isnt indented a line when they load the game
                mapPos.x = load_xpos
                mapPos.y = load_ypos
                states.lvlState = load_Map
                states.pl_hp = load_hp
                states.gold = load_gold
                states.magicka = load_magicka
                states.swordDam = load_swordDam
                states.spellList = ast.literal_eval(load_spells)
                states.shop_items = ast.literal_eval(load_shopItems)
                states.womanTalkedTo = load_womanState
                states.snakeDef = load_snakedef
                
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
