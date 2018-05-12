# game.py - simple game test

### CH LOG:
###  - Implement CLS function
###  - figure out how to return to same spot after combat and change combat state so enemy is gone!
###    possibly draw new maps without enemy and load those in if statement that checks states.xstate
###    and loads accordingly the right map so you dont have to fuck with the controls

import sys, os, textwrap, random
import msvcrt as getch
from random import randint
import faces, maps


def cls():
    os.system('CLS')

class states():
    pl_hp = 15
    gold = 0
    spellList = {'Fireball':2, 'Healing':1, 'ThunderStrike':1}
    
    currentEnemy= ''
    enemyHp = 0
    
class mapPos():
    x = 1
    y = 1
    

def mapOne():
    mapx = ''
    
    while True:
        os.system('CLS')
        mapx = maps.rewriteMapOne(mapx)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        for i in range(len(mapx)):
            print()
            for j in range(len(mapx[0])):
                print(mapx[i][j], end='')
        print('\n HP:'+str(states.pl_hp)+'  G:' +str(states.gold))

        plDir = input('\n   ')
        if plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] == ']':
            mapPos.x = 2
            mapPos.y = 1
            mapTwo()
            
        elif plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] != '|' and mapx[mapPos.x][mapPos.y+1] != 'M':
            mapPos.y +=2
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] != '|' and mapx[mapPos.x][mapPos.y-1] != 'M':
            mapPos.y -=2
        elif plDir.lower() == 'w' and mapx[mapPos.x-1][mapPos.y] != '_' and mapx[mapPos.x-1][mapPos.y] != 'M':
            mapPos.x -=1
        elif plDir.lower() == 's' and mapx[mapPos.x+1][mapPos.y] != '^' and mapx[mapPos.x+1][mapPos.y] != 'M':
            mapPos.x +=1
        elif plDir.lower() == ' ' and (mapx[mapPos.x+1][mapPos.y] == 'M' or mapx[mapPos.x][mapPos.y-1] == 'M' or mapx[mapPos.x][mapPos.y+1] == 'M'):
            talkingPerson(faces.man.face, faces.man.messages)
        
        # Exit input
        elif plDir.lower() == 'p':
            sys.exit(0)
        
        os.system('CLS')


def mapTwo():
    os.system('CLS')
    mapx = ''
    
    while True:
        mapx = maps.rewriteMapTwo(mapx)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        for i in range(len(mapx)):
            print()
            for j in range(len(mapx[0])):
                print(mapx[i][j], end='')
        print('\n HP:'+str(states.pl_hp)+'  G:' +str(states.gold))
        

        plDir = input('\n   ')
        if plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] == ']':
            mapPos.x = 2
            mapPos.y = 1
            mapThree()
        elif plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] == 'I':
            mapPos.x = 2
            mapPos.y = 1
            houseMap()
        elif plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] != '|' and mapx[mapPos.x][mapPos.y+1] != 'Q':
            mapPos.y +=2
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] == '[':
            mapPos.x = 2
            mapPos.y = 7
            mapOne()
            
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] != '|' and mapx[mapPos.x][mapPos.y-1] != 'Q':
            mapPos.y -=2
        elif plDir.lower() == 'w' and mapx[mapPos.x-1][mapPos.y] != '_' and mapx[mapPos.x-1][mapPos.y] != 'Q':
            mapPos.x -=1
        elif plDir.lower() == 's' and mapx[mapPos.x][mapPos.y] == mapx[4][11]:
            os.system('CLS')
            print('\tAWWW YEAH SECRET SAUCE!')
            if states.gold < 10:
                print('\tHere\'s some dough, boiii!')
                states.gold += 5
            input()
            mapTwo()
            
        elif plDir.lower() == 's' and mapx[mapPos.x+1][mapPos.y] != '^' and mapx[mapPos.x+1][mapPos.y] != 'Q':
            mapPos.x +=1
        elif plDir.lower() == ' ' and (mapx[mapPos.x-1][mapPos.y] == 'Q' or mapx[mapPos.x][mapPos.y-1] == 'Q' or mapx[mapPos.x][mapPos.y+1] == 'Q'):
            talkingPerson(faces.girl.face, faces.girl.messages)
        
        # Exit input
        elif plDir.lower() == 'p':
            sys.exit(0)
        os.system('CLS')


def mapThree():
    os.system('CLS')
    mapx = ''
    
    while True:
        mapx = maps.rewriteMapThree(mapx)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        for i in range(len(mapx)):
            print()
            for j in range(len(mapx[0])):
                print(mapx[i][j], end='')
        print('\n HP:'+str(states.pl_hp)+'  G:' +str(states.gold))
        

        plDir = input('\n   ')
        if plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] != '|' and mapx[mapPos.x][mapPos.y+1] != '@':
            mapPos.y +=2
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] == '[':
            mapPos.x = 2
            mapPos.y = 11
            mapTwo()
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] != '|' and mapx[mapPos.x][mapPos.y-1] != '@':
            mapPos.y -=2
        elif plDir.lower() == 'w' and mapx[mapPos.x-1][mapPos.y] != '_' and mapx[mapPos.x-1][mapPos.y] != '@':
            mapPos.x -=1
        elif plDir.lower() == 's' and mapx[mapPos.x+1][mapPos.y] == '-':
            os.system('CLS')
            print('SECRET ROOM YEAH BOIIII')
            input()
            mapPos.x = 7
            mapPos.y = 7
            mapThree()
        elif plDir.lower() == 's' and mapx[mapPos.x+1][mapPos.y] != '^' and mapx[mapPos.x+1][mapPos.y] != '@':
            mapPos.x +=1
        elif plDir.lower() == ' ' and (mapx[mapPos.x-1][mapPos.y] == '@' or mapx[mapPos.x][mapPos.y-1] == '@' or mapx[mapPos.x][mapPos.y+1] == '@'):
            states.currentEnemy = 'SnakeMan'
            states.enemyHp = 10
            talkingPerson(faces.snakeMan.face, faces.snakeMan.messages)
            combatState()
        
        # Exit input
        elif plDir.lower() == 'p':
            sys.exit(0)
        os.system('CLS')


def houseMap():
    os.system('CLS')
    mapx = ''

    while True:
        mapx = maps.rewriteHouse(mapx)
        mapx[mapPos.x][mapPos.y] = 'X'

        #print map
        for i in range(len(mapx)):
            print()
            for j in range(len(mapx[0])):
                print(mapx[i][j], end='')
        print('\n HP:'+str(states.pl_hp)+'  G:' +str(states.gold))
        

        plDir = input('\n   ')
        if plDir.lower() == 'd' and mapx[mapPos.x][mapPos.y+1] != '|' and mapx[mapPos.x][mapPos.y+1] != '#':
            mapPos.y +=2
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] == '[':
            mapPos.x = 4
            mapPos.y = 5
            mapTwo()
        elif plDir.lower() == 'a' and mapx[mapPos.x][mapPos.y-1] != '|':
            mapPos.y -=2
        elif plDir.lower() == 'w' and mapx[mapPos.x-1][mapPos.y] != '^':
            mapPos.x -=1
        elif plDir.lower() == 's' and mapx[mapPos.x+1][mapPos.y] != '_' and mapx[mapPos.x+1][mapPos.y] != '#':
            mapPos.x +=1
        elif plDir.lower() == ' ' and (mapx[mapPos.x-1][mapPos.y] == '#' or mapx[mapPos.x][mapPos.y-1] == '#' or mapx[mapPos.x][mapPos.y+1] == '#'):
            if states.pl_hp < 10:
                states.pl_hp = 10
            talkingPerson(faces.oven.face, faces.oven.messages)
        
        # Exit input
        elif plDir.lower() == 'p':
            sys.exit(0)
        os.system('CLS')
    


def talkingPerson(fc, ms):  #(face, messages)
    print('woprking')

    os.system('CLS')
    face = fc
    messages = ms
    for i in range(len(messages)):
        os.system('CLS')
        print(random.choice(face))
        text = textwrap.wrap(messages[i], 25)
        for j in range(len(text)):
            print(text[j].center(36))
        input('\n'+'[enter]'.center(36))



##################
##    COMBAT    ##   
##################
    
def combatState():
    while (states.enemyHp > 0 and states.pl_hp > 0):
        os.system('CLS')
        print(maps.battleZone[0])
        print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
        print(f"\n    [1] Sword Attack\n    [2] Spells")
        ans = input("    > ")

        if (ans == '1'):
            enemy_dam = randint(1,4)
            states.enemyHp -= enemy_dam
            os.system('CLS')
            print(maps.battleZone[0])
            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
            print("\n    -", enemy_dam, " hp to "+states.currentEnemy+"!")
            input()

            if (states.enemyHp <= 0):
                print(f'    --You\'ve killed {states.currentEnemy}!--')
                input()
                sys.exit(0)

            else:
                enemyAttack()

        elif (ans == '2'):
            os.system('CLS')
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
                spell = input('    > ')
                if spellList[int(spell)-1] == 'Back':
                    continue
                else:
                    # check if player is out of spell
                    num = states.spellList.get(spellList[int(spell)-1])
                    if num == 0:
                        print('    You Don\'t Have Anymore of that Spell!')
                        input()
                    else:
                        os.system('CLS')
                        print(maps.battleZone[0])
                        if spellList[int(spell)-1] == 'Fireball':
                            fireDam = randint(5,9)
                            states.enemyHp -= fireDam
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use {spellList[int(spell)-1]}! -{fireDam} HP to {states.currentEnemy}')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.enemyHp > 0:
                                enemyAttack()
                            else:
                                print('You won!')
                                input()
                                sys.exit(0)
                        elif spellList[int(spell)-1] == 'Healing':
                            healing = randint(2,5)
                            states.pl_hp += healing
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use Healing! +{healing}HP')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            enemyAttack()
                        elif spellList[int(spell)-1] == 'ThunderStrike':
                            states.enemyHp -= 10
                            print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
                            print(f'\n    You Use ThunderStrike! -10 HP to {states.currentEnemy}')
                            states.spellList[spellList[int(spell)-1]] -= 1
                            input()
                            if states.enemyHp > 0:
                                enemyAttack()
                            else:
                                print('You won!')
                                input()
                                sys.exit(0)     
                        
            except ValueError:
                print('    -Invalid Option-')
                input()


        
def enemyAttack():
    os.system('CLS')
    play_dam = randint(1,3)
    states.pl_hp -= play_dam
    print(maps.battleZone[1])
    print(f"    HP: {states.pl_hp}      {states.currentEnemy}: {states.enemyHp}")
    print(f'\n    {states.currentEnemy} attacks! -{play_dam} HP')
    input()

    if (states.pl_hp <= 0):
        print('You died!') #gamestatus.death
        input()
        sys.exit(0)
    else:
        combatState()

    

    
mapOne()

    

